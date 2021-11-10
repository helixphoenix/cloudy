import requests

SERVERS_URL="http://localhost:7777/servers"
def make_get_request(url):
    request = requests.get(url)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Bad Request")
    
    
    
def get_servers(SERVERS_URL):
    return make_get_request(SERVERS_URL)
 

