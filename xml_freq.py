import os,sys
import xml.etree.ElementTree as ET
dirs = os.listdir("./")

freqdict = {}

for file in dirs:
	if file.endswith(".xml"):
		tree = ET.parse(file)
		root = tree.getroot()

		for i in root.iter(None):
	    		elem = i.tag
  	  		if elem in freqdict:
 		       		freqdict[elem]+=1
    			else:
        			freqdict[elem]=1

print(freqdict)
