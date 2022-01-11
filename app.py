from flask import Flask, render_template, json
from flask_pymongo import pymongo
import datetime
from datetime import date, datetime, timedelta
import json

CONNECTION_STRING = 'mongodb+srv://maliabarker:tpofbawf@cluster0.hllse.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_default_database()
events = db.events
descriptions = db.descriptions

app = Flask(__name__)

@app.route('/')
def index():
    event = find_closest_date()
    events_desc = find_three_events()
    print(f'events_desc: {events_desc}')
    dt = event['date']
    time = dt.strftime("%b %d, %Y %X")
    jstime = dt.strftime("%m/%d/")
    json_str = json.dumps(jstime)
    return render_template('index.html', time=time, event=event, json_str=json_str, events_desc=events_desc)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')




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
    # print(dates)
    # for x in dates:
    #     print(x)
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

# events = find_three_events()

# def log_desc():
#     data = [
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 18:35 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 1, 2) },
#         { 'eventName': 'Full Moon', 'description': ' The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 23:51 UTC. This full moon was known by early Native American tribes as the Wolf Moon because this was the time of year when hungry wolf packs howled outside their camps. This moon has also been know as the Old Moon and the Moon After Yule.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 1, 17) },
#         { 'eventName': 'Mercury at Greatest Eastern Elongation', 'description': 'The planet Mercury reaches greatest eastern elongation of 19.2 degrees from the Sun. This is the best time to view Mercury since it will be at its highest point above the horizon in the evening sky. Look for the planet low in the western sky just after sunset.', 'img': '/static/images/mercury.png', 'date': datetime(2022, 1, 7) },
#         { 'eventName': 'Quadrantids Meteor Shower', 'description': 'The Quadrantids is an above average shower, with up to 40 meteors per hour at its peak. It is thought to be produced by dust grains left behind by an extinct comet known as 2003 EH1, which was discovered in 2003. The shower runs annually from January 1-5. It peaks this year on the night of the 3rd and morning of the 4th. The thin, crescent moon will set early in the evening leaving dark skies for what should be an excellent show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Bootes, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 1, 3) },
#         { 'eventName': 'Quadrantids Meteor Shower', 'description': 'The Quadrantids is an above average shower, with up to 40 meteors per hour at its peak. It is thought to be produced by dust grains left behind by an extinct comet known as 2003 EH1, which was discovered in 2003. The shower runs annually from January 1-5. It peaks this year on the night of the 3rd and morning of the 4th. The thin, crescent moon will set early in the evening leaving dark skies for what should be an excellent show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Bootes, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 1, 4) },

