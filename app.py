from flask import Flask, render_template, json
from flask_pymongo import pymongo
import datetime
from datetime import date, datetime, timedelta
import json

CONNECTION_STRING = 'mongodb+srv://maliabarker:tpofbawf@cluster0.hllse.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_default_database()
events = db.events

app = Flask(__name__)

@app.route('/')
def index():
    # time = json.dumps(find_closest_date())
    event = find_closest_date()
    dt = event['date']
    time = dt.strftime("%b %d, %Y %X")
    jstime = dt.strftime("%m/%d/")
    json_str = json.dumps(jstime)
    print(f'jstime: {jstime}')
    print(f'json string: {json_str}')
    return render_template('index.html', time=time, event=event, json_str=json_str)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/events')
def events_index():
    return render_template('events.html')

def find_closest_date():
    # 'date' = events.find_one( { ''date'': { '$gte': 'date'time.now() } } )
    # 'date' = events.find({''date'': {'$gte': 'date'time.now()}})
    # for x in 'date':
    #     print(x)
    date = events.aggregate([
    {
        '$match': 
            {
                'date': 
                    {
                        '$gte': datetime.today().replace(day=1), 
                        '$lte': datetime.today() + timedelta(days=15)
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
    # {'$limit': 1}
    ])
    for x in date:
        return x


# print(find_closest_date())
time = find_closest_date()
print(time)

# def log_events():
#     data = [
#         { 'eventName': 'Mercury at Greatest Western Elongation', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 2, 16) },
#         { 'eventName': 'Mercury at Greatest Eastern Elongation', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 4, 29) },
#         { 'eventName': 'Mercury at Greatest Western Elongation', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 6, 16) },
#         { 'eventName': 'Saturn at Opposition', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 8, 14) },
#         { 'eventName': 'Mercury at Greatest Eastern Elongation', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 8, 27) },
#         { 'eventName': 'Neptune at Opposition', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 9, 16) },
#         { 'eventName': 'Jupiter at Opposition', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 9, 26) },
#         { 'eventName': 'Mercury at Greatest Western Elongation', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 10, 8) },
#         { 'eventName': 'Uranus at Opposition', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 11, 9) },
#         { 'eventName': 'Mars at Opposition', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 12, 8) },
#         { 'eventName': 'Mercury at Greatest Eastern Elongation', 'calendar': 'Planetary Event', 'color': 'orange', 'date': datetime(2022, 12, 21) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 2, 1) },
#         { 'eventName': 'Full Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 2, 16) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 3, 2) },
#         { 'eventName': 'Full Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 3, 18) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 4, 1) },
#         { 'eventName': 'Full Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 4, 16) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 4, 30) },
#         { 'eventName': 'Full Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 5, 16) },
#         { 'eventName': 'Total Lunar Eclipse', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 5, 16) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 5, 30) },
#         { 'eventName': 'Full Moon, Supermoon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 6, 14) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 6, 29) },
#         { 'eventName': 'Full Moon, Supermoon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 7, 13) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 7, 28) },
#         { 'eventName': 'Full Moon, Supermoon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 8, 12) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 8, 27) },
#         { 'eventName': 'Full Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 9, 10) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 9, 25) },
#         { 'eventName': 'Full Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 10, 9) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 10, 25) },
#         { 'eventName': 'Full Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 11, 8) },
#         { 'eventName': 'Total Lunar Eclipse', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 11, 8) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 11, 23) },
#         { 'eventName': 'Full Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 12, 8) },
#         { 'eventName': 'New Moon', 'calendar': 'Moon Event', 'color': 'blue', 'date': datetime(2022, 12, 23) },
#         { 'eventName': 'March Equinox', 'calendar': 'Solar Event', 'color': 'yellow', 'date': datetime(2022, 3, 20) },
#         { 'eventName': 'Partial Solar Eclipse', 'calendar': 'Solar Event', 'color': 'yellow', 'date': datetime(2022, 4, 30) },
#         { 'eventName': 'June Solstice', 'calendar': 'Solar Event', 'color': 'yellow', 'date': datetime(2022, 6, 21) },
#         { 'eventName': 'September Equinox', 'calendar': 'Solar Event', 'color': 'yellow', 'date': datetime(2022, 9, 23) },
#         { 'eventName': 'Partial Solar Eclipse', 'calendar': 'Solar Event', 'color': 'yellow', 'date': datetime(2022, 10, 25) },
#         { 'eventName': 'December Solstice', 'calendar': 'Solar Event', 'color': 'yellow', 'date': datetime(2022, 12, 21) },
#         { 'eventName': 'Lyrids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 4, 22) },
#         { 'eventName': 'Lyrids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 4, 23) },
#         { 'eventName': 'Eta Aquarids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 5, 6) },
#         { 'eventName': 'Eta Aquarids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 5, 7) },
#         { 'eventName': 'Delta Aquarids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 7, 28) },
#         { 'eventName': 'Delta Aquarids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 7, 29) },
#         { 'eventName': 'Perseids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 8, 12) },
#         { 'eventName': 'Perseids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 8, 13) },
#         { 'eventName': 'Draconids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 10, 7) },
#         { 'eventName': 'Orionids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 10, 21) },
#         { 'eventName': 'Orionids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 10, 22) },
#         { 'eventName': 'Taurids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 11, 4) },
#         { 'eventName': 'Taurids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 11, 5) },
#         { 'eventName': 'Leonids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 11, 17) },
#         { 'eventName': 'Leonids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 11, 18) },
#         { 'eventName': 'Geminids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 12, 13) },
#         { 'eventName': 'Geminids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 12, 14) },
#         { 'eventName': 'Ursids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 12, 21) },
#         { 'eventName': 'Ursids Meteor Shower', 'calendar': 'Meteors, Comets, & Asteroids', 'color': 'green', 'date': datetime(2022, 12, 22) },
#     ]
#     for event in data:
#         events.insert_one(event)
#         print(event)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
