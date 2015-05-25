from scan_machines import *
from sbhs1 import *
import time

def Main():
    import socket
    import json
    
    
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    c,addr = s.accept()
    print "Connection is : ",c 
    print "Address is : ",addr
    """
    Accept a connection. The socket must be bound to an address and 
    listening for connections. The return value is a pair (conn, address) 
    where conn is a new socket object usable to send and
     receive data on the connection, and address is the address bound to 
    the socket on the other end of the connection.
    """
    print "Connection from:"+str(addr)
    data_server = json.loads(c.recv(1024))
    print "Data_Server : ",data_server
    get_fan_val = data_server['_fanval']
    get_heat_val = data_server['_heatval']
    print "Server_Fan_Val",get_fan_val
    print "Server_Fan_Val_Type",type(get_fan_val)
    print "Server_Heat_Val",get_heat_val
    print "Server_Heat_Val_Type",type(get_heat_val)
    
    #print "Scanning Machines..."
    #scan_machines()
    # SBHS init
    new_device = Sbhs()
    new_device.connect(8)
    new_device.connect_device(0)
    new_device.setFan(get_fan_val)
    new_device.setHeat(get_heat_val)
    while 1:
        get_temp_val =new_device.getTemp()
        print "Temperature from Server : ",get_temp_val
        data_temperature = {'_temperature_val':get_temp_val}
        data_temperature_json = json.dumps(data_temperature)
        print "Temeperature sent in JSON : ",data_temperature_json
        c.send(data_temperature_json)
        time.sleep(1)
    #c.close()
if __name__ == '__main__':
    Main()    