#!/usr/bin/python
#from sbhs1 import *
import sbhs1
import os
import sys

def scan_machines():
	# erase the old map_machine_ids.txt file
	
	try:
		print "Erasing the  old map_machine_ids file......"
		file('map_machine_ids.txt', 'w').close()
	except:
	    print 'Failed to create machine map file file'
	    sys.exit(1)
	

	# open the map_machine_ids file for writing
	try:
		print "Opening map_machine_ids file......"
		map_machine_file = file('map_machine_ids.txt', 'w')
	except:
	    print 'Failed to create machine map file file'
	    sys.exit(1)
    
	# get list of device file names that start with ttyUSB* in the /dev folder
	device_files = []
	device_files += [each for each in os.listdir('/dev') if each.startswith('ttyUSB')]
	for d_f in range(0,len(device_files)):
		print "Device Files are : ",device_files

	# if no device filename found then exit
	if not device_files:
	    print 'No USB device found in /dev folder'
	    sys.exit(1)

	for device in device_files:
	    s = Sbhs()
	    # getting the number from the device filename
	    dev_id = device[6:]
	    try:
		dev_id = int(dev_id)
		print "Device ID is : ",dev_id
	    except:
		print 'Invalid device name /dev/%s' % device
		continue
	    # connect to device
	    res = s.connect_device(dev_id)
	    print "Res : ",res
	    if not res:
		print 'Cannot connect to /dev/%s' % device
		s.disconnect()
		continue
	    # get the machine id from the device
	    machine_id = s.getMachineId()
	    
	    if machine_id < 0:
		print 'Cannot get machine id from /dev/%s' % device
		s.disconnect()
		continue
	    print 'Found SBHS device /dev/%s with machine id %d' % (device, machine_id)
	    map_str = "%d=/dev/%s\n" % (machine_id, device)
	    map_machine_file.write(map_str)

	#if __name__ == 'main':
		#print 'Done. Exiting...'
	    map_machine_file.close()
	#sys.exit(1)

