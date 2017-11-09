#!/usr/bin/env python
import urllib2
import json

# PUT YOUR API KEY HERE
api_key = "18cf221b7bed1405"

# PUT YOUR STATE HERE
state = "WA"

# PUT YOUR CITY HERE
city_value = "Issaquah"

f = urllib2.urlopen("http://api.wunderground.com/api/%s/geolookup/conditions/q/%s/%s.json" % (api_key, state, city_value))

json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']

precipitation = parsed_json['current_observation']['precip_1hr_metric']

print "Current precipitation in %s is: %s" % (location, precipitation)

# isinstance is generally bad, like goto, to try to avoid using if at all possible.
#isinstance( precipitation, ( int, long ) )

# Ensure that the value of precipitation is float
float(precipitation)

if precipitation < 2.00:
   print ("Rain is above 2mm, turning off IR.")
else:
   print ("Rain is below 2mm, ensure IR is on.")

f.close()
