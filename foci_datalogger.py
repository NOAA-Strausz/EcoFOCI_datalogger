#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:47:01 2018

@author: dave

goal of this program is to make a simple serial logger, possibly for use as
a shipboard underway sampling system logger
"""
import serial



#start instrument dictionary for keeping instrument info in
instrument = {}

instrument['gps'] = {'name':'gps', 'port':'/dev/ttyUSB0', 'baudrate':9600, 
       'bytesize':8, 'parity':'N', 'stopbits':1, 'timeout':1, 'xonxoff':0, 
       'rtscts':0, 'dsrdtr':0}

ser = serial.Serial()
ser.port = instrument['gps']['port']
ser.baudrate = instrument['gps']['baudrate']
ser.timeout = instrument['gps']['timeout']
ser.open()

file = open('test.txt','w')

while True:
    line=ser.readline()
    line=line.decode().strip()
    line=line+"\n"
    if len(line) > 3:  
        file.write(line)
        print(line,end='')
    file.flush()
file.close()



