import os
import shutil
import yaml
import markdown
from yattag import Doc, indent

POSTS_DIR = "posts"
OUTPUT_DIR = "site"

def load_posts():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith(".md"):
            continue
        with open(os.path.join(POSTS_DIR, filename), "r", encoding="utf-8") as f:
            content = f.read()

        # Extract YAML front matter
        if content.startswith("---"):
            _, fm, body = content.split("---", 2)
            meta = yaml.safe_load(fm)
            description_html = markdown.markdown(body.strip())
            meta["description_html"] = description_html
            posts.append(meta)

    # Sort by order
    posts.sort(key=lambda p: p["order"], reverse=True)
    return posts

def generate_site(posts):
    doc, tag, text, line = Doc().ttl()

    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            doc.stag('link', rel='stylesheet', href='style.css')
            doc.stag('link', rel='stylesheet',
                     href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css')

        with tag('body'):
            # HEADER
            with tag('header'):
                with tag('a', href='https://www.youtube.com/@FinFET', target="_blank"):
                    doc.stag('img', src='images/finfet.png', height=200)
                with tag('p'):
                    text("A channel on YouTube where I try stuff out with programming (especially Python) and tech in general.")
                social_media(tag)

            with tag('main'):
                with tag('aside'): pass
                with tag('article'):
                    for post in posts:
                        with tag('h2'): text(post['title'])
                        doc.asis(post['description_html'])
                        if post.get('video'):
                            video_frame(tag, post['video'])
                            doc.stag('br')
                        if post.get('game_id'):
                            game_frame(tag, text, post['game_id'],
                                       post.get('aspect', '5b4'),
                                       source=post.get('source', ''))
                            doc.stag('br')
                        if post.get('itch'):
                            itch_frame(tag, post['itch'])
                        if post.get('repo'):
                            repo(tag, text, post['repo'])
                        end_post(doc)
                with tag('aside'): pass

            with tag('footer'):
                social_media(tag)
                with tag('p'):
                    from datetime import datetime
                    text(f'{datetime.now().year} FinFET Channel. All rights reserved.')
            
            # Lazy load script
            doc.asis("""
            <script>
            document.addEventListener("DOMContentLoaded", function() {
            const lazyIframes = document.querySelectorAll("iframe[data-src]");
            const observer = new IntersectionObserver((entries, obs) => {
                entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const iframe = entry.target;
                    iframe.src = iframe.dataset.src;
                    iframe.removeAttribute("data-src");
                    obs.unobserve(iframe);
                }
                });
            }, { rootMargin: "200px" });
            lazyIframes.forEach(iframe => observer.observe(iframe));
            });
            </script>
            """)


    return indent(doc.getvalue())

# === Helper functions ===
def video_frame(tag, video):
    with tag('div', klass='videocontainer'):
        with tag('iframe',
                 **{'data-src': f'https://www.youtube.com/embed/{video}'},
                 loading='lazy',
                 klass='video',
                 allowfullscreen=''):
            pass

def itch_frame(tag, game):
    with tag('div', klass='itchcontainer'):
        with tag('iframe',
                 **{'data-src': f"https://itch.io/embed/{game}?dark=true"},
                 loading='lazy',
                 klass='video'):
            pass

def game_frame(tag, text, game, aspect_ratio='5b4', source=""):
    with tag('div', klass='gamecontainer' + aspect_ratio):
        with tag('iframe',
                 **{'data-src': source + game},
                 loading='lazy',
                 klass='video',
                 allowfullscreen=''):
            pass

def repo(tag, text, repository):
    with tag('p'):
        with tag('a', href=f'https://github.com/FinFetChannel/{repository}',
                 target="_blank"):
            text('GitHub Repository')

def end_post(doc):
    doc.stag('br'); doc.stag('hr'); doc.stag('br')

def social_media(tag):
    links = [
        #("https://www.reddit.com/r/FinFET/", "fab fa-reddit fa-2x"),
        ("https://finfetchannel.itch.io/", "fab fa-itch-io fa-2x"),
        ("https://www.youtube.com/@FinFET", "fab fa-youtube fa-2x"),
        ("https://github.com/FinFetChannel", "fab fa-github fa-2x"),
        ("mailto:finfetchannel@outlook.com", "fa fa-envelope fa-2x"),
        #("https://discord.com/invite/ZQmnZc4ARa", "fab fa-discord fa-2x"),
    ]
    for href, klass in links:
        with tag('a', href=href, target="_blank", klass=klass):
            pass

# === Copy static files ===
def prepare_output():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Copy style.css
    if os.path.exists("style.css"):
        shutil.copy("style.css", OUTPUT_DIR)

    # Copy images folder
    if os.path.exists("images"):
        shutil.copytree("images", os.path.join(OUTPUT_DIR, "images"))

if __name__ == '__main__':
    prepare_output()
    posts = load_posts()
    html = generate_site(posts)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
