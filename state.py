import numpy as py
from colorama import Fore, Back, Style, init
import copy


class State:
    def __init__(self,array1,array2,arlist3goal):
        self.boald=array1
        self.colorsquare=array2
        self.goalsquare=arlist3goal
        
    
        # result1=py.where(self.colorsquare=="A")
        # result2=py.where(self.colorsquare=="B")

    def chickGoal(self):
        return py.array_equal(self.colorsquare,self.goalsquare)

# //////////////////////////////////////////////////////

#    RIGHT 
    def checkmoveright(self, posA, posB,posC,array,exitA,exitB):
        if posA[0].size > 0 and posA[1].size > 0:
            rowA, colA = posA[0][0], posA[1][0]
            max_colA=colA-1
            while array[rowA][max_colA]!="■" and array[rowA][max_colA]!="B"  and array[rowA][max_colA]!="C" :
                max_colA-=1
            max_colA+=1 
            a=self.goalsquare[rowA][colA]  
            if a=="A" :
                array[rowA][colA]="□"
                array[rowA][max_colA] = "□"  
                self.goalsquare[rowA][colA] ="□"
            elif a=="B" :
                array[rowA][colA]="b"
                array[rowA][max_colA] = "A"  
            elif a=="C" :
                array[rowA][colA]="c"
                array[rowA][max_colA] = "A"                   
            else:    
                array[rowA][colA] = "□"
                array[rowA][max_colA] = "A"  
        # ////////////////
        if posB[0].size > 0 and posB[1].size > 0 :
            rowB, colB = posB[0][0], posB[1][0] 
            max_colB=colB-1
            while array[rowB][max_colB]!="■" and array[rowB][max_colB]!="A" and array[rowB][max_colB]!="C" :
                max_colB-=1 
            max_colB+=1 
            b=self.goalsquare[rowB][colB] 
            if b=="A" :
                array[rowB][colB]="a"
                array[rowB][max_colB] = "B" 
            elif b=="B" :
                array[rowB][colB]="□" 
                array[rowB][max_colB] = "□" 
                self.goalsquare[rowB][colB] ="□" 
            elif b=="C":
                array[rowB][colB]="c"
                array[rowB][max_colB] = "B"                   
            else:     
                array[rowB][colB] = "□"  
                array[rowB][max_colB] = "B"

                # //////////
        if posC[0].size > 0 and posC[1].size > 0 :
            rowC, colC = posC[0][0], posC[1][0] 
            max_colC=colC-1
            while array[rowC][max_colC]!="■" and array[rowC][max_colC]!="A" and array[rowC][max_colC]!="B" :
                max_colC-=1 
            max_colC+=1 
            c=self.goalsquare[rowC][colC] 
            if c=="A" :
                array[rowC][colC]="a"
                array[rowC][max_colC] = "C" 
            elif c=="B" :
                array[rowC][colC]="b" 
                array[rowC][max_colC] = "C" 
            elif c=="C" :
                array[rowC][colC]="□"
                array[rowC][max_colC] = "□"   
                self.goalsquare[rowC][colC] ="□"                 
            else:     
                array[rowC][colC] = "□"  
                array[rowC][max_colC] = "C"                 
        
        return array 

# /////////////////////
    def moveright(self, posA, posB,posC,array,exitA,exitB):
        array= self.checkmoveright( posA, posB,posC,array,exitA,exitB)
        s=State(self.boald,array,self.goalsquare)
        return s
    

# /////////////////////////////////////////////////////////////////

