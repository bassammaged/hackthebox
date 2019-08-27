#!/usr/bin/python3.7
def main():
    
    
    print('[+] Starting Extraction...\n')
    fileToExtraction    = open('syslog.txt','r')
    searchWords         = 'Manufacturer'
    manufacturerResult  = open('manuf.txt','a')
    for line in fileToExtraction:
            if (searchWords in line):
                arr     = line.split('Manufacturer:')
                manuf   = arr[1]
                manuf   = manuf.strip()
                manuf   = manuf + '\r\n'
                manufacturerResult.write(manuf)
    print('End..')

if __name__ == '__main__':
    main()
 
