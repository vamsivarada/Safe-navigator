from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

import requests
import pandas as pd
def azureapi(sourcelat,sourcelong,destinationlat,destinationlong,departat):
    response = requests.get("https://atlas.microsoft.com/route/directions/json?subscription-key=I3_Xc6FKJFTakajfVotqIQ4bqVa53Tw9XYyuMjfF_Iw&api-version=1.0&query={},{}:{},{}&maxAlternatives=1&instructionsType=text&traffic=true&departAt={}".format(sourcelat,sourcelong,destinationlat,destinationlong,departat))
    response = response.json()
    import pandas as pd
    df = pd.DataFrame(response)
    newdict = {}
    finaldict = {}
    for i in range(0,len(df['routes'])):
        count = 0
        for j in range(0,len(df['routes'][i]['guidance']['instructions'])):
            message = df['routes'][i]['guidance']['instructions'][j]['message']
            if ('left' in message) or ('right' in message):
                count = count + 1
        newdict[i] = count
    for key, value in newdict.items():
        if min(newdict.values()) == value:
            traveltime  = df['routes'][key]['legs'][0]['summary']['travelTimeInSeconds']
            coordinates = df['routes'][key]['legs'][0]['points']
            finaldict['traveltime'] = traveltime
            finaldict['coordinates'] = str(coordinates).replace('\'', '\"')
            return finaldict

@app.route('/postjson', methods = ['GET'])
def hello():
    content = request.get_json()
    output = azureapi(request.args.get('sourceLat'), request.args.get('sourceLong'), request.args.get('destLat'), request.args.get('destLong'), "2019-12-09T12:12:57")
    # output = azureapi("52.50931","13.42936","52.50274","13.43872","2019-12-09T12:12:57")
    print(output)
    return output

app.run(host='0.0.0.0', port= 8090)