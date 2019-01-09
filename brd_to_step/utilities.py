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
        
    def flip( self ):
        
        return Line( self.pt2, self.pt1 )
        
    def __str__( self ):
        return '(' + str( self.pt1.x ) + ',' + str( self.pt1.y ) + ') -> (' + str( self.pt2.x ) + ',' + str( self.pt2.y ) + ')'
        
        
        
class Outline():
    
    def __init__(self):
        None
   


def main():

    lines = []
    
    outlines = {}
    
    '''
    outlines = { 
                0: [ 1->2, 2->3, 3->4, 4->1 ],
                1 : [ 7->8, 8->9, 9->7 ]
                 }
    '''


    lines.append( Line( Point( 0,0 ), Point( 1,1 ) ) )  #0
    lines.append( Line( Point( 1,2 ), Point( 2,2 ) ) )  #2
    lines.append( Line( Point( 2,2 ), Point( 0,0 ) ) )  #3
    lines.append( Line( Point( 1,2 ), Point( 1,1 ) ) )  #1, flipped

    #loop thru items to find matches
    for current_index in range( 0, len( lines ) ):
        
        #init outlines
        if current_index == 0:
            outlines[ 0 ] = []
            
            outlines[ 0 ].append( lines[ current_index ] )
            
        
        print( str( current_index ) + ':' +  str( lines[ current_index ] ) )
        
        #init match to false
        match_found = False
        
        #loop thru items to find match to current item. Start at next item and go to end of list
        for match_index in range( (current_index+1), len( lines ) ):
            
            #check if match to end of current
            if lines[ current_index ].connects( lines[ match_index ] ):
                print( '\tfound match' )
                print( '\t' + str( match_index ) + ':' +  str( lines[ match_index ] ) )
                
                #swap pointsmatch_index = index
                
                move_to_index = (current_index+1)
            
                lines[match_index], lines[move_to_index] = lines[move_to_index], lines[match_index]
                
                match_found = True
                
                break
            
            #check if you flip line if it matches
            elif lines[ current_index ].connects( lines[ match_index ].flip() ):
                print( '\tfound match with flip' )
                print( '\t' + str( match_index ) + ':' +  str( lines[ match_index ] ) )
                
                #swap pointsmatch_index = index
                
                move_to_index = (current_index+1)
            
                lines[match_index], lines[move_to_index] = lines[move_to_index], lines[match_index].flip()  
                
                match_found = True
                
                break
            else:
                None
                
                
        #check if match found
        if match_found:
            
            #TODO - check if outline is closed
            
        else:
            #no match to add new outline
            max_outline = 0
            for outline_index in outlines:
                max_outline = max( max_outline, outline_index )
                
            outlines[ max_outline ] = []
            
            outlines[ max_outline ].append( lines[ current_index ] )    
            
                
                
    #print lines
    for line in lines:
        print( str( line ) )
            
        
        
        
        
if __name__ == "__main__":
    main()