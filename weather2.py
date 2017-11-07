import urllib2
import json

# PUT YOUR API KEY HERE
api_key = "18cf221b7bed1405"
city_value = "Issaquah"
# f = urllib2.urlopen('http://api.wunderground.com/api/18cf221b7bed1405/geolookup/conditions/q/IA/Issaquah.json')
f = urllib2.urlopen("http://api.wunderground.com/api/%s/geolookup/conditions/q/IA/%s.json" %api_key, %city_value) )

#url = "http://api.wunderground.com/api/%s/geolookup/conditions/q/IA/%s.json{}".format( first_id )
#
#A = json.load(urllib.urlopen(url))
#print A



json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

precipitation = parsed_json['current_observation']['precip_1hr_metric']

print "Current precipitation in %s is: %s" % (location, precipitation)
# rain = parsed_json['precip_1hr_metric']

#if  rain < 2:
#    print "Time to turn off IR Sensors"
#    # exit(0)
##    print "IR Sensors should be on."
#else:
#        print "your choice was: %r" % choice
#        dead("Error in value.")


f.close()
