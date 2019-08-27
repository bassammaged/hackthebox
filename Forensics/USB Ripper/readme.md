# USB Ripper Write up
## [+] Challenge Information:
- Hackthebox challenge link: https://www.hackthebox.eu/home/challenges/download/81 <br>
- zip password: "hackthebox" without "qoutation"
- The challenge discription: <br>
    ```There is a sysadmin, who has been dumping all the USB events on his Linux host all the year... Recently, some bad guys managed to steal some data from his machine when they broke into the office. Can you help him to put a tail on the intruders? Note: once you find it, "crack" it.```
## [+] Walkthrough:
1. tried to figure out auth.json, and we found that:
    - auth.json is contains the manufacturer number and serial number for authrozied removable devices.
    ![auth.log manufacturer screenshot](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/manufAuthjson.PNG)
    ![auth.log serial screenshot](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/serialAuthjson.png)
    <br>
    <br>
2. we opened the syslog file, and we found a ton of informations about removable devices that connected with the machine in the last year but we noticed that there are important details mentioned in the file (manufaturer number and serial number for each device).
<br>
![syslog screenshot](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/syslog.PNG)
    <br>
    <br>
    
```we need to analysis this massive information! so we decided to create scripts to anlysis the syslog and auth.log```

   <br>
   <br>
3. firstly, we created two script to extract serial number and manufacturer number for each device on sepreate sheet.


   - [Manufacturer extraction script](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/scripts/extractManuf.py)
   - [Serial Number extraction script](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/scripts/extractSerial.py)
    <br>
    <br>
    ![Manufacturer extaction Script photo](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/Manufextraction.PNG)
    ![Serial number extaction Script photo](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/serialextraction.PNG)
    <br>
    <br>
    ![Extacted Manufacturer screenshot](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/Manufextraction1.PNG)
    ![Extacted Serial number screenshot](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/serialextraction1.PNG)
    <br>
    <br>
 4. we wrote another script to compare the extracted serial number and manufacturer number with the auth.log content to figure out if there is any removable device un-authorized contected with the machine or not.
 ```we are looking for the extracted serial number and extracted manufacturer number that not mentioned in auth.log.```
    - [Compare manufacturer number script](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/scripts/manufCompare.py)
    - [Compare serial number script](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/scripts/serialCompare.py)
    <br>
![Compare manufacturer number script screenshot](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/manufcompare.PNG)
![Compare serial number script screenshot](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/serialcompare.PNG)
    <br>
    <br>
5. finally, we found the missed manufacturer number or serial number! Holaaaaaaa.
![Missed serial number](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/serialcompare1.PNG)
    <br>
    <br>
6. open syslog and searching about any intresting infomration about the intruder removable device, nothing new!
![missed value screenshot](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/missingvalue.PNG)
<br>
<br>
7. we noticed that the length of missed value is 32, may be! holly could be a MD5! let's try to online rainbow attack.
![flag](https://github.com/BassamMaged/HackTheBox/blob/master/Forensics/USB%20Ripper/pics/flag.PNG)

<br>
<br>

```Thank you for reading my write up, Schemer - Black Toppers Team```
