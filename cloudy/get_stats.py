import requests
import tempfile
import json

from cloudy.get_servers import make_get_request, get_servers, SERVERS_URL

def get_stats(servers):
    services=dict()
    for server in servers:
        url=f'http://localhost:7777/{server}'
        request_content = make_get_request(url)
        if request_content:
            if request_content['service'] not in services:
                services[request_content['service']]=[{'IP':server,'cpu':request_content['cpu'],'memory':request_content['memory']}]
            else:
                services[request_content['service']].append({'IP':server,'cpu':request_content['cpu'],'memory':request_content['memory']})    
        else:
          raise Exception("Service details could not be retrieved, please try again")
    return services

def service_details():
    servers = get_servers(SERVERS_URL)
    details = get_stats(servers)
    return details


