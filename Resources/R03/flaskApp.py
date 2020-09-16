from flask import Flask
from flask import request
from flask import jsonify
import pymongo  # package for working with MongoDB

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the base route'


@app.route('/test/')
def test():

    name = request.args.get("name",None)

    print(f"name: {name}")

    if name == None:
        return jsonify({"Numrow":0,"Error":True,"Message":"No name passed to test route!!"})

    return jsonify(list(request.args.keys()))

@app.route('/country/<string:name>')
def country(name):
    global db
    countries = db["countries"]

    lines = []
    # points = {'lat':[],'lon':[],'latlon':[]}

    for obj in countries.find({"properties.ADMIN" : name}, { "geometry.coordinates": 1, "_id": 0 }):
        lines.append(obj)

    print(lines)
    
    # for group in lines[0]['geometry']['coordinates']:
    #     #print(group)
    #     for line in group:
    #         #print(line)
    #         for point in line:
    #             points['lat'].append(point[1])
    #             points['lon'].append(point[0])
    #             points['latlon'].append(point)

    return jsonify(lines)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)