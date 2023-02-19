from yattag import Doc, indent

def main():
    doc, tag, text, line = Doc().ttl()

    doc.asis('<!DOCTYPE html>')

    with tag('html'):
        with tag('head'):
            doc.stag('link', rel='stylesheet', href='/style.css')
            doc.stag('link', rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css')

        with tag('body'):
            with tag('header'):
                doc.stag('img', src='finfet.png')
                # with tag('h1'):
                #     finfet_logo(tag, text)
                #     text(' channel')
                with tag('p'):
                    finfet_logo(tag, text)
                    text(' is a ')
                    with tag('a', href='https://www.youtube.com/@FinFET'):
                        text('channel on YouTube') 
                    text(' where I try stuff out with programming (especially Python) and tech in general.')
                social_media(tag)
            with tag('main'):
                with tag('aside'):pass

                with tag('article'):

                    ###############################################################################
                    with tag('h2'): text("2022/2023 - Super MaRayO Caster")
                    with tag('p'):
                        text('''A first-person perspective version of Super Mario Bros. using raycasting, made in Python with PyGame and PygBag.''')
                    video_frame(tag, 'NXhRi8UgzZk')
                    doc.stag('br')
                    game_frame(tag, text, '7339954')
                    itch_frame(tag, '1789891')
                    end_post(doc)

                    ###############################################################################
                    with tag('h2'): text("2022 - The LockPickin'joyer")
                    with tag('p'):
                        text('''A game inspired by the LockPickingLawyer, made in Python with PyGame and PygBag.''')
                    video_frame(tag, 'p-QJxbZmP3c')
                    doc.stag('br')
                    game_frame(tag, text, '6464625')
                    itch_frame(tag, '1474850')
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
                    end_post(doc)
                    
                    ###############################################################################
                    with tag('h2'): text('2021 - Pytracing Maze - my first game release')
                    with tag('p'):
                        text('''A simple 3D maze game, where you have to find the exit to pass to the next level, 
                        but beware of enemies.  The final objective is to obtain the highest score, you 
                        lose points when you die and the difficulty increases with the score.''')
                    video_frame(tag, 'GNfGmNccGjE')
                    with tag('p'):
                        text('''This game uses a simple implementation of raytracing, where several rays are cast
                        for each pixel, this allows for real time shadows and reflections. Geometry is based on 
                        math, with cubes and spheres on a grid system.''')
                    itch_frame(tag, '1126594')
                    with tag('p'):
                        text('''The game was made in Python with Pygame, for better performance the drawing is accelerated 
                        with Numba, leading to 20 times gain in fps.''')
                    end_post(doc)

                    ###############################################################################
                    with tag('h2'): text('2020 - Simple Raycasting with Matplotlib')
                    with tag('p'):
                        text('''One of my first projects in Python, a simple raycasting game with matplotlib, drawing walls as
                            vertical lines on a grid system.''')    
                    video_frame(tag, '5xyeWBxmqzc')
                    end_post(doc)

                with tag('aside'): pass

            with tag('footer'):
                social_media(tag)
                with tag('p'):
                     text('2023 FinFET Channel. All rights reserved.')
            
    with open("index.html", "w") as f:
        f.writelines(indent(doc.getvalue()))

def finfet_logo(tag, text):
    with tag('span', style='color: rgb(7, 97, 193)'):
        text('Fin')
    with tag('span', style='color: rgb(227, 52, 52)'):
        text('FET')

def video_frame(tag, video):
    with tag('div', klass='videocontainer'):
        with tag('iframe', src='https://www.youtube.com/embed/'+video, klass='video'):pass

def itch_frame(tag, game):
    with tag('div', klass='itchcontainer'):
        with tag('iframe', src="https://itch.io/embed/"+game+"?dark=true", klass='video'):pass

def game_frame(tag, text, game):
    with tag('a', href="https://itch.io/embed-upload/"+game, target=game):
        text('Click here to load the game')
    with tag('div', klass='gamecontainer'):
        with tag('iframe', src='about:blank', name=game, klass='video'):pass

def end_post(doc):
    doc.stag('br'); doc.stag('hr'); doc.stag('br')

def social_media(tag):
    with tag('a', href="https://www.reddit.com/r/FinFET/", klass="fab fa-reddit fa-2x"):pass
    with tag('a', href="https://finfetchannel.itch.io/", klass="fab fa-itch-io fa-2x"):pass
    with tag('a', href="https://www.youtube.com/@FinFET", klass="fab fa-youtube fa-2x"):pass
    with tag('a', href="https://github.com/FinFetChannel", klass="fab fa-github fa-2x"):pass
    with tag('a', href="mailto:finfetchannel@outlook.com", klass="fa fa-envelope fa-2x"):pass
    with tag('a', href="https://discord.com/invite/ZQmnZc4ARa", klass="fab fa-discord fa-2x"):pass
    
if __name__ == '__main__':
    main()