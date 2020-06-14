from typing import Final
import json

import asyncio
import aiohttp

from .Auth import Auth
from .TokenManager import TokenManager


async def getCurrentForecast(client_id: str, client_secret: str, latitude: str, longitude: str):
    return await getForecast('current', client_id, client_secret, latitude, longitude)


async def getSevenDayForecast(client_id: str, client_secret: str, latitude: str, longitude: str):
    return await getForecast('7day', client_id, client_secret, latitude, longitude)


async def getHourlyForecast(client_id: str, client_secret: str, latitude: str, longitude: str):
    return await getForecast('nexthour', client_id, client_secret, latitude, longitude)


async def get24HourForecast(client_id: str, client_secret: str, latitude: str, longitude: str):
    return await getForecast('24hour', client_id, client_secret, latitude, longitude)


async def getForecast(endpoint: str, client_id: str, client_secret: str, latitude: str, longitude: str):
    async with aiohttp.ClientSession() as session:
        tokenMgr = TokenManager(client_id, client_secret)
        auth = Auth(session, "https://api.srgssr.ch/forecasts/v1.0/weather", tokenMgr)

        # fetch 7 day weather forcast for given location
        params = {'latitude': latitude, 'longitude': longitude}
        payload = {}
        resp = await auth.request('get', endpoint, params=params, json=payload)

        # only continue if the call was successful
        if resp.status != 200:
            resp.raise_for_status()

        response = await resp.json()
        
        return response



# async def main():
#     print('Main function called')


# asyncio.run(main())