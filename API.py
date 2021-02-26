from urllib import request
import json
import time


def trackTime(funcToBeDecorated):
    def timeTaken(api):
        startTime = int(time.time() * 1000)  # milliseconds
        funcToBeDecorated(api)
        endTime = int(time.time() * 1000)  # milliseconds
        print("\nResults:-")
        print(f"Function: {funcToBeDecorated.__name__}, Time Taken: {endTime - startTime}")

    return timeTaken


@trackTime
def RESTapi(api):
    handle = request.urlopen(api)  # opening the api url
    data = handle.read().decode()  # reading the data
    js = json.loads(data)  # loading the json
    # lst = []
    periods = js["properties"]["periods"]
    for p in range(0, len(periods)):
        start = periods[p]["startTime"]  # getting the start time
        temp = periods[p]["temperature"]  # getting the temparature
        unit = periods[p]["temperatureUnit"]  # getting the unit of temperature
        # lst.append(f"{start[11:16]} {temp}{unit}")
        print(f"{start[11:16]} {temp}{unit}")
    # return "\n".join(i for i in lst)


api = "https://api.weather.gov/gridpoints/TOP/31,80/forecast/hourly"
RESTapi(api)
