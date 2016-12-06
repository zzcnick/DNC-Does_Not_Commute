import json, urllib2, requests

# API Key: AIzaSyCnkOEu9Xyc2O3sNqzmTzCNub6e_kSoUeY

# ================================================
#                Google API Calls
# ================================================

# ================================================
#                   Geolocation
# ================================================
def call_gl():
    gl_url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCnkOEu9Xyc2O3sNqzmTzCNub6e_kSoUeY"
    gl_data = requests.post(gl_url)
    gl_dict = json.loads(gl_data.text)
    return gl_dict

def gl_location():
    gl_dict = call_gl()
    return [gl_dict['location']['lat'],
            gl_dict['location']['lng']]

# print gl_location()

# ================================================
#                   Geocoding
# ================================================
def call_gc_ll(lat, lng): 
    gc_url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=AIzaSyCnkOEu9Xyc2O3sNqzmTzCNub6e_kSoUeY"%(lat,lng)
    gc_data = urllib2.urlopen(gc_url)
    gc_get = gc_data.read()
    gc_dict = json.loads(gc_get)
    return gc_dict

def gc_address(lat, lng):
    gc_dict = call_gc_ll(lat, lng)
    return gc_dict['results'][0]['formatted_address']

# gl = gl_location()
# print gc_address(gl[0], gl[1])

# ================================================
#                Distance Matrix
# ================================================
def call_dm(lat1, lng1, lat2, lng2):
    add1_raw = gc_address(lat1,lng1)
    add1 = "+".join(add1_raw.split())
    add2_raw = gc_address(lat2,lng2)
    add2 = "+".join(add2_raw.split())
    dm_url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=%s&destinations=%s,NY&key=AIzaSyCnkOEu9Xyc2O3sNqzmTzCNub6e_kSoUeY"%(add1,add2)
    dm_data = urllib2.urlopen(dm_url)
    dm_get = dm_data.read()
    dm_dict = json.loads(dm_get)
    return dm_dict

def dm_eta(lat1, lng1, lat2, lng2):
    dm_dict = call_dm(lat1, lng1, lat2, lng2)
    return dm_dict['rows'][0]['elements'][0]['duration']['text']

def dm_dist(lat1, lng1, lat2, lng2):
    dm_dict = call_dm(lat1, lng1, lat2, lng2)
    return dm_dict['rows'][0]['elements'][0]['distance']['text']

# d1 = gl_location()
# d2 = ["40.7925920","-73.8465270"]
# print "Estimated Time: ", dm_eta(d1[0],d1[1],d2[0],d2[1])
# print "Distance: ", dm_dist(d1[0],d1[1],d2[0],d2[1])


