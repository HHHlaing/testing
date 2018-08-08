# Required to call maketrans function.

intab = "aeiou"
outtab = "!@#$%"
deltab = "io"
trantab = str.maketrans(intab, outtab, deltab)

str = "this is string example....wow!!!";
print (str.translate(trantab))
