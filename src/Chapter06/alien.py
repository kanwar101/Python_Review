alien_0={'key1':'value1', 'key2':'value2','key3':'value3'}
print (alien_0['key1'])

alien_0['key4'] = 'value4'
print (alien_0)


empty_dict={}
empty_dict['system'] = 'HP'
empty_dict['OS'] = 'Chrome'
empty_dict['processor']='intel'

print (empty_dict)

empty_dict['system']='Dell'
print (empty_dict)

# if loop with dictionaries
alien_0={'x_position':0, 'y_position':25, 'speed':'fast'}
print (f"Original Position {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment =2
else:
	x_increment = 3

alien_0 ['x_position'] = alien_0 ['x_position'] + x_increment

print (alien_0)


# remove value pair from dictionary

del alien_0['speed']
print (alien_0)

# dictionary usage

