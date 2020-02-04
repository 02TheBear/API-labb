from urllib import request
import json

contery = input("Which platform? ").lower()
city = input("Which player? ").lower()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{contery}&appid=417e0181c8fa548da68f08c2b20d8989"

json_dict_list = request.urlopen(url)
dict_list = json.load(json_dict_list)


