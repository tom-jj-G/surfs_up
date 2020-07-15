#Depedencies import
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask

#Creating engine
engine = create_engine("sqlite:///Data/hawaii.sqlite")

#Reflect the database
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link
session = Session(engine)

#Create the Welcome Route


# # Create a Flask application called “app.”
# @app.route('/')
# def hello_world():
# 	return 'Hello world'