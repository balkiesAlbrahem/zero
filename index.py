import numpy as py 
from colorama import Fore, Back, Style, init
from state import *
from game import *
from tkinter import *
from tkinter import simpledialog, messagebox

class player:
   def __init__(self,array1,array2,arraygoal):
    #   self.master=master
      self.arr1=array1
      self.arr2=array2
      self.arrgoal=array3goul
      self.initstate=State(array1,array2,array3goul)
    
  
   def move_player(self):
      new_state=self.initstate
      new_state.printS()
      while (not new_state.chickGoal()):
            # 1 right
            # 2 left
            # 3 uo
            # 4 down
            inp=input("enter 1 or 2 or 3 or 4: ")
            inp=int(inp)
            new_state=new_state.move(inp)
            new_state.printS()
            print("*"*20)
      if(new_state.chickGoal):
          print("SUCCESS")
            # messagebox.showinfo("تهانينا!", "Success")
            

# start application
if __name__ == "__main__":
    gamee=game(1)
    array1=gamee.funarr1()
    array2=gamee.funarr2()
    array3goul=gamee.funarr3()
    print("/"*30)
    player1=player(array1,array2,array3goul)
    player1.move_player()
    # root.mainloop()

           







