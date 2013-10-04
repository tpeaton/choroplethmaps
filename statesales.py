### colorize_svg.py
# Code adapted from:
# http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/

import csv
from BeautifulSoup import BeautifulSoup
 
# Read in unemployment rates

def writeFile(filename, data):
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

stateSales = readCSVtoDict('slm2013salesbystate.csv')
# Load the SVG map
svg = open('Blank_US_Map.svg', 'r').read()
 
# Load into Beautiful Soup
soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])
 
# Find states
paths = soup.findAll('path')

# Map colors
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]
 
# State style
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
 
# Color the states based on sales
# SP- & MI- for Michigan

for p in paths:
        if p['id'] in stateSales:
            salesValue = stateSales[p['id']]

            if salesValue > 500000:
                color_class = 5
            elif salesValue > 200000:
                color_class = 4
            elif salesValue > 100000:
                color_class = 3
            elif salesValue > 50000:
                color_class = 2
            elif salesValue > 10000:
                color_class = 1
            else:
                color_class = 0

            color = colors[color_class]
            p['style'] = path_style + color


writeFile('test.svg', soup.prettify())
