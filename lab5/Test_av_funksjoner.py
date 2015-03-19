import struct

f = "iglO52O1.jpg"

f = open(f, 'rb')

bin = struct.unpack('B', f.read(1))[0]
print bin

# f.read(1)

loop = [str(bin >> x & 1) for x in (7,6,5,4,3,2,1,0)]

print loop

loop_string = ''.join(loop)

print loop_string

index = 0
number = 0
while index < 10:
	number = number + 1
	print number
	index = index + 1



