# network-status-exporter

## Deps

Requires:
* Net-SNMP > 5.7 
  * Fedora/Centos: `yum install net-snmp-devel`
  * Debian/Ubuntu: `apt install libsnmp-dev snmp-mibs-downloader` (note requries non-free repos to be enabled)
* Python 2.7
  * Included with Dockerfile

## Usage

The demo application will send a SNMP request for a status update from selected BGP peering connection to a network appliance. The SNMP response will include whether the peering connection are **established**.

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python reporter.py config.yml
```

## Configuration

```yaml
poll_interval: 15
environment: dev
routers:
  - host: 29.38.10.2
    community: pgbcommunity
    routes:
      - 29.28.10.3
      - 29.28.10.4
```

## License

This work is [public domain](https://creativecommons.org/publicdomain/zero/1.0/).
