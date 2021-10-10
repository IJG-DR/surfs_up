############################################################
# MODULE 9.5.1 Set Up the Dabase and Flask
############################################################

# Import dependencies

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes.
Base = automap_base()
Base.prepare(engine, reflect=True)

# With the database reflected, save our references to each table. Create a variable for each of the 
# classes so that we can reference them later.
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create a session link from Python to the database.
session = Session(engine)

#Set up Flask
app = Flask(__name__)

############################################################
# MODULE 9.5.2 - Create the Welcome Route (NOTE: when creating routes, follow the naming 
# convention /api/vX.XX/ do indicate the app version is X.XX)
############################################################

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

############################################################
# MODULE 9.5.3 Precipitation Routes
############################################################

@app.route("/api/v1.0/precipitation")

def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

############################################################
# MODULE 9.5.4 Station Route
############################################################

@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

############################################################
# MODULE 9.5.5 Monthly Temperature Route
############################################################

@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


############################################################
# MODULE 9.5.6 Statistics Routes
############################################################

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Note that the imputs to the function are provided in the route address above
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # if no end date provided, return statistics for all dates after start date
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        # Use numpy unravel method to unravel the results into a one-dimensional
        # array, and convert that to a list.
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)