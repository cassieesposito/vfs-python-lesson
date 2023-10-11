########## Student Functions ###############

def go(steps):
  for i in range(steps):
    move()
  return


def turn(rotations):
  for i in range(rotations):
    turn_left()
  return


########### Weird stuff we gotta do to make a module using stanfordkarel################

def fileName(file):
    import os
    return os.path.basename(file.removesuffix('.py'))

def defineCallingProgram(file):
    global parent
    parent=__import__(fileName(file))
    return

def move():
    return parent.move()

def turn_left():
    return parent.turn_left()

