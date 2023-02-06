from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

doc.asis('<!DOCTYPE html>')

with tag('html'):
    with tag('head'):
        doc.stag('link', rel='stylesheet', href='/style.css')

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
                    text('Here is a video of one of my first projects in Python, a simple raycasting game with matplotlib:')    
                with tag('div', klass='container'):
                    with tag('iframe', src="https://www.youtube.com/embed/5xyeWBxmqzc", klass='video'):
                        pass

                with tag('h2'):
                    text('Pytracing Maze - my first game release')
                with tag('p'):
                    text('A simple 3D maze game, where you have to find the exit to pass to the next level, but beware of enemies.  The final objective is to obtain the highest score, you lose points when you die and the difficulty increases with the score.')
                with tag('iframe', src="https://itch.io/embed/1126594?dark=true", width="552", height="167"):
                    pass

            with tag('aside'):
                pass

        with tag('footer'):
            with tag('p'):
                text('This is the footer?')
        
with open("index.html", "w") as f:
    f.writelines(indent(doc.getvalue()))
