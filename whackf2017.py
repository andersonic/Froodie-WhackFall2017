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
    print fileText
    data = json.loads(fileText)
    f.close()
    return data

def add_location(currentLocation):
    data = {"location": currentLocation, "time": get_current_time()}
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/havefood')
def havefood():
    return render_template('havefood.html')

@app.route('/wantfood')
def wantfood(source = None):
    data = read_database()
    foodLocations = ""
    for food in data:
        foodLocations += food['location'] + '|'
    image = "https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap"\
            + "&markers=color:yellow%7Clabel:F%7C"\
            + foodLocations\
            + "&key=AIzaSyDEcCaNT7FKxd2p7DO37MuzS1NLsI59H10"
    return render_template('wantfood.html', source = image)

@app.route('/foodsubmission', methods=['POST'])
def foodsubmission():
    location = request.form['location']
    add_location(location)
    return render_template('responsereceived.html')

if __name__ == '__main__':
    start_json_file()
    app.run(host = "localhost", port = 5556, debug = True)
