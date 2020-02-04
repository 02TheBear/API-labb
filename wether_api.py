from urllib import request
import json

contery = input("Witch country(country code)? ").lower()
city = input("Witch city? ").lower()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{contery}&appid=417e0181c8fa548da68f08c2b20d8989"

json_dict_list = request.urlopen(url)
dict_list = json.load(json_dict_list)
zero_degrees = 273.15

# Reformating
dict_list["main"]["temp"] -= zero_degrees
dict_list["main"]["temp"] = int(dict_list["main"]["temp"])

wind_dict = {
    "NE":{"min_deg": 23, "max_deg": 68, "direction": "nordöstlig"},
    "E":{"min_deg": 68, "max_deg": 113, "direction": "östlig"},
    "SE":{"min_deg": 113, "max_deg": 158, "direction": "sydöstlig"},
    "S":{"min_deg": 158, "max_deg": 203, "direction": "sydlig"},
    "SW":{"min_deg": 203, "max_deg": 248, "direction": "sydvästlig"},
    "W":{"min_deg": 248, "max_deg": 293, "direction": "västlig"},
    "NW":{"min_deg": 293, "max_deg": 338, "direction": "nordvästlig"},
}
temporary = "nordlig"
for wind_direction in wind_dict:
    if  int(dict_list["wind"]["deg"]) < wind_dict[wind_direction]["min_deg"] and int(dict_list["wind"]["deg"]) < wind_dict[wind_direction]["max_deg"]:
        temporary = wind_dict["wind"]["direction"]

dict_list["wind"]["deg"] = temporary

if dict_list["clouds"]["all"] < 100:
    dict_list["wind"]["all"] = "mycket målnigt"
elif dict_list["clouds"]["all"] < 75:
    dict_list["wind"]["all"] = "måtligt målnigt"
elif dict_list["clouds"]["all"] < 50:
    dict_list["wind"]["all"] = "något målnigt"
elif dict_list["clouds"]["all"] < 25:
    dict_list["wind"]["all"] = "lätt målnigt"


print(
    f"""I {dict_list["name"]},{dict_list["sys"]["country"]} är det {dict_list["main"]["temp"]} grader och en {dict_list["wind"]["speed"]}m/s vind i en {dict_list["wind"]["deg"]} riktning, det är också {dict_list["wind"]["all"]}."""
)

