import requests
import tempfile
import json

from cloudy.get_services import service_details

def avarage_resources():
    avarage=dict()
    services=service_details()
    for service in services:
        total_instance,cpu,mem=len(services[service]),0,0
        for instance in services[service]:
            cpu+=int(instance['cpu'].strip("%"))
            mem+=int(instance['memory'].strip("%"))
        avarage[service]=[cpu/total_instance,mem/total_instance]    
    return avarage        


# 2. Print out average CPU/Memory of services of the same type 

def print_avarage_resources():
    avarage_res= avarage_resources()
    print("   Service                        CPU            Memory")
    print("---------------------------------------------------------")
    for service, avg_resource in avarage_res.items():
        cpu=int(avg_resource[0])
        memory=int(avg_resource[1])
        print(f"{service}".ljust(18),f"              ",f"{cpu}%".ljust(15),f"{memory}%")
        
        

 


            
         
            
        