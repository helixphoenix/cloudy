import requests
import tempfile
import json
import time
from datetime import datetime
from cloudy.get_stats import service_details
from cloudy.health_check import health_check

#1. Print running services to stdout (similar to the table below) 
def print_services():
    services=service_details()    
    print("-------------------------------------------","Running Services","------------------------------------------")  
    print("")    
    print("   IP                       Service                  Status                   CPU            Memory")
    print("-------------------------------------------------------------------------------------------------------")
    for service, instances in services.items():
        for instance in instances:
            status=health_check(instance)
            print(f"{instance['IP']}".ljust(25),f"{service}".ljust(25),f"{status}".ljust(25),f"{instance['cpu']}".ljust(15),f"{instance['memory']}")




# 4. Have the ability to track and print CPU/Memory of all instances of a given service over
# time (until the command is stopped, e.g. ctrl + c).


def watch_service(service_name):
    service_stats=service_details()
    service_stat=service_stats[service_name]  
    print("---------------",f"{service_name} Stats","---------------")     
    print("") 
    while True:
        print("-----------------","time:",datetime.now().strftime("%H:%M:%S"),"------------------")
        print("")
        print("   IP                     CPU            Memory")
        print("---------------------------------------------------")
        for instance in service_stat:
            print(f"{instance['IP']}".ljust(25),f"{instance['cpu']}%".ljust(15),f"{instance['memory']}%")
        time.sleep(30)
        
 