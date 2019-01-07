from __future__ import print_function

import getopt
import os
import pdb
import sys

from xml.dom import minidom

from conversion_error import ConversionError

from OCC.gp import gp_Pnt, gp_Vec
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.STEPControl import STEPControl_Reader, STEPControl_Writer, STEPControl_AsIs
from OCC.IFSelect import IFSelect_RetDone
from OCC.Interface import Interface_Static_SetCVal


#simple build that draws board from 4 points
def build_test( path ):
    #points
    pt1 = gp_Pnt( 0, 0, 0 )
    pt2 = gp_Pnt( 0, 2, 0 )
    pt3 = gp_Pnt( 1.5, 2, 0 )
    pt4 = gp_Pnt( 1, 0, 0 )

    
    edge1 = BRepBuilderAPI_MakeEdge( pt1, pt2 )
    edge2 = BRepBuilderAPI_MakeEdge( pt2, pt3 )
    edge3 = BRepBuilderAPI_MakeEdge( pt3, pt4 )
    edge4 = BRepBuilderAPI_MakeEdge( pt4, pt1 )

    #make wire with 4 edges
    wire = BRepBuilderAPI_MakeWire( edge1.Edge(), edge2.Edge(), edge3.Edge(), edge4.Edge() )

    #alternate wire. create and then add in
    #makeWire = BRepBuilderAPI_MakeWire()
    #makeWire.add( wire )
    #wireProfile = makeWire.Wire()
    

    face = BRepBuilderAPI_MakeFace( wire.Wire() )

    #vector & height
    vector = gp_Vec( 0, 0, .1 )

    body = BRepPrimAPI_MakePrism( face.Face(), vector )

    # initialize the STEP exporter
    step_writer = STEPControl_Writer()
    Interface_Static_SetCVal("write.step.schema", "AP203")

    # transfer shapes and write file
    step_writer.Transfer( body.Shape(), STEPControl_AsIs)
    status = step_writer.Write( path )

    if status != IFSelect_RetDone:
        raise AssertionError("load failed")


def build( input, output ):
	#sample xml for testing
    xml = "<eagle version=\"7\"><drawing><board><plain><wire x1=\"0\" y1=\"0\" x2=\"0\" y2=\"2\" width=\"0.254\" layer=\"20\"/><wire x1=\"0\" y1=\"2\" x2=\"1.5\" y2=\"2\" width=\"0.254\" layer=\"20\"/><wire x1=\"1.5\" y1=\"2\" x2=\"1\" y2=\"0\" width=\"0.254\" layer=\"20\"/><wire x1=\"1\" y1=\"0\" x2=\"0\" y2=\"0\" width=\"0.254\" layer=\"20\"/></plain></board></drawing></eagle>"
    
    
    #xmldoc = minidom.parseString( xml )
    
    xmldoc = minidom.parse( input )

    wires = xmldoc.getElementsByTagName('wire')
    
    makeWire = BRepBuilderAPI_MakeWire()
    
    for wire in wires:
        
        if wire.attributes[ 'layer' ].value == '20':
            x1 = float( wire.attributes[ 'x1' ].value )
            y1 = float( wire.attributes[ 'y1' ].value )
            
            x2 = float( wire.attributes[ 'x2' ].value )
            y2 = float( wire.attributes[ 'y2' ].value )
            
            #print('Building edge from  {}, {} to {}, {}'.format( x1,y1,x2,y2))
            
            edge = BRepBuilderAPI_MakeEdge( gp_Pnt( x1, y1, 0.0 ), \
                                            gp_Pnt( x2, y2, 0.0 ) \
                                                      )
        
            makeWire.Add( edge.Edge() )
        
        
    face = BRepBuilderAPI_MakeFace( makeWire.Wire() )

    #vector & height
    vector = gp_Vec( 0, 0, .1 )

    body = BRepPrimAPI_MakePrism( face.Face(), vector )

    # initialize the STEP exporter
    step_writer = STEPControl_Writer()
    Interface_Static_SetCVal("write.step.schema", "AP203")

    # transfer shapes and write file
    step_writer.Transfer( body.Shape(), STEPControl_AsIs)
    status = step_writer.Write( output )

    if status != IFSelect_RetDone:
        raise AssertionError("load failed")
        
        
 
            
    
    
    

    




    


