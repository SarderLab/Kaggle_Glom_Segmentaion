def converter(geojson_list, names, colorList=None, alpha=0.4):
    if colorList == None:
        colorList = ["rgb(0, 255, 128)", "rgb(0, 255, 255)", "rgb(255, 255, 0)", "rgb(255, 128, 0)", "rgb(0, 128, 255)",
                     "rgb(0, 0, 255)", "rgb(0, 102, 0)", "rgb(153, 0, 0)", "rgb(0, 153, 0)", "rgb(102, 0, 204)",
                     "rgb(76, 216, 23)", "rgb(102, 51, 0)", "rgb(128, 128, 128)", "rgb(0, 153, 153)", "rgb(0, 0, 0)"]
    data = []

    for n, child in enumerate([geojson_list]):
        dataDict = dict()
        name = names[n]
        #_ = os.system("printf 'Building JSON layer: [{}]\n'".format(name))
        element = []
        
        for i in child:
            eleDict = dict()
            eleDict["closed"] = True

            lineColor = colorList[n % len(colorList)]
            eleDict["lineColor"] = lineColor

            fillColor = lineColor[:3]+'a'+lineColor[3:-1] + f', {alpha})'
            eleDict["fillColor"] = fillColor

            eleDict["lineWidth"] = 2
            points = []
            #ver = i.find('Vertices')
            Verts = i["geometry"]["coordinates"][0]
            if len(Verts) <= 1:
                continue # skip if only 1 vertex points
            for j in Verts:
                eachPoint = []
                eachPoint.append(float(j[0]))
                eachPoint.append(float(j[1]))
                eachPoint.append(float(0))

                points.append(eachPoint)
            eleDict["points"] = points
            eleDict["type"] = "polyline"
            element.append(eleDict)
        dataDict["elements"] = element
        dataDict["name"] = name
        data.append(dataDict)

    return data
