#!/usr/bin/python3.7
import os

def main():
    print('start Comparing...')
    serialFile   = open('serial.txt','r')
    serialFound  = open('serialFound.txt','a')
    i           = 1
    for line in serialFile:
        line = line.rstrip()
        cmd             = 'cat auth.json ' + '| ' + 'grep ' + '"' + line + '"'
        resultCommand   = os.popen(cmd).read()
        if (len(resultCommand) != 0):
            result = 'Found!\r\n'
            serialFound.write(result)
        else:
            result = 'Missing: ' + line + '\r\n'
            serialFound.write(result)
        result = result.strip()
        print('[PROCESSING] {} , [RESULT]: ({})'.format(i,result))
        i = i + 1
if __name__ == "__main__":
    main()  
