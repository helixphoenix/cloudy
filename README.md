### Assumptions

## Assumption 1

"2. Print out average CPU/Memory of services of the same type "
"4. Have the ability to track and print CPU/Memory of all instances of a given service over
time (until the command is stopped, e.g. ctrl + c)."

Assumed that "services of the same type "[2] and "all instances of a given service"[4] means the same thing so took service_name as service type as no other service type is defined.


## Assumption 2
Defined service health with ```cpu+memory<100``` condition, which is pseudo service health should be defined by the service specific conditions and the number of CPUs was not known so the definition of health is an improvement area.

## Assumption 3
Assumed that CPX server is running on port ```7777``` only

### Tools
Used click for commands and followed the recommendations 
[here](https://towardsdatascience.com/how-to-build-and-publish-command-line-applications-with-python-96065049abc1) 

### App in general

The app can be generelize for any cloud API and the installation can be done via pip

### Running Locally
Run cpx_server on port ```./cpx_server.py 7777```

1. make sure that you are at /cloudy
2. ```python3 setup.py build```
3. ```python3 setup.py install```     
4. ```python3 cloudy/__main__.py command (optional:argument)```


### Commands
1. **services** :Prints running services to stdout. usage: ```python3 cloudy/__main__.py services```

2. **avg** :Prints out average CPU and Memory of services out of their instances. usage ```python3 cloudy/__main__.py avg```

3. **flag** :Flags services which have fewer than 2 healthy instances running. usage ```python3 cloudy/__main__.py flag```

4. **watch** : Watches specific service resources (until the command is stopped, e.g. ctrl + c). ```python3 cloudy/__main__.py watch service_name```