#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:49:05 2018

@author: strausz
"""
import serial

instrument = {}

instrument['gps'] = {'name':'gps', 'port':'/dev/ttyUSB1', 'baudrate':4800, 
       'bytesize':8, 'parity':'N', 'stopbits':1, 'timeout':1, 'xonxoff':0, 
       'rtscts':0, 'dsrdtr':0}

instrument['sbe39'] = {'name':'sbe39', 'port':'/dev/ttyUSB0', 'baudrate':9600, 
       'bytesize':8, 'parity':'N', 'stopbits':1, 'timeout':1, 'xonxoff':0, 
       'rtscts':0, 'dsrdtr':0}


for inst, values in instrument.items():
    filename = values['name']+".txt"
    file = open(filename, 'w')
    ser = serial.Serial()
    ser.port = values['port']
    ser.baudrate = values['baudrate']
    ser.timeout = values['timeout']
    ser.open()     
    while True:
        line=ser.readline()
        line=line.decode().strip()
        line=line+"\n"
        if len(line) > 3:  
            file.write(line)
        print(line,end='')
        file.flush()
    file.close()