#         { 'eventName': 'Mercury at Greatest Western Elongation', 'description': 'The planet Mercury reaches greatest western elongation of 26.3 degrees from the Sun. This is the best time to view Mercury since it will be at its highest point above the horizon in the morning sky. Look for the planet low in the eastern sky just before sunrise.', 'img': '/static/images/mercury.png', 'date': datetime(2022, 2, 16) },
#         { 'eventName': 'Mercury at Greatest Eastern Elongation', 'description': 'The planet Mercury reaches greatest eastern elongation of 20.6 degrees from the Sun. This is the best time to view Mercury since it will be at its highest point above the horizon in the evening sky. Look for the planet low in the western sky just after sunset.', 'img': '/static/images/mercury.png', 'date': datetime(2022, 4, 29) },
#         { 'eventName': 'Mercury at Greatest Western Elongation', 'description': 'The planet Mercury reaches greatest western elongation of 23.2 degrees from the Sun. This is the best time to view Mercury since it will be at its highest point above the horizon in the morning sky. Look for the planet low in the eastern sky just before sunrise.', 'img': '/static/images/mercury.png', 'date': datetime(2022, 6, 16) },
#         { 'eventName': 'Saturn at Opposition', 'description': "The ringed planet will be at its closest approach to Earth and its face will be fully illuminated by the Sun. It will be brighter than any other time of the year and will be visible all night long. This is the best time to view and photograph Saturn and its moons. A medium-sized or larger telescope will allow you to see Saturn's rings and a few of its brightest moons.", 'img': '/static/images/saturn.png', 'date': datetime(2022, 8, 14) },
#         { 'eventName': 'Mercury at Greatest Eastern Elongation', 'description': 'The planet Mercury reaches greatest eastern elongation of 27.3 degrees from the Sun. This is the best time to view Mercury since it will be at its highest point above the horizon in the evening sky. Look for the planet low in the western sky just after sunset.', 'img': '/static/images/mercury.png', 'date': datetime(2022, 8, 27) },
#         { 'eventName': 'Neptune at Opposition', 'description': 'The blue giant planet will be at its closest approach to Earth and its face will be fully illuminated by the Sun. It will be brighter than any other time of the year and will be visible all night long. This is the best time to view and photograph Neptune. Due to its extreme distance from Earth, it will only appear as a tiny blue dot in all but the most powerful telescopes.', 'img': '/static/images/neptune.png', 'date': datetime(2022, 9, 16) },
#         { 'eventName': 'Jupiter at Opposition', 'description': "The giant planet will be at its closest approach to Earth and its face will be fully illuminated by the Sun. It will be brighter than any other time of the year and will be visible all night long. This is the best time to view and photograph Jupiter and its moons. A medium-sized telescope should be able to show you some of the details in Jupiter's cloud bands. A good pair of binoculars should allow you to see Jupiter's four largest moons, appearing as bright dots on either side of the planet.", 'img': '/static/images/jupiter.png', 'date': datetime(2022, 9, 26) },
#         { 'eventName': 'Mercury at Greatest Western Elongation', 'description': 'The planet Mercury reaches greatest western elongation of 18 degrees from the Sun. This is the best time to view Mercury since it will be at its highest point above the horizon in the morning sky. Look for the planet low in the eastern sky just before sunrise.', 'img': '/static/images/mercury.png', 'date': datetime(2022, 10, 8) },
#         { 'eventName': 'Uranus at Opposition', 'description': 'The blue-green planet will be at its closest approach to Earth and its face will be fully illuminated by the Sun. It will be brighter than any other time of the year and will be visible all night long. This is the best time to view Uranus. Due to its distance, it will only appear as a tiny blue-green dot in all but the most powerful telescopes.', 'img': '/static/images/uranus.png', 'date': datetime(2022, 11, 9) },
#         { 'eventName': 'Mars at Opposition', 'description': "The red planet will be at its closest approach to Earth and its face will be fully illuminated by the Sun. It will be brighter than any other time of the year and will be visible all night long. This is the best time to view and photograph Mars. A medium-sized telescope will allow you to see some of the dark details on the planet's orange surface.", 'img': '/static/images/mars.png', 'date': datetime(2022, 12, 8) },
#         { 'eventName': 'Mercury at Greatest Eastern Elongation', 'description': 'The planet Mercury reaches greatest eastern elongation of 20.1 degrees from the Sun. This is the best time to view Mercury since it will be at its highest point above the horizon in the evening sky. Look for the planet low in the western sky just after sunset.', 'img': '/static/images/mercury.png', 'date': datetime(2022, 12, 21) },

