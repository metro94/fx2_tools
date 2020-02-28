import sys

VID = 0x2A0E
PID = 0x0020
DID = 0x0000
Config = 0x04

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' <firmware> <image>')
    exit()

firmware = sys.argv[1]
image = sys.argv[2]

with open(firmware, 'rb') as f:
    a = f.read()

length = len(a)

with open(image, 'wb') as f:
    f.write(bytearray([0xC2, VID & 0xFF, VID >> 8, PID & 0xFF, PID >> 8,
        DID & 0xFF, DID >> 8, Config]))
    f.write(bytearray([length >> 8, length & 0xFF, 0x00, 0x00]))
    f.write(a)
    f.write(bytearray([0x80, 0x01, 0xE6, 0x00, 0x00, 0x00, 0x00, 0x00]))
