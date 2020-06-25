import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# functions give carbon footprint number
# based on carbon footprint estimations

miles = None
tones = None
tone_miles = None
US_truck_carbon_factor = 161.8
grams_of_CO2 = US_truck_carbon_factor * tone_miles
metric_tons = 1000000 / grams_of_CO2


@app.route('/', methods=['GET'])
def home():
    return "<h1> API for canceling your carbon footprint </h1>"


@app.route('road_freight', methods=['GET'])
def caluate_road_freight():

    return


app.run()
