from xml.dom import minidom
x = minidom.parseString('<mytag><item>1</item></mytag>')
print x.toprettyxml()
#<?xml version="1.0" ?>
#<mytag>
#  <item>
#    1
#  </item>
#</mytag>
print x.getElementsByTagName('item')[0].childNodes[0].nodeValue #--> 1 
