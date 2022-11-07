#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("Pilkarze.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print("Root element : %s" % collection.getAttribute("shelf"))

players = collection.getElementsByTagName("player")

for player in players:
   print("\n-------Player---------")
   if player.hasAttribute("name"):
      print("Name: %s" % player.getAttribute("Name"))

   position = player.getElementsByTagName('position')[0]
   print("Position: %s" % position.childNodes[0].data)
   birth = player.getElementsByTagName('birth')[0]
   print("Birth: %s" % birth.childNodes[0].data)
   rating = player.getElementsByTagName('rating')[0]
   print("Rating: %s" % rating.childNodes[0].data)
   foot = player.getElementsByTagName('foot')[0]
   print("Foot: %s" % foot.childNodes[0].data)
   description = player.getElementsByTagName('description')[0]
   print("Description: %s" % description.childNodes[0].data)