#   LEFT
    def checkmoveleft(self, posA, posB,posC,array,exitA,exitB):
        if posA[0].size > 0 and posA[1].size > 0 :
            rowA, colA = posA[0][0], posA[1][0]
            max_colA=colA
            while array[rowA][max_colA]!="■" and array[rowA][max_colA]!="B"  and array[rowA][max_colA]!="C" :
               max_colA+=1 
            max_colA-=1 
            a=self.goalsquare[rowA][colA]  
            if a=="A" :
                array[rowA][colA]="□"
                array[rowA][max_colA] = "□"
                self.goalsquare[rowA][colA] ="□"
            elif a=="B" :
                array[rowA][colA]="b" 
                array[rowA][max_colA] = "A"  
            elif a=="C" :
                array[rowA][colA]="c" 
                array[rowA][max_colA] = "A"     
            else:    
                array[rowA][colA] = "□"  
                array[rowA][max_colA] = "A" 
       
        #   ///////////////////// 
        if posB[0].size > 0 and posB[1].size > 0:
            rowB, colB = posB[0][0], posB[1][0]
            max_colB=colB
            while array[rowB][max_colB]!="■" and array[rowB][max_colB]!="A"  and array[rowB][max_colB]!="C"  :
                max_colB+=1   
            max_colB-=1
            b=self.goalsquare[rowB][colB] 
            if b=="A" :
                array[rowB][colB]="a"
                array[rowB][max_colB] = "B" 
            elif b=="B" :
                array[rowB][colB]="□"
                array[rowB][max_colB] = "□"
                self.goalsquare[rowB][colB] ="□" 
            elif b=="C" :
                array[rowB][colB]="c"
                array[rowB][max_colB] = "B"                     
            else:     
                array[rowB][colB] = "□"   
                array[rowB][max_colB] = "B" 

        #    /////////////
        if posC[0].size > 0 and posC[1].size > 0:
            rowC, colC = posC[0][0], posC[1][0]
            max_colC = colC
            while array[rowC][max_colC]!="■" and array[rowC][max_colC]!="A" and array[rowC][max_colC]!="B"  :
                max_colC+=1   
            max_colC-=1
            c=self.goalsquare[rowC][colC] 
            if c=="A" :
                array[rowC][colC]="a"
                array[rowC][max_colC] = "C" 
            elif c=="B" :
                array[rowC][colC]="b"
                array[rowC][max_colC] = "C"
            elif c=="C" :
                array[rowC][colC]="□"
                array[rowC][max_colC] = "□"   
                self.goalsquare[rowC][colC] ="□"                   
            else:     
                array[rowC][colC] = "□"   
                array[rowC][max_colC] = "C" 

        return array 

# 
    def moveleft(self, posA, posB,posC,array,exitA,exitB):
        array= self.checkmoveleft( posA, posB,posC,array,exitA,exitB)
        s=State(self.boald,array,self.goalsquare)
        return s

