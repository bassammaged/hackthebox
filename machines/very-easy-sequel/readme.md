# Sequek Walkthrough
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
nmap -sS 10.129.145.72 -p 3306 --script vuln -oA 02-nmap-run-vuln-script.result
```

###### What after 3306 Discovery
One of the basic security checks, can be take place is trying the default credentials `root with blank password`

###### Weakness!
* Default credential.

<p align="center" text> Good Luck </p>
<p align="center" text> Kemet </p>
