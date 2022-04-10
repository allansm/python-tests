import xml.etree.ElementTree as et
import os

data = "<user type='admin'>\n\t<id>1</id>\n\t<name>allansm</name>\n</user>"

xml = et.ElementTree(et.fromstring(data))
root = xml.getroot()

print("tag:"+root.tag)
print("attributes:", end='')
print(root.attrib)

for n in root:
    print(n.tag+":"+n.text)

f = open("user.xml", "wb")
xml.write(f)
f.close()

del xml
del root
del data

newxml = et.parse("user.xml")
newroot = newxml.getroot()

print("\n"+et.tostring(newroot, encoding='utf8', method='xml').decode())

os.remove("user.xml")
