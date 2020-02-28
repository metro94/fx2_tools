import sys

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' <image> <firmware>')
    exit()

image = sys.argv[1]
firmware = sys.argv[2]

b = bytearray([0 for i in range(0x4000)])

with open(firmware, 'rb') as f:
    a = f.read()

    if a[0] != 0xC2:
        print('First byte is always 0xC2')
        exit()

    print('VID = 0x%04X, PID = 0x%04X, DID = 0x%04X, Config = 0x%02X' %
        (a[1] | a[2] << 8, a[3] | a[4] << 8, a[5] | a[6] << 8, a[7]))
    a = a[8:] # strip firmware header

while len(a) > 0:
    length = a[0] << 8 | a[1]
    base_addr = a[2] << 8 | a[3]
    if base_addr < 0x4000:
        print('Block: length = 0x%04X, base_addr = 0x%04X' % (length, base_addr))
        b[base_addr:base_addr+length] = a[4:4+length]
    a = a[4+length:]

with open(firmware, 'wb') as f:
    f.write(b)
