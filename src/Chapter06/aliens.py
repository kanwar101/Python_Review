aliens_0 = {'color':'green', 'point':5}
alient_1 = {'color':'blue', 'point':7} 
alient_2 = {'color':'white', 'point':10}


aliens =[aliens_0,alient_1, alient_2]

for alien in aliens:
	print(alien)
	print("next item in the list")


empty_aliens = []
for value in range(0,10):
	new_alien = {'color':'Orange', 'points':value*2}
	empty_aliens.append (new_alien)

print (empty_aliens)

print ("Only first 5 element")
print (empty_aliens[:5])