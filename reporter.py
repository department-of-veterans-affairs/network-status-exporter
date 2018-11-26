from easysnmp import Session


def print_status(status):
  if status is None or status.value is None:
    return 'no status reported'

  elif status.value == '1':
    return 'idle'
  elif status.value == '2':
    return 'connect'
  elif status.value == '3':
    return 'active'
  elif status.value == '4':
    return 'opensent'
  elif status.value == '5':
    return 'openconfirm'
  elif status.value == '6':
    return 'established'
  else:
    return 'unknown status'

## ------------
for config in configuration:
    hostname = config.get('hostname')
    route1, route2 = config.get('routes')
    community = config.get('community')
    print "Host: " + hostname

    # Create an SNMP session to be used for all our requests
    session = Session(hostname=hostname, community=community, version=2)

    # Route 1 - BGP connection to 10.241.16.16
    status = session.get('.1.3.6.1.2.1.15.3.1.2.' + route1)
    print "BGP Peering Status Connection 1: " + print_status(status)

    # Route 2 - BGP connection to 10.242.16.16
    status = session.get('.1.3.6.1.2.1.15.3.1.2.' + route2)
    print "BGP Peering Status Connection 2: " + print_status(status)