#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 05:48 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 2, 1) },
#         { 'eventName': 'Full Moon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 16:59 UTC. This full moon was known by early Native American tribes as the Snow Moon because the heaviest snows usually fell during this time of the year. Since hunting is difficult, this moon has also been known by some tribes as the Hunger Moon, since the harsh weather made hunting difficult.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 2, 16) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 17:38 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 3, 2) },
#         { 'eventName': 'Full Moon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 07:20 UTC. This full moon was known by early Native American tribes as the Worm Moon because this was the time of year when the ground would begin to soften and the earthworms would reappear. This moon has also been known as the Crow Moon, the Crust Moon, the Sap Moon, and the Lenten Moon.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 3, 18) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 06:27 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 4, 1) },
#         { 'eventName': 'Full Moon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 18:57 UTC. This full moon was known by early Native American tribes as the Pink Moon because it marked the appearance of the moss pink, or wild ground phlox, which is one of the first spring flowers. This moon has also been known as the Sprouting Grass Moon, the Growing Moon, and the Egg Moon. Many coastal tribes called it the Fish Moon because this was the time that the shad swam upstream to spawn.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 4, 16) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 20:30 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 4, 30) },
#         { 'eventName': 'Full Moon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 04:15 UTC. This full moon was known by early Native American tribes as the Flower Moon because this was the time of year when spring flowers appeared in abundance. This moon has also been known as the Corn Planting Moon and the Milk Moon.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 5, 16) },
#         { 'eventName': 'Total Lunar Eclipse', 'description': "A total lunar eclipse occurs when the Moon passes completely through the Earth's dark shadow, or umbra. During this type of eclipse, the Moon will gradually get darker and then take on a rusty or blood red color. The eclipse will be visible throughout all of North America, Greenland, the Atlantic Ocean, and parts of western Europe and western Africa.", 'img': '/static/images/lunareclipse.png', 'date': datetime(2022, 5, 16) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 11:32 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 5, 30) },
#         { 'eventName': 'Full Moon, Supermoon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 11:52 UTC. This full moon was known by early Native American tribes as the Strawberry Moon because it signaled the time of year to gather ripening fruit. It also coincides with the peak of the strawberry harvesting season. This moon has also been known as the Rose Moon and the Honey Moon. This is also the first of three supermoons for 2022. The Moon will be near its closest approach to the Earth and may look slightly larger and brighter than usual.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 6, 14) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 02:53 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 6, 29) },
#         { 'eventName': 'Full Moon, Supermoon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 18:38 UTC. This full moon was known by early Native American tribes as the Buck Moon because the male buck deer would begin to grow their new antlers at this time of year. This moon has also been known as the Thunder Moon and the Hay Moon. This is also the second of three supermoons for 2022. The Moon will be near its closest approach to the Earth and may look slightly larger and brighter than usual.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 7, 13) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 17:55 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 7, 28) },
#         { 'eventName': 'Full Moon, Supermoon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 01:36 UTC. This full moon was known by early Native American tribes as the Sturgeon Moon because the large sturgeon fish of the Great Lakes and other major lakes were more easily caught at this time of year. This moon has also been known as the Green Corn Moon and the Grain Moon. This is also the last of three supermoons for 2022. The Moon will be near its closest approach to the Earth and may look slightly larger and brighter than usual.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 8, 12) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 08:17 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 8, 27) },
#         { 'eventName': 'Full Moon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 09:58 UTC. This full moon was known by early Native American tribes as the Corn Moon because the corn is harvested around this time of year. This moon is also known as the Harvest Moon. The Harvest Moon is the full moon that occurs closest to the September equinox each year.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 9, 10) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 21:55 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 9, 25) },
#         { 'eventName': 'Full Moon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 20:55 UTC. This full moon was known by early Native American tribes as the Hunters Moon because at this time of year the leaves are falling and the game is fat and ready to hunt. This moon has also been known as the Travel Moon and the Blood Moon.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 10, 9) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 10:49 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 10, 25) },
#         { 'eventName': 'Full Moon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 11:03 UTC. This full moon was known by early Native American tribes as the Beaver Moon because this was the time of year to set the beaver traps before the swamps and rivers froze. It has also been known as the Frosty Moon and the Dark Moon.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 11, 8) },
#         { 'eventName': 'Total Lunar Eclipse', 'description': "A total lunar eclipse occurs when the Moon passes completely through the Earth's dark shadow, or umbra. During this type of eclipse, the Moon will gradually get darker and then take on a rusty or blood red color. The eclipse will be visible throughout eastern Russia, Japan, Australia, the Pacific Ocean, and parts of western and central North America.", 'img': '/static/images/lunareclipse.png', 'date': datetime(2022, 11, 8) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 22:58 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 11, 23) },
#         { 'eventName': 'Full Moon', 'description': 'The Moon will be located on the opposite side of the Earth as the Sun and its face will be will be fully illuminated. This phase occurs at 04:09 UTC. This full moon was known by early Native American tribes as the Cold Moon because this is the time of year when the cold winter air settles in and the nights become long and dark. This moon has also been known as the Long Nights Moon and the Moon Before Yule.', 'img': '/static/images/fullmoon.png', 'date': datetime(2022, 12, 8) },
#         { 'eventName': 'New Moon', 'description': 'The Moon will located on the same side of the Earth as the Sun and will not be visible in the night sky. This phase occurs at 10:17 UTC. This is the best time of the month to observe faint objects such as galaxies and star clusters because there is no moonlight to interfere.', 'img': '/static/images/newmoon.png', 'date': datetime(2022, 12, 23) },

