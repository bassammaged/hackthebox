#!/usr/bin/python3.7
import os

def main():
    print('start Comparing...')
    ManufFile   = open('manuf.txt','r')
    manufFound  = open('manufFound.txt','a')
    i           = 1
    for line in ManufFile:
        line = line.rstrip()
        cmd             = 'cat auth.json ' + '| ' + 'grep ' + '"' + line + '"'
        resultCommand   = os.popen(cmd).read()
        if (len(resultCommand) != 0):
            result = 'Found!\r\n'
            manufFound.write(result)
        else:
            result = 'Missing: ' + line + '\r\n'
            manufFound.write(result)
        result = result.strip()
        print('[PROCESSING] {} , [RESULT]: ({})'.format(i,result))
        i = i + 1
if __name__ == "__main__":
    main()
