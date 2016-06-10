#!/usr/bin/python

import sys
from suds import null, WebFault
from suds.client import Client
import logging


username = ''
apiKey = ''
url = 'http://flightxml.flightaware.com/soap/FlightXML2/wsdl'

logging.basicConfig(level=logging.INFO)
api = Client(url, username=username, password=apiKey)
#print api

#api.service.SetMaximumResultSize(20)
#result = api.service.FlightInfo('OH-LWA', 20) 
#flightsret = result['flights']

#for flight in flightsret:
#     print "%s\t\t%s" % ( flight['origin'], flight['destination'])

result = api.service.AirlineFlightSchedules(1466459808, 1467323808, '', '', 'UAE', '188', 5, 0)
freturns = result['data']

for flight in freturns:
     print "%s\t%s" % (flight['departuretime'], flight['destination'])

