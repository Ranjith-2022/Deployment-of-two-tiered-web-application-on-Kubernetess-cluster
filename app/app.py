from flask import Flask, render_template, request
from flask import jsonify
from flask import Flask, render_template, request
from pymysql import connections
import boto3
import os
import random
import argparse

app = Flask(__name__)

DBHOST = os.environ.get("DBHOST") or "localhost"
DBUSER = os.environ.get("DBUSER") or "root"
DBPWD = os.environ.get("DBPWD") or "passwors"
DATABASE = os.environ.get("DATABASE") or "employees"
COLOR_FROM_ENV = os.environ.get('APP_COLOR') or "lime"
DBPORT = int(os.environ.get("DBPORT"))
BGIMAGE = os.environ.get("BGIMAGE") or "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hcamag.com%2Fca%2Fspecialization%2Frecruitment%2Fwhere-are-the-best-places-to-work-in-toronto%2F449981&psig=AOvVaw1h3a-21n5jLMF4_e4FQgGK&ust=1712473430555000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMD3uuaCrYUDFQAAAAAdAAAAABAE"
OURNAMES = os.environ.get("OURNAMES")


# Create a connection to the MySQL database
db_conn = connections.Connection(
    host= DBHOST,
    port=DBPORT,
    user= DBUSER,
    password= DBPWD, 
    db= DATABASE
    
)
output = {}
table = 'employee';

# Define the supported color codes
color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#89CFF0",
    "blue2": "#30336b",
    "pink": "#f4c2c2",
    "darkblue": "#130f40",
    "lime": "#C1FF9C",
}

# Create a string of supported colors
SUPPORTED_COLORS = ",".join(color_codes.keys())

# Generate a random color
COLOR = random.choice(["red", "green", "blue", "blue2", "darkblue", "pink", "lime"])

@app.route("/")
def home():
    return render_template('addemp.html', background_image_url=get_background_image_url())

@app.route("/about")
def about():
    return render_template('about.html', background_image_url=get_background_image_url())

# Add other routes and functions as per your application requirements

if __name__ == '__main__':
    # Check for Command Line Parameters for color
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False)
    args = parser.parse_args()
    
    if args.color:
        print("Color from command line argument =" + args.color)
        COLOR = args.color
        if COLOR_FROM_ENV:
            print("A color was set through environment variable -" + COLOR_FROM_ENV + ". However, color from command line argument takes precendence.")
    elif COLOR_FROM_ENV:
        print("No Command line argument. Color from environment variable =" + COLOR_FROM_ENV)
        COLOR = COLOR_FROM_ENV
    else:
        print("No command line argument or environment variable. Picking a Random Color =" + COLOR)

    # Check if input color is a supported one
    if COLOR not in color_codes:
        print("Color not supported. Received '" + COLOR + "' expected one of " + SUPPORTED_COLORS)
        exit(1)

    app.run(host='0.0.0.0', port=81, debug=True)
