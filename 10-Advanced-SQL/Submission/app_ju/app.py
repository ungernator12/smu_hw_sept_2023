# Import the dependencies.
from flask import Flask, jsonify
import pandas as pd
from sqlHelperJU import SQLHelper

#################################################
# Database Setup
#################################################
sqlHelperJU = SQLHelper()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"<h1>Welcome to the Hawaii Climate API!</h1><br/>"
        f"<h3>Available Routes:</h3><br/>"
        f"<a href='/api/v1.0/precipitation' target='_blank'>/api/v1.0/precipitation</a><br>"
        f"<a href='/api/v1.0/stations' target='_blank'>/api/v1.0/stations</a><br>"
        f"<a href='/api/v1.0/tobs' target='_blank'>/api/v1.0/tobs</a><br>"
        f"<a href='/api/v1.0/2017-08-23' target='_blank'>/api/v1.0/2017-08-23</a><br>"
        f"<a href='/api/v1.0/2017-08-01/2017-08-23' target='_blank'>/api/v1.0/2017-08-01/2017-08-23</a><br>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    df = sqlHelperJU.get_precipitation_data()
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    df = sqlHelperJU.get_station_data
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/tobs")
def tobs():
    df = sqlHelperJU.get_tobs_data
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/<start>")
def date_start(start):
    df = sqlHelperJU.get_tobs_by_start_date(start)
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def date_range(start, end):
    df = sqlHelperJU.get_tobs_by_date_range(start, end)
    data = df.to_dict(orient="records")
    return jsonify(data)
#################################################
# Execute the app
#################################################
if __name__ == "__main__":
    app.run(debug=True)