#         { 'eventName': 'March Equinox', 'description': 'The March equinox occurs at 15:24 UTC. The Sun will shine directly on the equator and there will be nearly equal amounts of day and night throughout the world. This is also the first day of spring (vernal equinox) in the Northern Hemisphere and the first day of fall (autumnal equinox) in the Southern Hemisphere.', 'img': '/static/images/sun.png', 'date': datetime(2022, 3, 20) },
#         { 'eventName': 'Partial Solar Eclipse', 'description': "A partial solar eclipse occurs when the Moon covers only a part of the Sun, sometimes resembling a bite taken out of a cookie. A partial solar eclipse can only be safely observed with a special solar filter or by looking at the Sun's reflection. This partial eclipse will be visible throughout most of the southeast Pacific Ocean and southern South America. It will be best seen from Argentina with 53% coverage.", 'img': '/static/images/solareclipse.png', 'date': datetime(2022, 4, 30) },
#         { 'eventName': 'June Solstice', 'description': 'The June solstice occurs at 09:05 UTC. The North Pole of the earth will be tilted toward the Sun, which will have reached its northernmost position in the sky and will be directly over the Tropic of Cancer at 23.44 degrees north latitude. This is the first day of summer (summer solstice) in the Northern Hemisphere and the first day of winter (winter solstice) in the Southern Hemisphere.', 'img': '/static/images/sun.png', 'date': datetime(2022, 6, 21) },
#         { 'eventName': 'September Equinox', 'description': 'The September equinox occurs at 00:55 UTC. The Sun will shine directly on the equator and there will be nearly equal amounts of day and night throughout the world. This is also the first day of fall (autumnal equinox) in the Northern Hemisphere and the first day of spring (vernal equinox) in the Southern Hemisphere.', 'img': '/static/images/sun.png', 'date': datetime(2022, 9, 23) },
#         { 'eventName': 'Partial Solar Eclipse', 'description': "A partial solar eclipse occurs when the Moon covers only a part of the Sun, sometimes resembling a bite taken out of a cookie. A partial solar eclipse can only be safely observed with a special solar filter or by looking at the Sun's reflection. This partial eclipse will be best seen in parts of western Russia and Kazakhstan. It will be best seen from central Russia with over 80% coverage.", 'img': '/static/images/solareclipse.png', 'date': datetime(2022, 10, 25) },
#         { 'eventName': 'December Solstice', 'description': 'The December solstice occurs at 21:40 UTC. The South Pole of the earth will be tilted toward the Sun, which will have reached its southernmost position in the sky and will be directly over the Tropic of Capricorn at 23.44 degrees south latitude. This is the first day of winter (winter solstice) in the Northern Hemisphere and the first day of summer (summer solstice) in the Southern Hemisphere.', 'img': '/static/images/sun.png', 'date': datetime(2022, 12, 21) },

