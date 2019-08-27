#!/usr/bin/python3.7
def main():
    
    print('[+] Starting Extraction...\n')
    fileToExtraction    = open('syslog.txt','r')
    searchWords         = 'SerialNumber:'
    serialResult  = open('serial.txt','a')
    for line in fileToExtraction:
            if (searchWords in line):
                arr     = line.split('SerialNumber:')
                serial   = arr[1]
                serial   = serial.strip()
                serial   = serial + '\r\n'
                serialResult.write(serial)
    print('End..')

if __name__ == '__main__':
    main()
 