# ////////////////////////////////////////////////////////////
#   UP 
    def checkmoveup(self, posA, posB,posC,array,exitA,exitB):
        if posA[0].size > 0 and posA[1].size > 0:
            rowA, colA = posA[0][0], posA[1][0]
            max_rowA=rowA-1
            while array[max_rowA][colA]!="■" and array[max_rowA][colA]!="B" and array[max_rowA][colA]!="C" :
                max_rowA-=1
            max_rowA+=1
            a=self.goalsquare[rowA][colA]
            if a=="A" :
                array[rowA][colA]="□"
                array[max_rowA][colA] = "□"  
                self.goalsquare[rowA][colA] ="□"
            elif a=="B" :
                array[rowA][colA]="b"
                array[max_rowA][colA] = "A"
            elif a=="C" :
                array[rowA][colA]="c"
                array[max_rowA][colA] = "A"     
            else:
                array[rowA][colA] = "□"  
                array[max_rowA][colA] = "A" 

        # ///////////
        if posB[0].size > 0 and posB[1].size > 0:
            rowB, colB = posB[0][0], posB[1][0]
            max_rowB=rowB-1
            while array[max_rowB][colB]!="■" and array[max_rowB][colB]!="A" and array[max_rowB][colB]!="C":
               max_rowB-=1  
            max_rowB+=1  
            b=self.goalsquare[rowB][colB]                        
            if  b=="A" :
                array[rowB][colB]="a"
                array[max_rowB][colB] = "B"
            elif b=="B" :
                array[rowB][colB]="□"
                array[max_rowB][colB] = "□"
                self.goalsquare[rowB][colB] ="□"
            elif  b=="C" :
                array[rowB][colB]="c"
                array[max_rowB][colB] = "B"    
            else:          
                array[rowB][colB] = "□"
                array[max_rowB][colB] = "B" 

        # ///////////
        if posC[0].size > 0 and posC[1].size > 0:
            rowC, colC = posC[0][0], posC[1][0]
            max_rowC=rowC-1
            while array[max_rowC][colC]!="■" and array[max_rowC][colC]!="A" and array[max_rowC][colC]!="B":
               max_rowC-=1  
            max_rowC+=1  
            c=self.goalsquare[rowC][colC]                        
            if  c=="A" :
                array[rowC][colC]="a"
                array[max_rowC][colC] = "C"
            elif c=="B" :
                array[rowC][colC]="b"
                array[max_rowC][colC] = "C"
            elif c=="C" :
                array[rowC][colC]="□"
                array[max_rowC][colC] = "□"
                self.goalsquare[rowC][colC] ="□"      
            else:          
                array[rowC][colC] = "□"
                array[max_rowC][colC] = "C" 

        return array 


    def moveup(self, posA, posB,posC,array,exitA,exitB):
        array= self.checkmoveup( posA, posB,posC,array,exitA,exitB)
        s=State(self.boald,array,self.goalsquare)
        return s

    #  down
    def checkmovedown(self, posA, posB, posC,array, exitA, exitB):
        if  posA[0].size > 0 and posA[1].size > 0  :
            rowA, colA = posA[0][0], posA[1][0]
            max_rowA = rowA + 1
            while array[max_rowA][colA] != "■" and array[max_rowA][colA] != "B" and array[max_rowA][colA] != "C":
               max_rowA += 1
            max_rowA -= 1
            a = self.goalsquare[rowA][colA]
            if a == "A" :
                array[rowA][colA] = "□"  
                array[max_rowA][colA] = "□"
                self.goalsquare[rowA][colA] ="□"
            elif a == "B":
                array[rowA][colA] = "b"  
                array[max_rowA][colA] = "A"
            elif a == "C":
                array[rowA][colA] = "c" 
                array[max_rowA][colA] = "A"    
            else:
                array[rowA][colA] = "□"
                array[max_rowA][colA] = "A"

            #  ////////
        if posB[0].size > 0 and posB[1].size > 0:
            rowB, colB = posB[0][0], posB[1][0]
            max_rowB = rowB + 1
            while array[max_rowB][colB] != "■" and array[max_rowB][colB] != "A" and array[max_rowB][colB] != "C" :
                max_rowB += 1
            max_rowB -= 1
            b = self.goalsquare[rowB][colB]
            if b == "A":
                array[rowB][colB] = "a"
                array[max_rowB][colB] = "B"
            elif b == "B":
                array[rowB][colB] = "□"
                array[max_rowB][colB] = "□"
                self.goalsquare[rowB][colB] ="□"
            elif b == "C":
                array[rowB][colB] = "c"
                array[max_rowB][colB] = "B"    
            else:
                array[rowB][colB] = "□"
                array[max_rowB][colB] = "B"

            #  ////////
        if posC[0].size > 0 and posC[1].size > 0:
            rowC, colC = posC[0][0], posC[1][0]
            max_rowC = rowC + 1
            while array[max_rowC][colC] != "■" and array[max_rowC][colC] != "A" and array[max_rowC][colC] != "B":
                max_rowC += 1
            max_rowC -= 1
            c = self.goalsquare[rowC][colC]
            if c == "A" :
                array[rowC][colC] = "a"
                array[max_rowC][colC] = "C"
            elif c == "B" :
                array[rowC][colC] = "b"
                array[max_rowC][colC] = "C"
            elif c == "C":
                array[rowC][colC] = "□"
                array[max_rowC][colC] = "□" 
                self.goalsquare[rowC][colC] ="□"   
            else:
                array[rowC][colC] = "□"
                array[max_rowC][colC] = "C"

        return array


    def movedown(self, posA,posB,posC,array,exitA,exitB):
        array= self.checkmovedown( posA, posB,posC,array,exitA,exitB)
        s=State(self.boald,array,self.goalsquare)
        return s

#  ////******************** //////////////// 
#   MOVE FOR ANYWHERE
    def move(self,value):
        result1=py.where(self.colorsquare=="A")
        result2=py.where(self.colorsquare=="B")
        result3=py.where(self.colorsquare=="C")
        if result1:
            exitresultA=True
        else:
            exitresultA=False    
              
        if result2:
            exitresultB=True 
        else:
            exitresultB=False

        copy_array=copy.deepcopy(self.colorsquare)
        match value :
            case 1:
                s=self.moveright(result1,result2,result3,copy_array,exitresultA,exitresultB)
                return s
            
            case 2:
                s=self.moveleft(result1,result2,result3,copy_array,exitresultA,exitresultB)
                return s
            
            case 3:
                s=self.moveup(result1,result2,result3,copy_array,exitresultA,exitresultB)
                return s
            
            case 4:
                s=self.movedown(result1,result2,result3,copy_array,exitresultA,exitresultB)
                return s
              
            case _:
                print("anywhere")

     
    def nextState(self):
        sonstate=[]
        r=self.move(1) 
        sonstate.append(r)
        l=self.move(2)
        sonstate.append(l)
        u=self.move(3)
        sonstate.append(u)
        d=self.move(4)
        sonstate.append(d)
        return sonstate
    
    
        

#   JUST PRINT 
    def printS(self):
        for i in range(len(self.colorsquare)):
            for j in range(len(self.colorsquare[i])):
                if(self.colorsquare[i][j]!="□" or self.colorsquare[i][j]!="■"):
                    print(Fore.BLUE+self.colorsquare[i][j]+Fore.BLACK,end=" ")
                else:    
                    print(self.colorsquare[i][j],end=' ')  
            print("")      
        
        

    