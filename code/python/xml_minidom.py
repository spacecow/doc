from xml.dom import minidom
xml = """<xml>
  <li>List 1</li>
  <li>List 2</li>
</xml>"""
d = minidom.parseString(xml)
print [e.childNodes[0].nodeValue for e in d.getElementsByTagName("li")]
#--> [u'List 1', u'List 2']
