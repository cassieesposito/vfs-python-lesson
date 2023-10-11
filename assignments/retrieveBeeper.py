from stanfordkarel import *
from studentKarelModule import *

def main():
  
  return



if __name__ == "__main__":
  def randint(a,b):
    import random
    return random.randint(a,b)
  
  defineCallingProgram(__file__)
  run_karel_program(f"8x1b{randint(1,8)}")
