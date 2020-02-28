import usb.core
import sys

if len(sys.argv) != 2:
    print('Usage: ' + sys.argv[0] + ' <image>')
    exit()

image = sys.argv[1]

with open('Vend_Ax.bin', 'rb') as f:
    data = f.read()

dev = usb.core.find(idVendor=0x2A0E)

## download Vend_Ax

dev.ctrl_transfer(0x40, 0xA0, 0xE600, 0x0000, bytearray([0x01]))
step = 0x1000
for addr in range(0x0, 0x4000, step):
    size = min(len(data), step)
    if size == 0:
        break
    assert dev.ctrl_transfer(0x40, 0xA0, addr, 0x0000, data[:size]) == size
    data = data[size:]
dev.ctrl_transfer(0x40, 0xA0, 0xE600, 0x0000, bytearray([0x00]))

## upload new firmware

data = bytearray([])
step = 0x0040
for addr in range(0x0, 0x4000, step):
    data = data + dev.ctrl_transfer(0xC0, 0xA9, addr, 0x0000, step)

with open(image, 'wb') as f:
    f.write(data)
