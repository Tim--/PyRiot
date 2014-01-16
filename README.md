PyRiot
======

A wrapper for the RIOT API written in Python.


PyRiot is extremely easy to use and offers all functionality of the RIOT API.  You can access games, leagues, runes, masteries, and much more for any summoner in any region.


Example: Get summoner by name and retrieve league info

from pyriot import pyriot

api = pyriot("your_api_key_here")
my_summoner = api.summoner("na", "summoner_name")
league = api.league("na", my_summoner['id'])
print league
