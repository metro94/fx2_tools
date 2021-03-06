import usb.core
import sys

if len(sys.argv) != 2:
    print('Usage: ' + sys.argv[0] + ' <firmware>')
    exit()

firmware_filename = sys.argv[1]

with open(firmware_filename, 'rb') as f:
    data = f.read()

dev = usb.core.find(idVendor=0x2A0E)

dev.ctrl_transfer(0x40, 0xA0, 0xE600, 0x0000, bytearray([0x01]))
step = 0x1000
for addr in range(0x0, 0x4000, step):
    size = min(len(data), step)
    if size == 0:
        break
    assert dev.ctrl_transfer(0x40, 0xA0, addr, 0x0000, data[:size]) == size
    data = data[size:]
dev.ctrl_transfer(0x40, 0xA0, 0xE600, 0x0000, bytearray([0x00]))
