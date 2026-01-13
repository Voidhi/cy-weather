from datetime import datetime

import httpx
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

def test_current_weather_http_error_maps_to_500(client, monkeypatch):
    async def fake_get_current_weather(city, country_code=None):
        raise httpx.HTTPError("network down")

    monkeypatch.setattr(
        "src.resources.weather_resource.weather_service.get_current_weather",
        fake_get_current_weather,
    )

    r = client.get("/weather/current?city=Paris")
    assert r.status_code == 500
    assert "connexion" in r.json()["detail"]