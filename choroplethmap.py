# Code adapted from:
# http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/

import os
import csv
from BeautifulSoup import BeautifulSoup
from collections import OrderedDict
 

class ColorStateMap():
    def __init__(self, colorDict, data, oFile):
        self.colorDict = colorDict
        self.data = data
        self.oFile = oFile

        mapFile = os.path.dirname(__file__) + '\\maps\\Blank_US_Map.svg'
        blankMap = self.readFile(mapFile)

        self.coloredMap = self.colorizeMap(blankMap, self.colorDict, self.data)

        self.writeFile(self.oFile, self.coloredMap)

    def readFile(self, filename):
        with open(filename, 'r') as f:
            contents = f.read()

        return contents


    def setStyleAttrib(self, cDict, p, value):
        styleAttrib = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;' \
            'stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;' \
            'stroke-dasharray:none;stroke-linecap:butt;marker-start:none;' \
            'stroke-linejoin:bevel;fill:'

        try:
            for c, t in cDict.iteritems():
                if value > t:
                    p['style'] = styleAttrib + c
            return p['style']
        except:
            pass


    def colorizeMap(self, map, colorDict, data):

        soup = BeautifulSoup(map, selfClosingTags=['defs',
            'sodipodi:namedview'])

        paths = soup.findAll('path')
        for path in paths:
            state = path['id']
            if state in data:
                self.setStyleAttrib(colorDict, path, data[path['id']])
            elif (state == 'MI-') or (state == 'SP-'):
                self.setStyleAttrib(colorDict, path, data['MI'])

        return soup.prettify()


    def writeFile(self, filename, data):
        with open(filename, 'wb') as f:
            f.write(data)


def readCSVtoDict(filename):
    dataDict = {}
    reader = csv.reader(open(filename))
    for row in reader:
        try:
            dKey = row[0]
            dVal = float(row[1].translate(None, ",$"))
            dataDict[dKey] = dVal
        except:
            pass

    return dataDict


<<<<<<< HEAD
iFile = os.path.dirname(__file__) + '\\data\\alvarez2013.csv'
=======
iFile = os.path.dirname(__file__) + '\\data\\salesbystate.csv'
>>>>>>> a64166f7d72dc18f44f94f4eb732e25c10ec4f7f
stateSales = readCSVtoDict(iFile)

cDict = OrderedDict([('#B1FFC3B', 0), ('#87EA9D', 10000), ('#00AD3B', 50000),
         ('#007829', 100000), ('#004216', 200000), ('#001708', 500000)])

NewMap = ColorStateMap(cDict, stateSales, 'coloredmap.svg')
