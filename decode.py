import base64
Str = "this is string example....wow!!!";
#Str = Str.encode('base64','strict');
str1=base64.b64encode(str)

print ("Encoded String: " + Str)
#print ("Decoded String: " + Str.decode('base64','strict'))
#print (base64.b64decode(str))
