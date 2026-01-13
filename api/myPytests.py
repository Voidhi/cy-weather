from datetime import datetime
from src.models.Weather import WeatherRequest, WeatherResponse
from src.services.weather_service import WeatherService
from pydantic import ValidationError
from pathlib import Path

import sys
import pytest
  

def test_weather_service_class():
    weather_service = WeatherService()

    ville_test_réel = "Pau"
    ville_test_imaginaire = "utopia"

    # get_current_weather :
    """ ith pytest.raises(ValidationError):
        weather_service.get_current_weather(city=ville_test_imaginaire)
         """
    


def test_weather_request_valid():
    req = WeatherRequest(city="Paris", country_code="FR")
    assert req.city == "Paris"
    assert req.country_code == "FR"


def test_weather_request_city_required():
    with pytest.raises(ValidationError):
        WeatherRequest(city="")

