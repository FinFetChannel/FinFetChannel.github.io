from yattag import Doc, indent

def main():
    doc, tag, text, line = Doc().ttl()

    doc.asis('<!DOCTYPE html>')

    with tag('html'):
        with tag('head'):
            doc.stag('link', rel='stylesheet', href='style.css')
            doc.stag('link', rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css')

        with tag('body'):
            with tag('header'):
                with tag('a', href='https://www.youtube.com/@FinFET', target="_blank"):
                    doc.stag('img', src='finfet.png', height=200)
                with tag('p'):
                    text('A channel on YouTube where I try stuff out with programming (especially Python) and tech in general.')
                social_media(tag)
            with tag('main'):
                with tag('aside'):pass

                with tag('article'):

                    ###############################################################################
                    with tag('h2'): text("2023 - DerDieDas Auto")
                    with tag('p'):
                        text(''' A racing game for training the genders (and articles) of German substantives. Made in Python with PyGame and PygBag.''')
                    video_frame(tag, 'Q3Gcv5q1fHY')
                    doc.stag('br')
                    game_frame(tag, text, '7562013', '16b9')
                    doc.stag('br')
                    itch_frame(tag, '1948138')
                    # repo(tag, text, '')
                    end_post(doc)

                    ###############################################################################
                    with tag('h2'): text("2022/2023 - Super MaRayO Caster")
                    with tag('p'):
                        text('''A first-person perspective version of Super Mario Bros. using raycasting, made in Python with PyGame and PygBag.''')
                    video_frame(tag, 'NXhRi8UgzZk')
                    doc.stag('br')
                    game_frame(tag, text, '7339954')
                    doc.stag('br')
                    itch_frame(tag, '1789891')
                    repo(tag, text, 'Super-MaRayO-Caster')
                    end_post(doc)

                    ###############################################################################
                    with tag('h2'): text("2022 - The LockPickin'joyer")
                    with tag('p'):
                        text('''A game inspired by the LockPickingLawyer, made in Python with PyGame and PygBag.''')
                    video_frame(tag, 'p-QJxbZmP3c')
                    doc.stag('br')
                    game_frame(tag, text, '6464625')
                    doc.stag('br')
                    itch_frame(tag, '1474850')
                    repo(tag, text, 'LockPickin-joyer')
                    end_post(doc)

                    ###############################################################################
                    with tag('h2'): text('2021/2022 - Dead And!')
                    with tag('p'): text('''A raycasting game made in Python, now with textures and sprites.''')
                    video_frame(tag, 'FLc6vUwyTdM')
                    with tag('p'):
                        text('Themes developed include:')
                        with tag('ul'):
                            for item in ['Floorcasting', 'Raycasting with textures and fake shadows', 'Sprites',
                                         'Enemies AI', 'Sounds', 'Simple GUI and menus', 'Level design']:
                                line('li',item)
                    itch_frame(tag, '1326223')
                    repo(tag, text, 'RayCasting2021')
                    end_post(doc)
                    
                    ###############################################################################
                    with tag('h2'): text('2021 - Pytracing Maze - my first game release')
                    with tag('p'):
                        text('''Simple ray tracing game in Python, based on my ray casting project.
                          As you may have guessed, things started to get a bit heavy for Python, 
                          so i had to resort to the Numba library, improving performance by 100x.''')
                    video_frame(tag, 'GNfGmNccGjE')
                    with tag('p'):
                        text('''This game uses a simple implementation of raytracing, where several rays are cast
                        for each pixel, this allows for real time shadows and reflections. Geometry is based on 
                        math, with cubes and spheres on a grid system.''')
                    itch_frame(tag, '1126594')
                    repo(tag, text, 'PytracingMaze')
                    end_post(doc)

                    ###############################################################################
                    with tag('h2'): text('2020 - Simple Raycasting with Matplotlib')
                    with tag('p'):
                        text('''Based on the Ray Casting technique, where the objects are drawn entirely out of vertical lines.
                          The size and position of the lines is defined by the distance between the player and the object. 
                          This is a very simple 3D maze game made from scratch in Python, using only three libraries: Numpy, Matplotlib,  Keyboard.''')    
                    video_frame(tag, '5xyeWBxmqzc')
                    repo(tag, text, 'RayCastingPythonMaze')
                    end_post(doc)

                with tag('aside'): pass

            with tag('footer'):
                social_media(tag)
                with tag('p'):
                     text('2023 FinFET Channel. All rights reserved.')
            
    with open("index.html", "w") as f:
        f.writelines(indent(doc.getvalue()))

def video_frame(tag, video):
    with tag('div', klass='videocontainer'):
        with tag('iframe', src='https://www.youtube.com/embed/'+video, klass='video', allowfullscreen=''):pass

def itch_frame(tag, game):
    with tag('div', klass='itchcontainer'):
        with tag('iframe', src="https://itch.io/embed/"+game+"?dark=true", klass='video'):pass

def game_frame(tag, text, game, aspect_ratio='5b4'):
    with tag('details'):
        with tag('summary'):
            text('Click HERE to reveal the game iframe and ')
            with tag('a', href="https://itch.io/embed-upload/"+game, target=game):
                text('HERE to actually load the game')
        with tag('div', klass='gamecontainer'+aspect_ratio):
            with tag('iframe', src='about:blank', name=game, klass='video', allowfullscreen=''):pass

def repo(tag, text, repository):
    with tag('p'):
        with tag('a', href='https://github.com/FinFetChannel/'+repository, target="_blank"):
            text('GitHub Repository')

def end_post(doc):
    doc.stag('br'); doc.stag('hr'); doc.stag('br')

def social_media(tag):
    with tag('a', href="https://www.reddit.com/r/FinFET/", target="_blank", klass="fab fa-reddit fa-2x"):pass
    with tag('a', href="https://finfetchannel.itch.io/", target="_blank", klass="fab fa-itch-io fa-2x"):pass
    with tag('a', href="https://www.youtube.com/@FinFET", target="_blank", klass="fab fa-youtube fa-2x"):pass
    with tag('a', href="https://github.com/FinFetChannel", target="_blank", klass="fab fa-github fa-2x"):pass
    with tag('a', href="mailto:finfetchannel@outlook.com", target="_blank", klass="fa fa-envelope fa-2x"):pass
    with tag('a', href="https://discord.com/invite/ZQmnZc4ARa", target="_blank", klass="fab fa-discord fa-2x"):pass
    
if __name__ == '__main__':
    main()