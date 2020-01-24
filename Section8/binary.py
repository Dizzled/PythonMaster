# with open("binary", "bw") as binaryFile:
#         binaryFile.write(bytes(range(17)))
#
# with open("binary", "br") as binFile:
#     for b in binFile:
#         print(b)

a = 65534   # FF FE
b = 65535   # FF FF
c = 65536   # 00 10 00 00
x = 2998302 # 02 2D C0 1E


# Its important to know the big or little endianess of the binary file to read from
with open('binary2', 'bw') as b2:
    b2.write(a.to_bytes(2, 'big'))
    b2.write(b.to_bytes(2, 'big'))
    b2.write(c.to_bytes(4, 'big'))
    b2.write(x.to_bytes(4, 'big'))
    b2.write(x.to_bytes(4, 'little'))

with open('binary2', 'br') as b3:
    e = int.from_bytes(b3.read(2), 'big')
    print(e)
    g = int.from_bytes(b3.read(2), 'big')
    print(g)
    h = int.from_bytes(b3.read(4), 'big')
    print(h)
    i = int.from_bytes(b3.read(4), 'big')
    print(i)
    j = int.from_bytes(b3.read(4), 'big')
    print(j)
