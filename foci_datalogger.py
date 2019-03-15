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

instrument = {'name':'gps', 'port':'/dev/ttyS0', 'baudrate':9600, 
       'bytesize':8, 'parity':'N', 'stopbits':1, 'timeout':1, 'xonxoff':0, 
       'rtscts':0, 'dsrdtr':0, 'poll_string':'TS\r'}

ser = serial.Serial()
ser.port = instrument['port']
ser.baudrate = instrument['baudrate']
ser.timeout = instrument['timeout']
ser.open()

file = open('test.txt','w')

while True:
    if instrument['poll_string']:
        ser.write(str.encode(instrument['poll_string']))
    line=ser.readline()
    line=line.decode().strip()
    line=line+"\n"
    if len(line) > 5:  
        file.write(line)
        print(line,end='')
    file.flush()
file.close()



