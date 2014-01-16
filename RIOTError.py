class RIOTError(Exception):
	def __init__(self, response):
		
		if isinstance(response, str):
			self.message = response
		else:
			self.message = {'error_code': response.status_code,
							'reason': response.reason,
							'url': response.request.url}

	def __str__(self):
		return repr(self.message)