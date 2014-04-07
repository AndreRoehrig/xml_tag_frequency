import xml.etree.ElementTree as ET
tree = ET.parse('generic.xml')
root = tree.getroot()

freqdict = {}

for i in root.iter(None):
    elem = i.tag
    print(elem)
    if elem in freqdict:
        freqdict[elem]+=1
    else:
        freqdict[elem]=0


print(freqdict)
