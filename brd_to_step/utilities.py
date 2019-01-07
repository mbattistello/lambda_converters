#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 09:31:40 2019

@author: marcobattistello
"""

       
def sortWireList( list ):
    oldList = list
    newList = []
    
    #get wire line 
    
    
  
class Point():

    def __init__( self, x, y ):
        self.x = x
        self.y = y
        
        
    
class Line():
    
    def __init__(self, pt1, pt2 ):
        self.pt1 = pt1
        self.pt2 = pt2
        
        
    def connects( self, otherTwoPoints ):
        
        if self.pt2.x == otherTwoPoints.pt1.x and self.pt2.y == otherTwoPoints.pt1.y:
            return True
        else:
            return False
        
        
        
class Outline():
    
    def __init__(self):
        None
   


def main():

    lines = []

    lines.append( Line( Point( 0,0 ), Point( 1,1 ) ) )
    lines.append( Line( Point( 1,1 ), Point( 1,2 ) ) )  
    lines.append( Line( Point( 1,2 ), Point( 2,2 ) ) )  
    lines.append( Line( Point( 2,2 ), Point( 0,0 ) ) ) 

    sortedLines = []    
    
    for line1 in lines:
        
        
        for line2 in lines:
            
            if line1 == line2:
                print( "same line" )
                
            elif line1.connects( line2 ):
                print( "connects" )
                
            else:
                print( "no match" )
                
                
        print( "\n" )
        
        
        
        
if __name__ == "__main__":
    main()