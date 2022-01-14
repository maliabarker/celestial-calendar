from flask import Flask, render_template, json, request
from flask_pymongo import pymongo
import datetime
from datetime import date, datetime, timedelta
import json
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
import pytz

CONNECTION_STRING = 'mongodb+srv://maliabarker:tpofbawf@cluster0.hllse.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(CONNECTION_STRING)

geolocator = Nominatim(user_agent="geoapiExercises")
obj = TimezoneFinder()

db = client.get_default_database()
events = db.events
descriptions = db.descriptions

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    event = find_closest_date()
    events_desc = find_three_events()
    dt = event['date']
    time = dt.strftime("%b %d, %Y %X")
    jstime = dt.strftime("%m/%d/")
    json_str = json.dumps(jstime)
    
    city = "San Francisco"
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone = pytz.timezone(result)
    d_aware = timezone.localize(dt)
    event_time = d_aware.strftime("%B %d, %Y %Z")
    converted_result = result.replace("_", " ")
    print(converted_result)
    json_tz_str = json.dumps(result)

    if request.method == 'POST':
        city = request.form.get('city')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        timezone = pytz.timezone(result)
        d_aware = timezone.localize(dt)
        event_time = d_aware.strftime("%B %d, %Y %Z")
        converted_result = result.replace("_", " ")
        json_tz_str = json.dumps(result)

    return render_template('index.html', time=time, event=event, json_str=json_str, events_desc=events_desc, city=city, lat=location.latitude, lon=location.longitude, tz=converted_result, event_time=event_time, json_tz_str=json_tz_str)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')





# -----------------------------------------MONTHLY EVENT ROUTES------------------------------------------------------------

@app.route('/jan_events')
def jan_events_index():
    jan_events = find_jan_events()
    return render_template('jan_events.html', jan_events=jan_events)

@app.route('/feb_events')
def feb_events_index():
    feb_events = find_feb_events()
    return render_template('feb_events.html', feb_events=feb_events)

@app.route('/mar_events')
def mar_events_index():
    mar_events = find_mar_events()
    return render_template('mar_events.html', mar_events=mar_events)

@app.route('/apr_events')
def apr_events_index():
    apr_events = find_apr_events()
    return render_template('apr_events.html', apr_events=apr_events)

@app.route('/may_events')
def may_events_index():
    may_events = find_may_events()
    return render_template('may_events.html', may_events=may_events)

@app.route('/jun_events')
def jun_events_index():
    jun_events = find_jun_events()
    return render_template('jun_events.html', jun_events=jun_events)

@app.route('/jul_events')
def jul_events_index():
    jul_events = find_jul_events()
    return render_template('jul_events.html', jul_events=jul_events)

@app.route('/aug_events')
def aug_events_index():
    aug_events = find_aug_events()
    return render_template('aug_events.html', aug_events=aug_events)

@app.route('/sep_events')
def sep_events_index():
    sep_events = find_sep_events()
    return render_template('sep_events.html', sep_events=sep_events)

@app.route('/oct_events')
def oct_events_index():
    oct_events = find_oct_events()
    return render_template('oct_events.html', oct_events=oct_events)

@app.route('/nov_events')
def nov_events_index():
    nov_events = find_nov_events()
    return render_template('nov_events.html', nov_events=nov_events)

@app.route('/dec_events')
def dec_events_index():
    dec_events = find_dec_events()
    return render_template('dec_events.html', dec_events=dec_events)





# -------------------------------------HELPER FUNCTIONS------------------------------------------------------------


def find_closest_date():
    date = events.aggregate([
    {
        '$match': 
            {
                'date': 
                    {
                        '$gte': datetime.today(), 
                        '$lte': datetime.today() + timedelta(days=30)
                    }
            }
    },
    {
        '$project':
            {
                'eventName': 1,
                'calendar': 1,
                'color': 1,
                'date': 1,
                'date_dist': {'$abs': [{'$subtract': ["$date", datetime.now()]}]}}
    },
    {
        '$sort': {'date_dist': 1}
    },
    {'$limit': 1}
    ])
    for x in date:
        return x

def find_three_events():
    dates = descriptions.aggregate([
    {
        '$match': 
            {
                'date': 
                    {
                        '$gte': datetime.today(), 
                        '$lte': datetime.today() + timedelta(days=50)
                    }
            }
    },
    {
        '$project':
            {
                'eventName': 1,
                'description': 1,
                'img': 1,
                'date': 1,
                'dt': 1,
                'date_dist': {'$abs': [{'$subtract': ["$date", datetime.now()]}]}}
    },
    {
        '$sort': {'date_dist': 1}
    },
    {'$limit': 3}
    ])
    return dates

def find_jan_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 1, 1), '$lte': datetime(2022, 1, 31)}}).sort('date', pymongo.ASCENDING)
    return data

def find_feb_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 2, 1), '$lte': datetime(2022, 2, 28)}}).sort('date', pymongo.ASCENDING)
    return data

def find_mar_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 3, 1), '$lte': datetime(2022, 3, 31)}}).sort('date', pymongo.ASCENDING)
    return data

def find_apr_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 4, 1), '$lte': datetime(2022, 4, 30)}}).sort('date', pymongo.ASCENDING)
    return data

def find_may_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 5, 1), '$lte': datetime(2022, 5, 31)}}).sort('date', pymongo.ASCENDING)
    return data

def find_jun_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 6, 1), '$lte': datetime(2022, 6, 30)}}).sort('date', pymongo.ASCENDING)
    return data

def find_jul_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 7, 1), '$lte': datetime(2022, 7, 31)}}).sort('date', pymongo.ASCENDING)
    return data

def find_aug_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 8, 1), '$lte': datetime(2022, 8, 31)}}).sort('date', pymongo.ASCENDING)
    return data

def find_sep_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 9, 1), '$lte': datetime(2022, 9, 30)}}).sort('date', pymongo.ASCENDING)
    return data

def find_oct_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 10, 1), '$lte': datetime(2022, 10, 31)}}).sort('date', pymongo.ASCENDING)
    return data

def find_nov_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 11, 1), '$lte': datetime(2022, 11, 30)}}).sort('date', pymongo.ASCENDING)
    return data

def find_dec_events():
    data = descriptions.find({'date': {'$gte': datetime(2022, 12, 1), '$lte': datetime(2022, 12, 31)}}).sort('date', pymongo.ASCENDING)
    return data


if __name__ == '__main__':
    app.run(debug=True, port=5002)
