# Dancing Walkthrough
## Basic instruction to start the lab

###### Establish VPN connection
By using openVPN tool you can establish VPN connection.
```bash
openvpn blabla.ovpn
```
> Replace blabla.ovpn with your own VPN profile.

###### Test connection
One of the most popular to test the connectio between two end-points is ping.
```bash
ping 10.129.120.141
```
> Replace the IP to the IP that belongs to the machine.
> Take in your considration, the way to test the connection and check if the host is live (ping). On the real life environment, most likely ping is denied on the network level or on the host to make identify hosr life harder.

###### Scan the open ports and banner grabbing
nmap one of the most popular tool to scan the hosts and perform banner grabbing.
```bash
nmap -sS <host_ip> -sV
```

###### Trying to exploit SMB
After the scan for most popular ports, SMB ports are opened, one of misconfiguration that could be take place is; there is no authentication required by SMB to access the share files/directories.

* Retrieve the shared paths
```
smbclient -L <host_ip>
```
* Access the shared paths
```
smbclient \\\\<host_ip>\<path>
```
the accessable path was `workshares`

> You can exploring the directories inside the `workshares` path, once you find flag.txt download it through `get`  command.

<p align="center" text> Good Luck </p>
<p align="center" text> Kemet </p>
