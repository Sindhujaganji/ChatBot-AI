
import testing as testpy
test=testpy.Testing()
from flask import Flask, render_template, request

# import json to load JSON data to a python dictionary
import json


# urllib.request to make a request to api
import urllib.request


app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])

def weather():
	query=""
	if request.method == 'POST':
		query = request.form['query']

	answer = test.response(query)
	print(answer)
	if answer=="gotoFunction":
	# your API key will come here
		api = "ba4df9cbf56f2797572f63a74fc41f2a"
		city=""
		flag = 0
		for i in query:
			if i=="*":
				flag=flag+1
			if flag==1:
				city=city+i
			elif flag==2:
				break
		city=city[1:]
		from geopy.geocoders import Nominatim
		geolocator = Nominatim(user_agent='myapplication')
		location = geolocator.geocode(city)
		#print(location.raw)
		print("Lattitude: "+location.raw["lat"])
		print("Longitude: "+location.raw["lon"])
		lat = location.raw["lat"]
		lon = location.raw["lon"]
		# source contain json data from api
		#https://api.openweathermap.org/data/2.5/weather?q={city name},{state code}&appid={API key}
		source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat=' + lat +'&lon='+lon+ '&appid=' + api).read()

		# converting JSON data to a dictionary
		list_of_data = json.loads(source)

		# data for variable list_of_data
		answer = "Current temperature in "+city+" is "+ str(list_of_data['main']['temp']) + ' in kelvin / '+str(round((list_of_data['main']['temp']-273),3))+" Celcious / "+str(round((1.8*(list_of_data['main']['temp']-273)+32),3))+ " Fahrenheit"
		# data = {
		# 	"query":query,
		# 	"city":city,
		# 	"country_code": str(list_of_data['sys']['country']),
		# 	"coordinate": str(list_of_data['coord']['lon']) + ' '
		# 				+ str(list_of_data['coord']['lat']),
		# 	"temp": str(list_of_data['main']['temp']) + 'k',
		# 	"temp_cel":str(round((list_of_data['main']['temp']-273),3)),
		# 	"pressure": str(list_of_data['main']['pressure']),
		# 	"humidity": str(list_of_data['main']['humidity']),
		# }
		data = {
			"query":query,
			"ans":answer
			
		}
		print(data)
		return render_template("home.html", data = data)
	else:
		data = {
			"query":query,
			"ans":answer
		}
		print(data)
		return render_template("home.html", data = data)

if __name__ == '__main__':
	app.run(debug = True)
