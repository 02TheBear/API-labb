from urllib import request
import json

contery = input("Witch country(country code)? ").lower()
city = input("Witch city? ").lower()

url = f"https://samples.openweathermap.org/data/2.5/weather?q={city},{contery}&appid=417e0181c8fa548da68f08c2b20d8989"
json_dict_list = request.urlopen(url)
dict_list = json.load(json_dict_list)
zero_degrees = 273.15

# Removing extra stuff
dict_list.pop("coord")
dict_list.pop("weather")
dict_list.pop("base")
dict_list["main"].pop("pressure")
dict_list["sys"].pop("type")
dict_list["sys"].pop("id")
dict_list["sys"].pop("message")
dict_list.pop("id")
dict_list.pop("cod")

# Reformating
dict_list["main"]["temp"] -= zero_degrees
dict_list["main"]["temp"] = int(dict_list["main"]["temp"])

dict_list["main"]["temp_min"] -= zero_degrees
dict_list["main"]["temp_min"] = int(dict_list["main"]["temp_min"])

dict_list["main"]["temp_max"] -= zero_degrees
dict_list["main"]["temp_max"] = int(dict_list["main"]["temp_max"])

if dict_list["wind"]["deg"] > 22.5 and dict_list["wind"]["deg"] < 67.5:
    dict_list["wind"]["deg"] = "nordöstlig"
elif dict_list["wind"]["deg"] > 67.5 and dict_list["wind"]["deg"] < 112.5:
    dict_list["wind"]["deg"] = "östlig"
elif dict_list["wind"]["deg"] > 112.5 and dict_list["wind"]["deg"] < 157.5:
    dict_list["wind"]["deg"] = "sydöstlig"
elif dict_list["wind"]["deg"] > 157.5 and dict_list["wind"]["deg"] < 202.5:
    dict_list["wind"]["deg"] = "sydlig"
elif dict_list["wind"]["deg"] > 202.5 and dict_list["wind"]["deg"] < 247.5:
    dict_list["wind"]["deg"] = "sydvästlig"
elif dict_list["wind"]["deg"] > 247.5 and dict_list["wind"]["deg"] < 292.5:
    dict_list["wind"]["deg"] = "västlig"
elif dict_list["wind"]["deg"] > 292.5 and dict_list["wind"]["deg"] < 337.5:
    dict_list["wind"]["deg"] = "nordvästlig"
else:
    dict_list["wind"]["deg"] = "nordlig"

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

