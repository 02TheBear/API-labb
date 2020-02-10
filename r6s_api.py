from urllib import request
import json
import tabulate

#Used to check a players stats
def  one_player():
    player = input("Which player? ").lower()

    url = f"""https://r6tab.com/api/search.php?platform=uplay&search={player}"""

    json_dict_list = request.urlopen(url)
    dict_list = json.load(json_dict_list)
    return(dict_list)

print(one_player())