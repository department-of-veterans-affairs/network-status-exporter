from easysnmp import Session
from prometheus_client import start_http_server, Enum
from yaml import load, Loader
import sys
import time


router_states = [
    'no_status',
    'idle',
    'connect',
    'active',
    'opensent',
    'openconfirm',
    'established',
    'unknown_status'
]


def print_status(status):
  if status is None or status.value is None:
    return router_states[0]
  elif status.value == '1':
    return router_states[1]
  elif status.value == '2':
    return router_states[2]
  elif status.value == '3':
    return router_states[3]
  elif status.value == '4':
    return router_states[4]
  elif status.value == '5':
    return router_states[5]
  elif status.value == '6':
    return router_states[6]
  else:
    return router_states[7]


def poll_routers(configuration, env, prom_metric):
    for config in configuration:
        hostname = config.get('hostname')
        community = config.get('community')

        # Create an SNMP session to be used for all our requests
        session = Session(hostname=hostname, community=community, version=2)

        for route in config.get('routes'):
            status = session.get('.1.3.6.1.2.1.15.3.1.2.' + route)
            e.labels(hostname, route, community, env).state(print_status(status))


if __name__ == '__main__':
    e = Enum(
        'bgp_connection_state',
        'Status of Router BGP connections',
        labelnames=('hostname', 'connection', 'community', 'environment'),
        states=router_states
    )
    start_http_server(8000)
    with open(sys.argv[1], 'r') as conf_file:
        config = load(conf_file, Loader=Loader)
        while True:
            poll_routers(config['routers'], config['environment'], e)
            time.sleep(config['poll_interval'])