#         { 'eventName': 'Lyrids Meteor Shower', 'description': 'The Lyrids is an average shower, usually producing about 20 meteors per hour at its peak. It is produced by dust particles left behind by comet C/1861 G1 Thatcher, which was discovered in 1861. The shower runs annually from April 16-25. It peaks this year on the night of the night of the 22nd and morning of the 23rd. These meteors can sometimes produce bright dust trails that last for several seconds. The waning gibbous moon may block some of the fainter meteors this year, but there is still potential for a good show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Lyra, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 4, 22) },
#         { 'eventName': 'Lyrids Meteor Shower', 'description': 'The Lyrids is an average shower, usually producing about 20 meteors per hour at its peak. It is produced by dust particles left behind by comet C/1861 G1 Thatcher, which was discovered in 1861. The shower runs annually from April 16-25. It peaks this year on the night of the night of the 22nd and morning of the 23rd. These meteors can sometimes produce bright dust trails that last for several seconds. The waning gibbous moon may block some of the fainter meteors this year, but there is still potential for a good show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Lyra, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 4, 23) },
#         { 'eventName': 'Eta Aquarids Meteor Shower', 'description': 'The Eta Aquarids is an above average shower, capable of producing up to 60 meteors per hour at its peak. Most of the activity is seen in the Southern Hemisphere. In the Northern Hemisphere, the rate can reach about 30 meteors per hour. It is produced by dust particles left behind by comet Halley, which has been observed since ancient times. The shower runs annually from April 19 to May 28. It peaks this year on the night of May 6 and the morning of the May 7. The waxing crescent moon will set early in the evening, leaving dark skies for what should be an excellent show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Aquarius, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 5, 6) },
#         { 'eventName': 'Eta Aquarids Meteor Shower', 'description': 'The Eta Aquarids is an above average shower, capable of producing up to 60 meteors per hour at its peak. Most of the activity is seen in the Southern Hemisphere. In the Northern Hemisphere, the rate can reach about 30 meteors per hour. It is produced by dust particles left behind by comet Halley, which has been observed since ancient times. The shower runs annually from April 19 to May 28. It peaks this year on the night of May 6 and the morning of the May 7. The waxing crescent moon will set early in the evening, leaving dark skies for what should be an excellent show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Aquarius, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 5, 7) },
#         { 'eventName': 'Delta Aquarids Meteor Shower', 'description': 'The Delta Aquarids is an average shower that can produce up to 20 meteors per hour at its peak. It is produced by debris left behind by comets Marsden and Kracht. The shower runs annually from July 12 to August 23. It peaks this year on the night of July 28 and morning of July 29. This is a great year for this shower because the new moon means dark skies for what should be an excellent. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Aquarius, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 7, 28) },
#         { 'eventName': 'Delta Aquarids Meteor Shower', 'description': 'The Delta Aquarids is an average shower that can produce up to 20 meteors per hour at its peak. It is produced by debris left behind by comets Marsden and Kracht. The shower runs annually from July 12 to August 23. It peaks this year on the night of July 28 and morning of July 29. This is a great year for this shower because the new moon means dark skies for what should be an excellent. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Aquarius, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 7, 29) },
#         { 'eventName': 'Perseids Meteor Shower', 'description': 'The Perseids is one of the best meteor showers to observe, producing up to 60 meteors per hour at its peak. It is produced by comet Swift-Tuttle, which was discovered in 1862. The Perseids are famous for producing a large number of bright meteors. The shower runs annually from July 17 to August 24. It peaks this year on the night of August 12 and the morning of August 13. Unfortunately the nearly full moon this year will block out all but the brightest meteors. But the Perseids are so bright and numerous that it could still be a decent show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Perseus, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 8, 12) },
#         { 'eventName': 'Perseids Meteor Shower', 'description': 'The Perseids is one of the best meteor showers to observe, producing up to 60 meteors per hour at its peak. It is produced by comet Swift-Tuttle, which was discovered in 1862. The Perseids are famous for producing a large number of bright meteors. The shower runs annually from July 17 to August 24. It peaks this year on the night of August 12 and the morning of August 13. Unfortunately the nearly full moon this year will block out all but the brightest meteors. But the Perseids are so bright and numerous that it could still be a decent show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Perseus, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 8, 13) },
#         { 'eventName': 'Draconids Meteor Shower', 'description': 'The Draconids is a minor meteor shower producing only about 10 meteors per hour. It is produced by dust grains left behind by comet 21P Giacobini-Zinner, which was first discovered in 1900. The Draconids is an unusual shower in that the best viewing is in the early evening instead of early morning like most other showers. The shower runs annually from October 6-10 and peaks this year on the the night of the 7th. The first quarter moon will block out all but the brightest meteors this year. If you are patient, you may still be able to catch a few good ones. Best viewing will be in the early evening from a dark location far away from city lights. Meteors will radiate from the constellation Draco, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 10, 7) },
#         { 'eventName': 'Orionids Meteor Shower', 'description': 'The Orionids is an average shower producing up to 20 meteors per hour at its peak. It is produced by dust grains left behind by comet Halley, which has been known and observed since ancient times. The shower runs annually from October 2 to November 7. It peaks this year on the night of October 21 and the morning of October 22. The thin, crescent moon will leave mostly dark skies for what should be a good show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Orion, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 10, 21) },
#         { 'eventName': 'Orionids Meteor Shower', 'description': 'The Orionids is an average shower producing up to 20 meteors per hour at its peak. It is produced by dust grains left behind by comet Halley, which has been known and observed since ancient times. The shower runs annually from October 2 to November 7. It peaks this year on the night of October 21 and the morning of October 22. The thin, crescent moon will leave mostly dark skies for what should be a good show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Orion, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 10, 22) },
#         { 'eventName': 'Taurids Meteor Shower', 'description': 'The Taurids is a long-running minor meteor shower producing only about 5-10 meteors per hour. It is unusual in that it consists of two separate streams. The first is produced by dust grains left behind by Asteroid 2004 TG10. The second stream is produced by debris left behind by Comet 2P Encke. The shower runs annually from September 7 to December 10. It peaks this year on the the night of November 4. This year the nearly full moon will block out all but the brightest meteors. But if you are patient, you may still be able to catch a few good ones. Best viewing will be just after midnight from a dark location far away from city lights. Meteors will radiate from the constellation Taurus, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 11, 4) },
#         { 'eventName': 'Taurids Meteor Shower', 'description': 'The Taurids is a long-running minor meteor shower producing only about 5-10 meteors per hour. It is unusual in that it consists of two separate streams. The first is produced by dust grains left behind by Asteroid 2004 TG10. The second stream is produced by debris left behind by Comet 2P Encke. The shower runs annually from September 7 to December 10. It peaks this year on the the night of November 4. This year the nearly full moon will block out all but the brightest meteors. But if you are patient, you may still be able to catch a few good ones. Best viewing will be just after midnight from a dark location far away from city lights. Meteors will radiate from the constellation Taurus, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 11, 5) },
#         { 'eventName': 'Leonids Meteor Shower', 'description': 'The Leonids is an average shower, producing an average of up to 15 meteors per hour at its peak. This shower is unique in that it has a cyclonic peak about every 33 years where hundreds of meteors per hour can be seen. That last of these occurred in 2001. The Leonids is produced by dust grains left behind by comet Tempel-Tuttle, which was discovered in 1865. The shower runs annually from November 6-30. It peaks this year on the night of the 17th and morning of the 18th. The second quarter moon will block many of the fainter meteors this year. But the Leonids can be unpredictable so there is still potential for a good show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Leo, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 11, 17) },
#         { 'eventName': 'Leonids Meteor Shower', 'description': 'The Leonids is an average shower, producing an average of up to 15 meteors per hour at its peak. This shower is unique in that it has a cyclonic peak about every 33 years where hundreds of meteors per hour can be seen. That last of these occurred in 2001. The Leonids is produced by dust grains left behind by comet Tempel-Tuttle, which was discovered in 1865. The shower runs annually from November 6-30. It peaks this year on the night of the 17th and morning of the 18th. The second quarter moon will block many of the fainter meteors this year. But the Leonids can be unpredictable so there is still potential for a good show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Leo, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 11, 18) },
#         { 'eventName': 'Geminids Meteor Shower', 'description': 'The Geminids is the king of the meteor showers. It is considered by many to be the best shower in the heavens, producing up to 120 multicolored meteors per hour at its peak. It is produced by debris left behind by an asteroid known as 3200 Phaethon, which was discovered in 1982. The shower runs annually from December 7-17. It peaks this year on the night of the 13th and morning of the 14th. The waning gibbous moon will block many of the fainter meteors this year. But the Geminids are so numerous and bright that this should still be a good show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Gemini, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 12, 13) },
#         { 'eventName': 'Geminids Meteor Shower', 'description': 'The Geminids is the king of the meteor showers. It is considered by many to be the best shower in the heavens, producing up to 120 multicolored meteors per hour at its peak. It is produced by debris left behind by an asteroid known as 3200 Phaethon, which was discovered in 1982. The shower runs annually from December 7-17. It peaks this year on the night of the 13th and morning of the 14th. The waning gibbous moon will block many of the fainter meteors this year. But the Geminids are so numerous and bright that this should still be a good show. Best viewing will be from a dark location after midnight. Meteors will radiate from the constellation Gemini, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 12, 14) },
#         { 'eventName': 'Ursids Meteor Shower', 'description': 'The Ursids is a minor meteor shower producing about 5-10 meteors per hour. It is produced by dust grains left behind by comet Tuttle, which was first discovered in 1790. The shower runs annually from December 17-25. It peaks this year on the the night of the 21st and morning of the 22nd. This year, the nearly new moon will leave dark skies for what should be a really good show. Best viewing will be just after midnight from a dark location far away from city lights. Meteors will radiate from the constellation Ursa Minor, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 12, 21) },
#         { 'eventName': 'Ursids Meteor Shower', 'description': 'The Ursids is a minor meteor shower producing about 5-10 meteors per hour. It is produced by dust grains left behind by comet Tuttle, which was first discovered in 1790. The shower runs annually from December 17-25. It peaks this year on the the night of the 21st and morning of the 22nd. This year, the nearly new moon will leave dark skies for what should be a really good show. Best viewing will be just after midnight from a dark location far away from city lights. Meteors will radiate from the constellation Ursa Minor, but can appear anywhere in the sky.', 'img': '/static/images/meteor3.png', 'date': datetime(2022, 12, 22) },
#     ]
#     for event in data:
#         descriptions.insert_one(event)
#         print(event)
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
