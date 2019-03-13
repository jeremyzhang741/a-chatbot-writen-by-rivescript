# -*- coding: utf-8 -*-


from flask import request, g, jsonify
from rivescript import RiveScript

from . import Resource
from .. import schemas

import os
import requests

bot = RiveScript()
bot.load_directory(os.path.join(os.path.dirname(__file__), "brain"))
bot.sort_replies()

class Ask(Resource):

	def post(self):
		params = request.json
		msg = params.get("input")

		if not params:
			return jsonify({
				"status": "error",
				"error": "Request must be of the application/json type!",
				}), 400

		username = 'apple'
		
		if msg[0:3] == "whe" or msg[0:3] == "how":
			mmsg = msg.split()
			city_1 = mmsg[-1]
			url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=5f61479bff6034962312d04203602eb0'.format(city_1)
			res = requests.get(url)
			data = res.json()
			weather = str(data["weather"][0]["main"])
			temp = str(data["main"]["temp_max"])
			bot.set_variable("weather_type",weather)
			bot.set_variable("num",temp)
		reply = bot.reply(username,msg)
		return {"reply": reply}, 200