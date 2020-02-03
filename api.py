import urllib3
import json
platform = input('Witch platform do you whant to search on?').lower()
player = input('Witch player do you whant info about?').lower()
url = f'https://r6tab.com/api/search.php?platform={platform}&search={player}'
info_list = json.load(urllib3.###(url))
print(info_list)

