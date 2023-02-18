from yattag import Doc, indent

doc, tag, text, line = Doc().ttl()

doc.asis('<!DOCTYPE html>')

with tag('html'):
    with tag('head'):
        doc.stag('link', rel='stylesheet', href='/style.css')
        doc.stag('link', rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css')

    with tag('body'):
        with tag('header'):
            with tag('h1'):
                with tag('span', style='color: rgb(7, 97, 193)'):
                    text('Fin')
                with tag('span', style='color: rgb(227, 52, 52)'):
                    text('FET')
                text(' channel')
            with tag('p'):
                with tag('span', style='color: rgb(7, 97, 193)'):
                    text('Fin')
                with tag('span', style='color: rgb(227, 52, 52)'):
                    text('FET')
                text(' is a ')
                with tag('a', href='https://www.youtube.com/@FinFET'):
                    text('channel on YouTube') 
                text(' where I try stuff out with programming (especially Python) and tech in general.')
        
        with tag('main'):
            with tag('aside'):
                pass

            with tag('article'):
                with tag('h2'):
                    text('Simple Raycasting with Matplotlib')
                with tag('p'):
                    text('''One of my first projects in Python, a simple raycasting game with matplotlib, drawing walls as
                         vertical lines on a grid system.''')    
                with tag('div', klass='videocontainer'):
                    with tag('iframe', src="https://www.youtube.com/embed/5xyeWBxmqzc", klass='video'):
                        pass
                doc.stag('br'); doc.stag('hr'); doc.stag('br')
                
                with tag('h2'):
                    text('Pytracing Maze - my first game release')
                with tag('p'):
                    text('''A simple 3D maze game, where you have to find the exit to pass to the next level, 
                    but beware of enemies.  The final objective is to obtain the highest score, you 
                    lose points when you die and the difficulty increases with the score.''')
                with tag('div', klass='videocontainer'):
                    with tag('iframe', src="https://www.youtube.com/embed/GNfGmNccGjE", klass='video'):
                        pass
                with tag('p'):
                    text('''This game uses a simple implementation of raytracing, where several rays are cast
                      for each pixel, this allows for real time shadows and reflections. Geometry is based on 
                      math, with cubes and spheres on a grid system.''')
                with tag('div', klass='itchcontainer'):
                    with tag('iframe', src="https://itch.io/embed/1126594?dark=true", klass='video'):
                        pass
                with tag('p'):
                    text('''The game was made in Python with Pygame, for better performance the drawing is accelerated 
                    with Numba, leading to 20 times gain in fps.''')
                doc.stag('br'); doc.stag('hr'); doc.stag('br')

                with tag('h2'):
                    text('Dead And!')
                with tag('p'):
                    text('''A raycasting game made in Python, now with textures and sprites.''')
                with tag('div', klass='videocontainer'):
                    with tag('iframe', src="https://www.youtube.com/embed/FLc6vUwyTdM", klass='video'):
                        pass
                with tag('p'):
                    text('''Themes developed include:''')
                    with tag('ul'):
                        line('li','Floorcasting')
                        line('li','Raycasting with textures and fake shadows')
                        line('li','Sprites')
                        line('li','Enemies AI')
                        line('li','Sounds')
                        line('li','GUI and menus')
                        line('li','Level design')
                        line('li','FPS mod')
                
                with tag('div', klass='itchcontainer'):
                    with tag('iframe', src="https://itch.io/embed/1326223?dark=true", klass='video'):
                        pass
                doc.stag('br'); doc.stag('hr'); doc.stag('br')
                
                with tag('h2'):
                    text("The LockPickin'joyer")
                with tag('p'):
                    text('''A game inspired by the LockPickingLawyer, made in Python with PyGame and PygBag.''')
                with tag('a', href="https://itch.io/embed-upload/6464625", target="LockPickingLawyer"):
                    text('Click Here to load the game')
                with tag('div', klass='gamecontainer'):
                    with tag('iframe', src="about:blank", name="LockPickingLawyer", klass='video'):pass
                doc.stag('br'); doc.stag('hr'); doc.stag('br')
                
                with tag('h2'):
                    text("Super MaRayO Caster")
                with tag('p'):
                    text('''A first-person perspective version of Super Mario Bros. using raycasting, made in Python with PyGame and PygBag.''')
                with tag('a', href="https://itch.io/embed-upload/7339954", target="SuperMarayo"):
                    text('Click Here to load the game')
                with tag('div', klass='gamecontainer'):
                    with tag('iframe', src='about:blank', name="SuperMarayo", klass='video'):pass
                doc.stag('br'); doc.stag('hr'); doc.stag('br')
            with tag('aside'):
                pass

        with tag('footer'):
            with tag('a', href="https://finfetchannel.itch.io/", klass="fab fa-itch-io fa-3x"):pass
            with tag('a', href="https://www.youtube.com/@FinFET", klass="fab fa-youtube fa-3x"):pass
            with tag('a', href="https://github.com/FinFetChannel", klass="fab fa-github fa-3x"):pass
            with tag('a', href="https://discord.com/invite/ZQmnZc4ARa", klass="fab fa-discord fa-3x"):pass
        
with open("index.html", "w") as f:
    f.writelines(indent(doc.getvalue()))
