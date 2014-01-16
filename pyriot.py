import json
import requests

from RIOTError import RIOTError

class pyriot(object):

	def __init__(self, api_key):
		self.api_key = api_key
		self.base_url = "https://prod.api.pvp.net"


	def request(self, path, payload={}):
		payload['api_key'] = self.api_key
		response = requests.get(self.base_url + path, params=payload)
		if response.status_code == 200:
			return response.json()
		elif response.status_code == 429:
			raise RIOTError("Rate Limit Exceeded")
		else:
			raise RIOTError(response)


	def champion(self, ftp=None, version="1.1"):
		path = "/api/lol/na/v%s/champion" % (version)
		params = {'freeToPlay': ftp}
		return self.request(path, params)


	def game(self, region, summonerID, version="1.2"):
		path = "/api/lol/%s/v%s/game/by-summoner/%s/recent" % (region, version, summonerID)
		return self.request(path)


	def league(self, region, summonerID, version="2.2"):
		if version == "2.1":
			path = "/api/%s/v%s/league/by-summoner/%s" % (region, version, summonerID)
		else:
			path = "/api/lol/%s/v%s/league/by-summoner/%s" % (region, version, summonerID)
		return self.request(path)


	def stats(self, region, summonerID, version="1.2", season="SEASON3"):
		path = "/api/lol/%s/v%s/stats/by-summoner/%s/summary" % (region, version, summonerID)
		params = {'season':season}
		return self.request(path, params)


	def ranked_stats(self, region, summonerID, version="1.2", season="SEASON3"):
		path = "/api/lol/%s/v%s/stats/by-summoner/%s/ranked" % (region, version, summonerID)
		params = {'season':season}
		return self.request(path, params)


	def summoner(self, region, summoner, version="1.2"):
		if isinstance(summoner, str):
			path = "/api/lol/%s/v%s/summoner/by-name/%s" % (region, version, summoner)
		elif isinstance(summoner, int):
			path = "/api/lol/%s/v%s/summoner/%s" % (region, version, summoner)
		return self.request(path)


	def summoners(self, region, summonerIDs, version="1.2"):
		if len(summonerIDs) > 40 or not isinstance(summonerIDs, list):
			raise RIOTError("Max list size is 40.")
		path = "/api/lol/%s/v%s/summoner/%s/name" % (region, version, ",".join(str(summoner) for summoner in summonerIDs))
		return self.request(path)


	def masteries(self, region, summonerID, version="1.2"):
		path = "/api/lol/%s/v%s/summoner/%s/masteries" % (region, version, summonerID)
		return self.request(path)


	def runes(self, region, summonerID, version="1.2"):
		path = "/api/lol/%s/v%s/summoner/%s/runes" % (region, version, summonerID)
		return self.request(path)


	def team(self, region, summonerID, version="2.2"):
		#/api/lol/{region}/v2.2/team/by-summoner/{summonerId}
		if version == "2.1":
			path = "/api/%s/v%s/team/by-summoner/%s" % (region, version, summonerID)
		else:
			path = "/api/lol/%s/v%s/team/by-summoner/%s" % (region, version, summonerID)
		return self.request(path)
