from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class InputFlight(BaseModel):
    total_travel_distance : float
    is_basic_economy : float
    seats_remaining : float
    duration : float
    flight_date_day : float
    flight_date_month : float
    search_date_day : float
    search_date_month : float
    departure_hour : float
    starting_airport_ATL : float
    starting_airport_BOS : float
    starting_airport_CLT : float
    starting_airport_DEN : float
    starting_airport_DFW : float
    starting_airport_DTW : float
    starting_airport_EWR : float
    starting_airport_IAD : float
    starting_airport_JFK : float
    starting_airport_LAX : float
    starting_airport_LGA : float
    starting_airport_MIA : float
    starting_airport_OAK : float
    starting_airport_ORD : float
    starting_airport_PHL : float
    starting_airport_SFO : float
    destination_airport_ATL : float
    destination_airport_BOS : float
    destination_airport_CLT : float
    destination_airport_DEN : float
    destination_airport_DFW : float
    destination_airport_DTW : float
    destination_airport_EWR : float
    destination_airport_IAD : float
    destination_airport_JFK : float
    destination_airport_LAX : float
    destination_airport_LGA : float
    destination_airport_MIA : float
    destination_airport_OAK : float
    destination_airport_ORD : float
    destination_airport_PHL : float
    destination_airport_SFO : float