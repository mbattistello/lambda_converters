from __future__ import print_function

import getopt
import os
import pdb
import sys

from conversion_error import ConversionError

from OCC.gp import gp_Pnt, gp_Vec
from OCC.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.STEPControl import STEPControl_Reader, STEPControl_Writer, STEPControl_AsIs
from OCC.IFSelect import IFSelect_RetDone
from OCC.Interface import Interface_Static_SetCVal



def build( path ):
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


    


