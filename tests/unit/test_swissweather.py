import unittest
from typing import Final
import json
import os
from datetime import datetime

import asyncio

from swissweather.api import getCurrentForecast, getSevenDayForecast, getHourlyForecast, get24HourForecast


class TestWeatherAPI(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.CLIENT_ID: Final = os.getenv('CLIENT_ID')
        self.CLIENT_SECRET: Final = os.getenv('CLIENT_SECRET')
        
        self.LATITUDE: Final = "46.94843"
        self.LONGITUDE: Final = "7.44323"


    async def test_getCurrentForecast(self):
        """
        Test response for getting the current forecast
        
        Test that the date returned is today and that the location returned is Berne
        """

        response = await getCurrentForecast(self.CLIENT_ID, self.CLIENT_SECRET, self.LATITUDE, self.LONGITUDE)

        # test a few values
        forecast_date = response['current_day']['date']
        timestamp = datetime.now()
        day = timestamp.strftime('%Y-%m-%d')

        self.assertEqual(day, forecast_date, "Assertion failed: wrong date")
        self.assertEqual(response['info']['name']['de'], 'Bern', "Assertion failed: wrong location")

        print(">>> Testing current forecast complete.")


    async def test_getSevenDayForecast(self):
        """
        Test response for getting the 7 day forecast

        Test that the date returned is today and that the location returned is Berne
        """

        response = await getSevenDayForecast(self.CLIENT_ID, self.CLIENT_SECRET, self.LATITUDE, self.LONGITUDE)

        # test a few values
        forecast_date = response['7days'][0]['date']
        timestamp = datetime.now()
        day = timestamp.strftime('%Y-%m-%d')

        self.assertEqual(day, forecast_date, "Assertion failed: wrong date")
        self.assertEqual(response['info']['name']['de'], 'Bern', "Assertion failed: wrong location")

        print(">>> Testing 7 day forecast complete.")


    async def test_getHourlyForecast(self):
        """
        Test response for getting the hourly forecast

        Test that the date/time returned is the current hour and that the location returned is Berne
        """

        response = await getHourlyForecast(self.CLIENT_ID, self.CLIENT_SECRET, self.LATITUDE, self.LONGITUDE)

        # test a few values
        forecast_date = response['date']
        timestamp = datetime.now()
        today = timestamp.strftime('%Y-%m-%d')

        self.assertEqual(today, forecast_date, "Assertion failed: wrong date")
        self.assertEqual(response['info']['name']['de'], 'Bern', "Assertion failed: wrong location")

        print(">>> Testing hourly forecast complete.")



    async def test_get24HourForecast(self):
        """
        Test response for getting the 24 hour forecast

        Test that the date/time returned is the current hour and that the location returned is Berne
        """

        response = await get24HourForecast(self.CLIENT_ID, self.CLIENT_SECRET, self.LATITUDE, self.LONGITUDE)

        # test a few values
        forecast_date = response['date']
        timestamp = datetime.now()
        today = timestamp.strftime('%Y-%m-%d')

        self.assertEqual(today, forecast_date, "Assertion failed: wrong date")
        self.assertEqual(response['info']['name']['de'], 'Bern', "Assertion failed: wrong location")

        print(">>> Testing 24 hour forecast complete.")



if __name__ == '__main__':
    unittest.main()