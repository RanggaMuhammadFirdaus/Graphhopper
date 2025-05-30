import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "c5bf0b18-9f6b-4afc-b06e-37ce25df3b97"
def geocoding (location, key):
    while location == "":
        location = input ("Enter the location again: ")
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    if json_status == 200 and len(json_data["hits"]) !=0:
        json_data = requests.get(url).json()
        lat=(json_data["hits"] [0] ["point"] ["lat"])
        lng=(json_data["hits"] [0] ["point"] ["lng"])
        name = json_data["hits"] [0] ["name"]
        value = json_data["hits"] [0] ["osm_value"]

        if "country" in json_data["hits"] [0]:
            country = json_data["hits"] [0] ["country"]
        else:
            country=""

        if "state" in json_data["hits"] [0]:
            state = json_data ["hits"] [0] ["state"]

        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        print ("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n" + url)
    else:
        lat="null"
        lng="null"
        new_loc=location
        if json_status != 200:
            print("Geocode API status: " + str(json_status) + "\nError message: " + json_data["message"])
    return json_status,lat,lng,new_loc

while True:
    loc1 = input("Starting Location: ")
    orig = geocoding(loc1, key)
    print(orig)

    loc2 = input("Destination: ")
    dest = geocoding(loc2, key)
    print(dest)
