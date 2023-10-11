from stanfordkarel import *

def main():
  
  turn_left()
  
  for i in range(5):
    for i in range(4):
      while front_is_clear():
        move()
      turn_right()
  return
  


def turn_right():
  for i in range(3):
    turn_left()
  
  # for i in range(20):
  #   for i in range(4):
  #     for i in range(7):
  #       move()
  #     turn_left()


  # for i in range(20): 
  #   move()
  #   turn_left()
  #   move()
  #   turn_left()
  #   move()
  #   turn_left()
  #   move()
  #   turn_left()

if __name__ == "__main__":
  run_karel_program("")
