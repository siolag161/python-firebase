from datetime import datetime, timedelta
import decimal
import jsonpickle

try:
    total_seconds = datetime.timedelta.total_seconds
except AttributeError:
    total_seconds = lambda self: ((self.days * 86400 + self.seconds) * 10 ** 6 + self.microseconds) / 10 ** 6.0

class DateTimeHandler(jsonpickle.handlers.BaseHandler):
    def flatten(self, obj, data):
        return obj.isoformat()

class TimeDeltaHandler(jsonpickle.handlers.BaseHandler):
    def flatten(self, obj, data):
        return total_seconds(obj)

class DecimalHandler(jsonpickle.handlers.BaseHandler):
    def flatten(self, obj, data):
        return float(obj)
	
jsonpickle.handlers.registry.register(datetime, DateTimeHandler)
jsonpickle.handlers.registry.register(timedelta, TimeDeltaHandler)
jsonpickle.handlers.registry.register(decimal.Decimal, DecimalHandler)

def json_encode(obj):
    return jsonpickle.encode(obj, unpicklable=False)

def json_decode(js):
    return jsonpickle.decode(js)

