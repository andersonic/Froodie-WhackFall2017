from flask import Flask, render_template, request
import json
from time import gmtime, strftime

app = Flask(__name__)

filename = '/Users/junruanderson/PycharmProjects/whackf2017/data.json'

def start_json_file():
    f = open(filename, 'w')
    f.write('[]')
    f.close()

def read_database():
    f = open(filename, 'r')
    fileText = f.read()
    data = json.loads(fileText)
    f.close()
    return data

def add_location(currentLocation, numServings):
    data = {"location": currentLocation, "time": get_current_time(), "servings":numServings}
    oldData = read_database()
    oldData.append(data)
    with open(filename, 'w') as data_file:
        json.dump(oldData, data_file)

def get_current_time():
    return strftime("%H:%M", gmtime())

def get_location_list():
    data = read_database()
    locations = []
    for location in data:
        locations.append(location['location'])
    return locations

def decrement_servings(locationToDecrement):
    oldData = read_database()
    currentIndex = 0
    index = -1
    for datapoint in oldData:
        if datapoint['location'] == locationToDecrement:
            index = currentIndex
        currentIndex += 1
    if index != -1:
        oldData[index]['servings'] -= 1
    if oldData[index]['servings'] <= 0:
        del oldData[index]
    with open(filename, 'w') as data_file:
        json.dump(oldData, data_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getlocation')
def getlocation():
    return render_template('getlocation.html')

@app.route('/havefood')
def havefood():
    return render_template('havefood.html')

@app.route('/wantfood', methods=['POST'])
def wantfood(source = None):
    theirLocation = request.form['yourlocation'].replace(" ", "+")
    print theirLocation
    data = read_database()
    foodLocations = ""
    for food in data:
        location = food['location'].replace(" ", "+")
        foodLocations += location + '|'
    image = "https://maps.googleapis.com/maps/api/staticmap?center="\
            + theirLocation + "&zoom=13&size=600x300&maptype=roadmap"\
            + "&markers=color:red%7Clabel:F%7C"\
            + foodLocations\
            + "&key=AIzaSyDEcCaNT7FKxd2p7DO37MuzS1NLsI59H10"
    return render_template('wantfood.html', source = image)

@app.route('/foodsubmission', methods=['POST'])
def foodsubmission():
    location = request.form['location']
    servings = request.form['servings']
    add_location(location, servings)
    return render_template('responsereceived.html')

if __name__ == '__main__':
    start_json_file()
    app.run(host = "localhost", port = 5556, debug = True)