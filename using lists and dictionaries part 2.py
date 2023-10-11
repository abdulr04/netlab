# import required modules/packages/library 
#from pprint import pprint

# create the devices_info list 
# device_info = []
# open the file and read the single line of device info 
file = open ('devices-03.txt', 'r')
file_line = file.readline().strip()

#display the line from the file 
print ('read line: ',file_line)

# use the string 'split' function to convert
# the comma-seperated string into a list of items 
devic_info = file_line.split(',')
# display a blank line to make easier to read print('')

#display a title print 
('input converted to a list:')
# display the list with nice formatting
pprint(device_info)

# close the file
file.close()

