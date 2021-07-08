from main import Main

main = None


def setup():
    size(800,600)
    rectMode(CENTER)
    ellipseMode(CENTER)
    global main
    main = Main()


def draw():
    background(255,255,255)
    global main
    main.run()

    if keyPressed:
        if key == 'a':
            main.move_player('LEFT')
        elif key == 'd':
            main.move_player('RIGHT')
