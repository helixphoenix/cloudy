
from cloudy.get_stats import service_details

def health_check(instance: dict):
    cpu=int(instance['cpu'].strip("%"))
    memory=int(instance['memory'].strip("%"))
    if cpu+memory>100:
        return "Unhealthy"
    else:
        return "Healthy"
    
    

# 3. Flag services which have fewer than 2 healthy instances running 
def flag_unhealthy():
    services=service_details()
    state='Healthy'
    for service, instances in services.items():
        healthy=0
        for instance in instances:
            status= health_check(instance)
            if status=="Healthy":
                healthy+=1
        if healthy<2:
            print(f"{service} is Unhealthy, please be aware")
            state='Unhealthy'
    if state=='Healthy':
       print("Nothing to flag about yet, Enjoy your day")        
            
        
    
        