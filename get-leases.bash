#!/bin/bash
scp root@192.168.50.10:/var/lib/dhcp/dhcpd.leases dhcpd.leases
python3 dhcp_parser.py dhcpd.leases
