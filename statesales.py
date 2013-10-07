# Code adapted from:
# http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/

import os
import csv
from BeautifulSoup import BeautifulSoup
from collections import OrderedDict
 

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


def colorStateMap(map, colorDict, data):

    soup = BeautifulSoup(map, selfClosingTags=['defs','sodipodi:namedview'])

    styleAttrib = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;' \
        'stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;' \
        'stroke-dasharray:none;stroke-linecap:butt;marker-start:none;' \
        'stroke-linejoin:bevel;fill:'

    paths = soup.findAll('path')
    for p in paths:
        state = p['id']
        if state in data:
            value = data[p['id']]

            for c, t in colorDict.iteritems():
                if value > t:
                    p['style'] = styleAttrib + c

        elif (state == 'MI-') or (state == 'SP-'):
            value = data['MI']

            for c, t in colorDict.iteritems():
                if value > t:
                    p['style'] = styleAttrib + c

    return soup


def writeFile(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)


def readFile(filename):
    with open(filename, 'r') as f:
        contents = f.read()

    return contents


iFile = os.path.dirname(__file__) + '\\data\\slm2013salesbystate.csv'
stateSales = readCSVtoDict(iFile)

mapFile = os.path.dirname(__file__) + '\\maps\\Blank_US_Map.svg'
blankMap = readFile(mapFile)

cDict = OrderedDict([('#B1FFC3B', 0), ('#87EA9D', 10000), ('#00AD3B', 50000),
         ('#007829', 100000), ('#004216', 200000), ('#001708', 500000)])

newMap = colorStateMap(blankMap, cDict, stateSales)
writeFile('test.svg', newMap.prettify())