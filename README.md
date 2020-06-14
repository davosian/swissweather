# Swiss Weather API

This is a library to consume the SRF Meteo weather API published by Switzerland's public broadcasting cooperation, SRG SSR. You can find the API documentation [on their website](https://developer.srgssr.ch/apis/srgssr-weather).

## Example Usage

The following code snippet shows how to use the library to get the current weather for a specific location in Switzerland (Berne).

```python
from typing import Final
from datetime import datetime
import json

from swissweather.api import getCurrentForecast
import asyncio

async def main():

    CLIENT_ID: Final = 'MY_CLIENT_ID' # get your account at https://developer.srgssr.ch/apis/srgssr-weather
    CLIENT_SECRET: Final = 'MY_CLIENT_SECRET'

    LATITUDE: Final = "46.94843" # Berne downtown
    LONGITUDE: Final = "7.44323" # Berne downtown

    response = await getCurrentForecast(CLIENT_ID, CLIENT_SECRET, LATITUDE, LONGITUDE)
    print(json.dumps(response, indent=2))


asyncio.run(main())
```

## Usage Details

First, you must [apply for a developer token and agree to their terms](https://developer.srgssr.ch/apis/srgssr-weather). As of this writing (June 2020), this is free for non-commercial use. After being accepted, you will get a `client_id` and `client_secret` you can use to interact with the service using this Python library.

All endpoints require the following parameters to be passed along:

`client_id`: the username you received from registering as developer from the link above

`client_secret`: the matching password you received from registering as developer from the link above

`latitude`: the first part of the coordinates from the location in Switzerland you want to know the forecast in `WGS 84` notation.

`longitude`: the second part of the coordinates from the location in Switzerland you want to know the forecast in `WGS 84` notation.

You can use an online map service like https://map.geo.admin.ch to get the coordinates for location you are interested in. Make sure you get the coordinates in the `WGS 84` notation, not in the Swiss coordinate system. For this, you can switch to the `WGS 84` notation in the dropdown at the bottom left of the map screen. Then move the mouse over the location you are interested in and you will see the coordinates next to the dropdown at the bottom of the map.

Currently, the following end-points are supported:


### Daily forecast for location

`https://api.srgssr.ch/forecasts/v1.0/weather/current`: Returns current weather forecast for all Swiss locations.

You get this forecast by calling `getCurrentForecast(client_id: str, client_secret: str, latitude: str, longitude: str)`.

To find out about the information provided in the payload, have a look at the [official documentation for currentforecast](https://developer.srgssr.ch/apis/srgssr-weather/docs/currentforecast).

### Seven day forecast for location

`https://api.srgssr.ch/forecasts/v1.0/weather/7day`: Returns next 7 days forecast for specific location.

You get this forecast by calling `getSevenDayForecast(client_id: str, client_secret: str, latitude: str, longitude: str)`.

To find out about the information provided in the payload, have a look at the [official documentation for weeksforecastbyid](https://developer.srgssr.ch/apis/srgssr-weather/docs/weeksforecastbyid).


### Hourly Forecast for location

`https://api.srgssr.ch/forecasts/v1.0/weather/nexthour`: Returns forecast data for the next hour for a specific location.

You get this forecast by calling `getHourlyForecast(client_id: str, client_secret: str, latitude: str, longitude: str)`.

To find out about the information provided in the payload, have a look at the [official documentation for hourforecastbyid](https://developer.srgssr.ch/apis/srgssr-weather/docs/hourforecastbyid).


### 24 hour forecast for location 

`https://api.srgssr.ch/forecasts/v1.0/weather/24hour`: Returns cities within Swiss locations.

You get this forecast by calling `get24HourForecast(client_id: str, client_secret: str, latitude: str, longitude: str)`.

To find out about the information provided in the payload, have a look at the [official documentation for 24hourforecastbyid](https://developer.srgssr.ch/apis/srgssr-weather/docs/24hourforecastbyid).