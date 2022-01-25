# Appointment Walkthrough
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

###### Trying to explore FTP and HTTP
After the scan for most popular ports, HTTP & FTP port was opened.

* Break the system
# FTP was vulnerable to FTP anonymous credentials
# After surfing the files on FTP, there were credentials files.
# You can use the credentials file to login into web application.


###### Weakness!
* FTP anonymous login.
* Insecure storage 

<p align="center" text> Good Luck </p>
<p align="center" text> Kemet </p>
