#!/usr/bin/env python
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
import numpy
import socket
import json
from gnuradio import gr

class sbhs_client(gr.sync_block):
    """
    docstring for block sbhs_client
    """
    def __init__(self,address,port_num,fan_val,heat_val):
        self.address = address
        self.port_num = port_num
        self.fan_val  = fan_val
        self.heat_val = heat_val
        print "Server Address is : ",self.address
        print "Port_Number is : ",self.port_num
        
        gr.sync_block.__init__(self,
            name="sbhs_client",
            in_sig=[],
            out_sig=[numpy.float32])
        
    


    def work(self, input_items, output_items):
        #in0 = input_items[0]
        out = output_items[0]
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((self.address,self.port_num))
        data = {'_fanval':self.fan_val,'_heatval':self.heat_val}
        print "Fan and heat values :",data
        data_json = json.dumps(data)
        print "Fan and Heat value sent in JSON Format  :",data_json
        s.send(data_json)
        while 1:
            temp_received_json = json.loads(s.recv(1024))
            print "Temperature received in JSON Format : ",temp_received_json
            temp_val = int(temp_received_json['_temperature_val'])
            print "Temperature Value: ",temp_val
            out[:] = temp_val
        return len(output_items[0])

