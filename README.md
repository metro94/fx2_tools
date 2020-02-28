## Description

Some pratical tools for Cypress FX2 firmware operations.

## Usage

Please install Python 3.x and PyUSB first.

```
pip install pyusb
```

**Image** means packaged **firmware** with C2 header.

* firmware_download.py: download image from PC to FX2 devices (C2 format)
* firmware_upload.py: upload image from FX2 to PC
* firmware_run.py: run firmware in FX2 devices
* firmware_mkimage.py: make image from firmware
* firmware_extract.py: extract firmware from image
