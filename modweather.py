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

float(precipitation)

if precipitation < 2.00:
   print ("Rain is above 2mm, turning off IR.")
else:
   print ("Rain is below 2mm, ensure IR is on.")

# import cookielib
# import urllib
# import urllib2
#
#
# # Store the cookies and create an opener that will hold them
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
#
# # Add our headers
# opener.addheaders = [('User-agent', 'RedditTesting')]
#
# # Install our opener (note that this changes the global opener to the one
# # we just made, but you can also just call opener.open() if you want)
# urllib2.install_opener(opener)
#
# # The action/ target from the form

# authentication_url = 'https://ssl.reddit.com/post/login'
# # Input parameters we are going to send
# payload = {
#   'op': 'login-main',
#   'user': '<username>',
#   'passwd': '<password>'
#   }

# # Use urllib to encode the payload
# data = urllib.urlencode(payload)

# # Build our Request object (supplying 'data' makes it a POST)
# req = urllib2.Request(authentication_url, data)

# # Make the request and read the response
# resp = urllib2.urlopen(req)
# contents = resp.read()



f.close()
