from stanfordkarel import *

def main():
  go(2)
  turn(3)
  move()
  turn_left()
  move()
  pick_beeper()
  turn(2)
  move()
  turn(3)
  move()
  put_beeper()
  turn(2)
  move()
  turn_left()
  return


def turn(rotations):
  for i in range(rotations):
    turn_left()
  return


def go(steps):
  for i in range(steps):
    move()
  return


if __name__ == "__main__":
  run_karel_program("collect_newspaper_karel")
