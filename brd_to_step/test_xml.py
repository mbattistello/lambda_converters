#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:10:00 2019

@author: marcobattistello
"""

from xml.dom import minidom

xml = "<eagle version=\"7\"><drawing><board><plain><wire x1=\"0\" y1=\"0\" x2=\"0\" y2=\"2\" width=\"0.254\" layer=\"20\"/><wire x1=\"0\" y1=\"2\" x2=\"1.5\" y2=\"2\" width=\"0.254\" layer=\"20\"/><wire x1=\"1.5\" y1=\"2\" x2=\"1\" y2=\"0\" width=\"0.254\" layer=\"20\"/><wire x1=\"1\" y1=\"0\" x2=\"0\" y2=\"0\" width=\"0.254\" layer=\"20\"/></plain></board></drawing></eagle>"
    
    
xmldoc = minidom.parseString( xml )

wires = xmldoc.getElementsByTagName('wire')

edges= []


for wire in wires:
    
    print( real( wire.attributes[ 'x1' ].value ) )
    print( float( wire.attributes[ 'y1' ].value ) )