mysystems =['alexa','laptop','intel','amd','siri']


copy_mysystems=mysystems[:]
print (copy_mysystems)

mysystems.append('tv')

copy_mysystems.append('monitor')

print (mysystems)
print (copy_mysystems)

another_copy_mystsems = mysystems

print (another_copy_mystsems)
mysystems.append('box')

print (another_copy_mystsems)