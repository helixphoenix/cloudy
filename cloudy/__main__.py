import sys
import pathlib
import click
from cloudy.get_services import print_services, watch_service
from cloudy.health_check import flag_unhealthy
from cloudy.resource_check import print_avarage_resources



@click.group()
def cloudy():
  pass


@cloudy.command()
def services():
    print_services()
    
@cloudy.command()
@click.argument('service_name', default="", type=str)
def watch(service_name):
    watch_service(service_name)

@cloudy.command()
def flag():
    flag_unhealthy()
    
@cloudy.command()
def avg():
    print_avarage_resources()    

if __name__ == '__main__':
    cloudy()

