# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liveinstaller.ui'
#
# Created: Wed Mar 8 21:01:56 2006
#      by: The PyQt User Interface Compiler (pyuic) 3.15.1
#
# WARNING! All changes made in this file will be lost!


from qt import *
from kdecore import *
from kdeui import *


image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x04" \
    "\xea\x49\x44\x41\x54\x38\x8d\xb5\x94\x5b\x6c\x54" \
    "\xd7\x15\x86\xbf\x7d\xce\x99\x99\x33\xb6\x67\xc6" \
    "\x60\x30\xb6\xc7\xa6\x5c\x64\xc7\x80\x08\xe0\xe0" \
    "\x94\x9a\x8b\x1d\x0a\xb9\x15\xa5\xad\x12\x48\x5e" \
    "\x22\x84\xf2\x9e\xbc\xe4\xa6\x24\x44\x4a\xa4\xa8" \
    "\x95\xfa\x52\xa9\x51\x1f\xd2\x87\xb4\x6f\x55\x42" \
    "\x12\x29\x51\x54\x1e\x72\x21\xf7\x88\x60\x20\x38" \
    "\xc5\x08\x98\x9a\x38\x36\x61\xf0\xd8\x9e\xf1\x39" \
    "\x67\xe6\xec\x7d\xf6\x39\xbb\x0f\xa9\x10\x97\x84" \
    "\xaa\x0f\x5d\x8f\x6b\xed\xf5\xe9\x5f\x5b\xeb\x5f" \
    "\xf0\x7f\x0a\xfb\x66\xc5\x8e\x1c\xcb\x1c\x1b\x27" \
    "\xd4\x48\x80\xae\x02\x1d\x07\x46\xf2\xfb\x5d\x3b" \
    "\x71\xab\x7e\x52\x95\xf1\x0f\xf9\xff\x09\xbc\x73" \
    "\x4d\x7a\xe4\x2f\xcf\xef\x78\x65\x70\xa5\xbb\xf9" \
    "\xc8\x89\xca\x11\x1c\xd7\x79\xea\xc1\xfe\x83\xcf" \
    "\x3e\x77\xe0\xc5\xbd\xf7\xac\xbd\xff\xce\xf5\xee" \
    "\xce\x2e\x57\x16\x65\x18\xca\x5a\x60\xaa\x2a\x21" \
    "\xba\xba\x5f\x5c\x0f\x6c\x72\xc8\x3e\xb2\x6b\xf1" \
    "\x81\x67\x9e\xd9\xf7\x6c\xc7\xc0\x50\x57\x54\x1a" \
    "\x8b\xff\xf6\xda\xc4\xa1\xec\x9a\xbd\xad\x77\x6c" \
    "\xdd\xb0\xc3\x71\xb3\xd9\xd0\x9f\xa2\x10\x8f\x51" \
    "\xf0\x4f\x33\x57\x3a\x3f\x37\x3a\x5a\x3a\x7e\xf8" \
    "\xd8\xa5\xc3\x1f\x8c\xfb\xef\x9f\xad\xc4\x67\xeb" \
    "\x11\xf5\x6b\xc0\x3d\xad\x14\x9f\xdf\xdf\x7f\xf0" \
    "\xe1\x47\x1f\xde\x9f\x69\xef\x76\xcd\xa5\x49\x66" \
    "\xfd\x22\xee\x8a\xfb\x68\x69\x6d\xc3\x00\x51\x14" \
    "\xe3\x79\x01\x97\xa7\xcf\xd3\x3a\xfb\x36\x9d\xd1" \
    "\x38\x2c\xcc\x63\xe6\x67\x29\x97\xbd\x99\xb7\xbe" \
    "\x9a\x79\xf3\xe9\x7f\x54\x9f\x74\xfe\x23\x5b\x6c" \
    "\xeb\x4d\x0f\xfd\xfe\xf1\xe1\xdf\x0d\xed\x7d\x60" \
    "\x3b\x58\x30\x79\x06\x6f\x56\x60\xf5\xee\xa6\xa5" \
    "\xb5\x8d\x38\x4e\x88\x22\x8d\x94\x0a\x25\x25\x4d" \
    "\x85\x2e\xbe\xaf\x6e\xa1\xb9\xfc\x35\x79\xbf\x82" \
    "\xf0\xe6\x28\xd8\x4e\xf3\xd8\xa5\xe8\x54\x10\x11" \
    "\x58\x00\x96\x40\xec\x5c\xdf\x3c\xb2\x65\xf7\xf0" \
    "\x2f\x88\x34\x7c\x3b\x4e\x32\x79\x8e\xc0\xee\x27" \
    "\xb7\xb4\x88\xd6\x31\x4a\x45\x48\xa9\xa8\xd7\x43" \
    "\x94\x8a\xd0\x51\x84\x5d\x58\xc9\xb4\xea\x06\x6f" \
    "\x0e\xa4\xe4\x9d\xaf\x6b\xef\xfe\xf5\x58\xf0\xaa" \
    "\x23\x70\x6c\x00\x03\xe6\xe4\x44\x78\x72\x49\x7d" \
    "\x62\xf1\x40\xd1\xbd\x4d\x94\x27\x85\x2c\x57\x08" \
    "\x57\x3f\x48\x53\x5b\x11\x25\x23\x7c\xbf\xce\xf4" \
    "\xd4\x24\xde\x82\x87\x65\x3b\x68\x1d\x93\x18\x0b" \
    "\x6f\x7e\x8e\x8e\xf2\xc7\x28\x69\xc9\xcf\xa7\x92" \
    "\xa3\x83\x7d\x1d\x5b\xee\x5b\x9e\xec\xbb\xb2\x15" \
    "\x52\xa3\x4e\x9e\xab\x9e\xd8\xb6\x74\x7e\x6b\x91" \
    "\xa0\xa7\xd1\x70\x91\x6b\x1f\x22\xd5\x94\xa7\xd1" \
    "\x08\xf9\x6e\xf2\x02\x8d\x99\x71\xe4\x42\x99\x30" \
    "\xce\xe0\xa4\x32\x44\x3a\xc6\x5f\xa8\xb2\x4c\x97" \
    "\x48\xad\xbd\x3d\x1e\xd8\xdc\x3b\xd8\xa2\x55\xeb" \
    "\x2b\x1f\x4d\xbd\xec\xdc\xd6\xc3\xc6\xde\xee\x5c" \
    "\xdf\xc0\xba\xe2\xa6\x55\x2b\x97\xae\x6e\x5f\xb3" \
    "\xb4\xc3\xb4\xe4\x63\x33\x59\xb1\x63\x63\x08\xa5" \
    "\x26\xa8\x87\x34\x82\x05\x9a\xd4\x34\xb1\x86\x5a" \
    "\xd0\x4e\xca\xcd\xa1\xe3\x84\x42\x3e\x45\xaa\xe5" \
    "\x16\x4c\xd8\xb0\x5e\x3f\x74\xf4\xd0\x0b\x6f\x97" \
    "\x9e\x3b\x5f\x33\x67\x9d\x0d\x45\xd6\x0f\x6f\xc8" \
    "\x8d\xec\xbc\x77\xe3\xae\xee\x5b\x37\x2e\xa7\xb9" \
    "\x00\xbe\x47\xf3\xe2\x0a\x29\xff\x7d\x94\xee\x43" \
    "\x88\x4e\x2c\x27\x4b\x23\xd5\x43\x6c\x14\x58\x19" \
    "\x12\xad\x58\xa6\xc6\xe8\x56\xef\x91\x4a\x02\x8e" \
    "\x7e\x39\x71\xf6\x89\xd7\xcf\x3f\x76\x29\xe4\xfb" \
    "\x2b\x7b\xec\x58\xd8\x3f\x5b\xcc\xf2\xad\xfd\xf9" \
    "\xad\xbf\x19\xea\xf9\xed\xaf\xf6\xed\xd9\x93\xb6" \
    "\x48\x33\x75\x1a\x66\x2f\xa3\xb5\x8b\x97\xed\x65" \
    "\x2a\xb3\x96\x5a\x61\x1d\x4d\xb9\x02\x3d\xc1\xa7" \
    "\x2c\x99\xff\x08\x11\xd5\xc1\x36\x7c\xf8\xd9\xc5" \
    "\xd1\x5f\xff\xf9\xcc\x2f\x3d\x4d\x0d\xc0\x01\xd0" \
    "\x09\x71\xa9\xc2\x44\xe9\xd3\x85\x89\x13\xe7\xfe" \
    "\x79\x6a\xdb\x03\x7b\x86\xf3\xeb\x86\xdb\xaa\xd9" \
    "\x4d\xe4\x9b\x3e\xc7\x9d\x1a\x65\x91\x73\x81\x45" \
    "\x79\x45\xd8\xec\x61\x66\xcb\x64\x67\x8e\x43\xa2" \
    "\xc1\x12\x18\x01\x46\xc7\x42\x5c\x65\x38\xe7\x7a" \
    "\xe7\x25\x88\x98\x24\x49\xfc\x30\xc3\x6c\xfa\x2e" \
    "\x6a\x2b\xb7\x93\xee\x2a\xd1\x2c\xcf\x50\x08\x4f" \
    "\xe3\x54\xbf\xc1\xae\x5c\x84\x60\x0e\x6c\x07\x23" \
    "\x2c\x54\x12\x63\x25\xb1\xb0\xae\xb2\xdb\x0d\x60" \
    "\x8c\x30\x46\x29\x4c\xa8\x31\xc6\x61\x3e\xc8\xe1" \
    "\x66\x36\x21\x9b\xfa\x08\x2e\xce\xd0\xe5\x9f\xc2" \
    "\x8e\x14\x28\x45\x62\x69\x64\x12\x63\x2c\x81\x48" \
    "\xae\x3d\x11\x3f\x02\x06\x13\x86\x48\x3f\x21\x13" \
    "\xcf\x53\x6f\xd4\xa9\xd5\x2c\xc8\x46\x64\xe5\x02" \
    "\x34\x02\x50\x21\x89\x6a\x10\x1a\x88\x01\xdb\x71" \
    "\xc0\x5c\x7b\xcf\x6e\x00\x1b\x10\x71\x5d\x8a\xea" \
    "\xe5\x06\xe9\xcc\x34\x6d\x6e\x8a\x1a\x29\x32\x42" \
    "\x43\x63\x1e\x1a\x3e\x46\x2a\xa4\x6c\xf0\xc3\xaf" \
    "\x5a\x08\x91\x60\xe1\xda\x37\x05\x0b\x83\x25\xc2" \
    "\xc0\xee\x0a\x8f\x30\x37\x93\x63\xc1\x5a\x41\x3d" \
    "\xb5\x82\x28\xe5\x90\xf7\xa6\x11\x61\x9d\x58\x69" \
    "\xb4\x94\x60\x59\x58\xb6\x43\xa8\x9b\xe3\xd1\x7f" \
    "\x05\x5f\x85\x31\xe1\x4f\x82\x3d\x69\xbc\xb1\x2f" \
    "\xc7\xbf\x19\x1c\xf0\x36\x2f\xcf\x9a\x6c\xac\x3e" \
    "\xc3\x0b\x5d\xfc\x28\x47\xde\x1b\xc7\xe8\x3a\x89" \
    "\x36\xa0\x23\xac\x74\x96\x72\xad\x65\xf6\x4f\x9f" \
    "\xd4\xfe\xf8\xea\x29\xef\xe5\x30\xa1\x71\x45\xe0" \
    "\x0d\x8a\x41\x2c\x71\x59\xb2\xb1\x33\x33\xb8\xeb" \
    "\x96\x45\x77\xef\xe8\x6f\x1d\xe9\xeb\x74\x7a\xf3" \
    "\x4e\xe0\x12\xd6\x48\x64\x44\x6c\x67\xd0\xa1\xe2" \
    "\xd8\x77\xee\xf1\x97\x8e\x54\x0f\x7e\x38\xa5\x0e" \
    "\x27\x90\x5c\xc7\xb9\x79\xb4\xbb\x74\x0c\x2c\xcb" \
    "\xfc\x7c\xf7\xea\x96\xbb\xb7\xaf\x4a\x0f\xf7\xb6" \
    "\xdb\xab\x12\x27\xcb\xdf\xbf\xa8\xbc\xf6\x87\x2f" \
    "\x6a\x2f\x5c\xf0\x93\xd2\x8f\xf5\xfd\x57\xf0\xd5" \
    "\x93\x74\x66\x45\xf1\xf6\x4e\x77\xc8\x75\x44\xf6" \
    "\x9d\x52\xfd\x8d\x20\xc6\xff\xa9\xf7\xff\x06\x2b" \
    "\xe8\x63\xaa\x26\xe5\xb4\x20\x00\x00\x00\x00\x49" \
    "\x45\x4e\x44\xae\x42\x60\x82"
image1_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x20\x00\x00\x00\x20" \
    "\x08\x06\x00\x00\x00\x73\x7a\x7a\xf4\x00\x00\x06" \
    "\x86\x49\x44\x41\x54\x58\x85\xe5\x97\x5b\x6c\x54" \
    "\xd7\x15\x86\xbf\x73\x99\xb1\xc7\xe3\x19\x66\xec" \
    "\x61\xc6\x63\x18\xc6\x06\x6c\x27\xbe\x81\x01\x73" \
    "\x71\x20\x04\xe2\x42\x93\x22\x4a\x11\xc4\x21\x6e" \
    "\xe2\x24\x54\x91\x2a\x91\x2a\x10\x45\x6d\x42\xdb" \
    "\xa8\x51\x2b\xb5\xef\xa8\xaa\x94\x36\x2a\x44\xaa" \
    "\xaa\xf4\xa1\x2f\xf4\x29\x51\x1f\xf2\xd0\x56\xb2" \
    "\x4a\x25\xd4\x90\x98\x40\x2d\xa4\x9a\x4b\xb0\xc7" \
    "\x97\x61\x98\x39\x67\xdf\xfa\x70\xf0\xc4\xa5\xe1" \
    "\x62\xd4\x2a\x0f\xdd\xd2\x92\xce\xd9\x67\xed\xb5" \
    "\xff\xf5\xaf\xb5\xff\xad\x63\x19\x63\xf8\x32\x87" \
    "\xfd\xa5\xee\x0e\xb8\x00\xef\x59\xd6\xa2\x17\x1a" \
    "\x78\x52\xc3\x8f\x81\x88\x81\x9f\x01\xbf\x5e\x6c" \
    "\x8c\x67\x8c\x09\x00\x3c\xc0\xe6\xad\x96\x6d\xbd" \
    "\xbb\xee\xd9\xa1\x86\x50\x7d\x94\xd1\x77\xde\xfd" \
    "\x85\x5f\xf6\xc7\x2c\xf8\xf3\x62\x63\x3d\x10\x00" \
    "\x01\xaf\xb7\xf6\xf5\x34\x74\xbc\xf9\x16\xb8\x21" \
    "\x26\xc7\x3e\xad\x39\xfb\xc1\x87\x3f\x0a\xc1\x13" \
    "\x80\x5a\x4c\xac\x45\xf7\x80\x81\xfe\x1a\xd7\x79" \
    "\xa6\xf3\xf0\x8b\x40\x08\x66\x6e\xd0\x39\x34\x44" \
    "\x34\x5a\xb7\xdd\x87\x3d\x12\xb8\x5f\x7b\x20\x00" \
    "\x12\xde\x58\xf5\xf8\xb6\x68\x72\xc7\x57\xa0\x30" \
    "\x05\x85\x29\xea\x57\x3f\x4c\xd7\xee\x9d\x61\x09" \
    "\xdf\x57\x10\xf9\x9f\x01\x50\xf0\x64\x24\x5a\xbb" \
    "\xaf\x63\x64\x04\x34\x70\xe3\x06\x94\xcb\x50\xba" \
    "\x49\xc7\xe0\x20\x89\xc6\xe4\x06\x1f\x9e\x37\x01" \
    "\x53\xf7\xb4\x2a\x80\xfb\x74\x0e\x29\x38\xde\xb6" \
    "\x7b\x90\x68\x57\x1f\x14\x0a\x01\x80\x62\x11\x66" \
    "\x67\xa9\x89\xa7\xe8\xd9\x3e\x80\x82\x57\x14\x34" \
    "\xfe\xd7\x19\x10\xf0\xcd\x25\xa9\xe4\x40\xc7\x73" \
    "\xcf\x41\xc5\x87\x62\x11\x2f\x93\xa1\x92\xcf\x43" \
    "\xa5\x02\x33\xb3\x3c\xb4\x71\x0b\xcd\xb9\x6c\x7b" \
    "\x05\x5e\x56\x8b\x01\x70\xaf\xec\x75\x50\xd7\x57" \
    "\x3a\x0f\xec\x23\x9c\x5b\x05\x93\x9f\xa1\x22\x11" \
    "\x44\x77\x37\x62\xc3\x06\x64\x3a\x0d\xd3\x05\x5c" \
    "\x2b\xc4\xba\x2d\x9b\x31\xf0\x92\x84\xac\x0e\xd6" \
    "\xde\xd1\xee\x1b\x80\x84\x17\x52\xcb\xd2\xbd\xb9" \
    "\xaf\x7e\x0d\xe6\x8a\x70\xb3\x0c\x6d\x6d\xd4\xd7" \
    "\xd6\x12\xb3\x6d\xec\xfe\x7e\x8c\xd6\x30\x33\x43" \
    "\x4b\x2e\xcf\x8a\xfc\xb2\xac\x07\xaf\xca\x80\xb9" \
    "\x3b\xda\xfd\x02\xc8\x19\xf8\x5e\xd7\xc1\xfd\x84" \
    "\x53\x4d\x30\x79\x1d\xd3\xdc\x8c\x9f\x4a\x71\xea" \
    "\xd4\x29\x4e\x9c\x38\xc1\x6c\x7d\x3d\x6c\xda\x04" \
    "\xd3\xd3\x38\xbe\xa4\xbf\xb7\x17\xdb\xb6\x5f\x52" \
    "\xb0\xf6\x5e\x4d\xe8\xb2\xe0\xe5\x0e\xb5\x7f\x39" \
    "\xbb\x3a\x9f\xcb\x3f\xbe\x1b\x0a\xd3\xa0\x14\xd6" \
    "\x86\x0d\x8c\x8e\x8e\x32\x32\x32\x02\x40\x72\xe9" \
    "\x52\x86\x0f\x1c\x80\xf7\xdf\x87\xcb\x13\xb4\xc4" \
    "\x93\xb4\xb5\xe6\x62\x67\x2f\x5e\x7a\x2d\x0c\xc3" \
    "\x77\x8b\x7f\x57\x06\x34\xb4\xd9\x8e\xfd\x7c\xef" \
    "\x53\x07\xb1\x22\xb1\xe0\xdc\xe7\x72\x10\x0e\xa3" \
    "\xa5\xc4\x75\x6f\x09\xa9\x94\xe0\x38\xb0\x75\x2b" \
    "\xcc\x15\xb1\x8a\x25\x06\x5a\x5a\xa9\xad\xad\x39" \
    "\x28\x60\xab\x22\x90\xc7\xdb\xad\x0a\xe0\x2e\xd9" \
    "\x1f\xcf\xf7\x75\x2f\x6d\xda\xfc\x08\x4c\x15\xc0" \
    "\x75\xa1\xa7\x07\x80\xc6\x86\x06\xe2\xf1\x38\x00" \
    "\xd9\x6c\x36\x58\xb0\x7b\x37\x2c\x5f\x0e\xd3\x05" \
    "\xb2\x58\xf4\x2c\xcb\x86\xca\xf0\x96\x06\x77\xd1" \
    "\x4d\xa8\xe0\xd1\x70\x4d\xe8\x50\xcf\xd0\xd3\x58" \
    "\x4e\x38\xc8\xbe\xbb\x1b\x62\x31\x00\x32\x99\x0c" \
    "\x89\x44\x82\xba\xba\x3a\x52\xa9\x54\x10\x2d\x12" \
    "\x81\xa1\xa1\x40\x1b\xa6\x66\x78\x24\x91\x24\x19" \
    "\x8d\xec\xf0\xe0\xc0\x5d\x19\xf8\x82\xe6\x08\x0b" \
    "\x38\xb6\xba\x7f\x6d\x38\x51\x03\x5c\xb9\x0c\xb1" \
    "\x38\xba\xad\xad\xca\x4e\x2a\x95\x22\x93\xc9\x10" \
    "\x8f\xc7\x69\x6c\x6c\xac\xce\x9b\x81\x81\x80\xa5" \
    "\xeb\xd7\x09\x7b\x25\xd6\xe4\x97\x21\xe0\x98\x84" \
    "\x98\x0f\x2c\xb4\x3b\x96\x40\xc0\xb6\xba\x64\xe2" \
    "\xeb\x6d\x6b\xdb\x99\xf9\xd5\x4f\x29\xfc\xf2\x27" \
    "\x78\x2b\x9a\xa0\xae\xae\xea\x63\xdb\x36\x4d\x4d" \
    "\x4d\xa4\xd3\x69\x32\x99\x4c\x75\xde\xaa\xa9\xc1" \
    "\x1b\x3e\xc4\x47\xc5\x2b\xfc\xf5\xca\x05\x5a\xe2" \
    "\x51\x32\x4b\xe2\xfd\x15\xf8\xc6\x1d\x19\xb8\xad" \
    "\x36\x35\x0a\xde\x6c\xdf\xd4\x47\x78\xe2\x1c\xfe" \
    "\x95\x39\xbc\xda\x30\xa2\xb3\x2b\x38\xeb\x0b\x46" \
    "\x3a\x9d\xa6\xb9\xb9\xf9\xf3\x66\x04\xb4\xd6\x98" \
    "\xc7\x76\x70\xf3\xb1\x47\x29\x4d\x6b\x8a\xd7\xfe" \
    "\xc9\x9a\xe6\x34\xd8\xf6\x71\x0d\x8d\x5f\x78\x17" \
    "\x2c\x1c\x12\x9e\x4d\x34\xa5\xb7\xad\x6a\x6d\xa4" \
    "\x72\xee\xef\x28\x07\x9c\xef\xfc\x00\x1a\x33\x28" \
    "\x21\xd0\x0b\x40\x64\xb3\x59\x5a\x5a\x5a\x3e\xa7" \
    "\xdf\x18\x94\x94\x10\xae\x65\xd9\x6b\x3f\xc4\x89" \
    "\x85\x99\xbc\x36\x45\xb3\x0b\xb9\x78\xbc\xdd\x83" \
    "\xa3\xfa\x36\x06\x6e\xd7\x81\xb8\x82\xa3\xed\xfd" \
    "\xbd\xd8\x97\xce\x21\x26\x05\x7a\x70\x3b\xec\xdc" \
    "\x83\x9c\x2b\x62\x3b\x36\x58\x16\xae\xeb\x62\xdb" \
    "\x36\x47\x8e\x1c\x41\x08\x51\xcd\x5c\x29\x85\x54" \
    "\x0a\xe1\x15\xa9\xed\xdf\x42\x62\xdf\x7e\x26\x4e" \
    "\xfe\x96\xc9\xcf\xae\xd2\x9b\x4a\x71\x71\x76\xf6" \
    "\xb0\x30\xe6\x6d\x0b\x2e\x55\x4b\x39\x0f\xc0\x04" \
    "\xb5\x3f\x9c\x6e\xc9\x75\xae\xc8\xd4\x73\xf3\x93" \
    "\x31\x54\xd4\x45\x3e\xf5\x2d\x84\xb1\x91\xbe\x87" \
    "\x90\x12\x21\x04\x4a\x29\x7c\xdf\xe7\xcc\x99\x33" \
    "\x8c\x8e\x8e\x52\x2a\x95\xd0\x5a\x23\xa5\x44\x4a" \
    "\x89\xf0\x7d\xfc\x8a\x47\x62\xe4\x30\x6e\x43\x8c" \
    "\xc2\xd4\x0d\x1a\xb4\xa0\x23\xb9\xa4\xc9\x83\xa3" \
    "\xf3\x12\xfd\x6f\x00\x14\xb4\xe0\x38\x6f\x74\x0f" \
    "\xac\x47\x5f\xf8\x1b\xb2\xa8\xa8\x0c\x3e\x81\xb7" \
    "\x71\x07\x62\xba\x80\xef\xfb\x55\x0b\x85\x42\x9c" \
    "\x3e\x7d\x9a\x5d\xbb\x76\xb1\x77\xef\x5e\x4e\x9e" \
    "\x3c\x89\xeb\xba\xd5\xef\x42\x08\xfc\x99\x69\x9c" \
    "\xae\x5e\xe2\xc3\xc3\x48\x09\x57\xa7\xae\xd3\x17" \
    "\x8f\x12\xb6\xed\x6f\x0b\xd8\xfc\x1f\x3a\x20\xe0" \
    "\x58\x76\xf5\xca\x54\xca\x2a\x51\x19\xbf\x84\xae" \
    "\x77\xb9\xb1\xff\x45\x3c\xcf\xc7\xd3\x0a\x5f\x1b" \
    "\x84\x09\xac\x2c\x04\x4d\xb9\x1c\x6b\xd6\xaf\xa7" \
    "\xfd\xe1\x4e\x56\xb4\xae\xc4\x53\x0a\x5f\xeb\x05" \
    "\x66\xf0\x4a\x25\xea\x0f\x1e\xc2\x5d\x9a\x60\x7a" \
    "\xce\x87\x72\x99\xce\x78\x2c\xec\xc1\xab\xf3\x00" \
    "\xe6\x7b\xa0\xcb\x71\xdd\xa7\xbb\xfa\xbb\xf0\xcf" \
    "\xff\x09\xa1\xc1\x18\x85\x33\x3e\x86\x58\xb1\x0a" \
    "\x0f\x0d\xd2\x47\xfb\x61\x5c\xd7\x45\x94\x6f\xd2" \
    "\xb1\xb2\x95\xdf\xff\xee\x3d\x94\x94\x24\x1b\x92" \
    "\x4c\x5d\xbb\x1a\xf4\xc0\xad\x32\xf9\xbe\x8f\xc0" \
    "\xa2\xfc\xe9\x79\x64\xc5\x47\x03\x57\x66\xe6\xe8" \
    "\x6d\x48\xf2\x51\xd1\xd9\x5b\x52\x6a\x27\xf0\x47" \
    "\xcb\x18\xc3\xcf\x2d\xeb\x9d\x8e\x8d\x6b\x5f\xe8" \
    "\xcb\xc7\x99\xfb\xcb\x87\x68\x1b\xb4\x02\xe9\x86" \
    "\x91\xcb\xdb\xd0\xc6\xc2\x18\x50\xd8\xc1\x1d\x61" \
    "\x2c\x34\x16\x8e\x13\x42\x1b\xa8\xf8\x02\x65\x40" \
    "\x19\x83\x32\x06\x69\x40\x69\x8d\xc6\xa6\x72\x69" \
    "\x1c\x31\x57\x44\xdb\xe0\x29\xc8\xc7\xa2\x4c\x58" \
    "\x36\x1f\xcc\x16\xff\xf0\x1b\x63\xf6\x04\x07\xd8" \
    "\xb6\x77\x2e\x6f\x4e\x61\x2e\x7f\x8c\x1b\xaf\x47" \
    "\x03\x4a\x83\x25\x15\xce\xf8\x27\x28\x03\x52\x1b" \
    "\x50\xa0\x8c\xc6\x68\x30\x06\x2a\x0a\xb4\x09\x7c" \
    "\x95\x06\x65\x82\x77\x74\x40\xab\x31\x10\x76\x2c" \
    "\x9c\x5a\x17\xad\xc0\xb5\x0c\xb3\x65\x8f\xa6\xba" \
    "\x08\x11\xcb\x5a\x57\x2d\x81\xd2\xfa\xec\xf8\xd8" \
    "\x78\xde\xe9\x78\x08\xd9\xa0\x30\x4a\xa3\xa5\xc2" \
    "\x68\x8d\xd1\x06\xad\x14\x5a\x6b\xb4\xd2\x18\xa5" \
    "\xb1\xb4\xc6\x56\x0a\x57\x6b\x94\xd6\x58\x4a\xe3" \
    "\x28\x8d\xd6\x0a\xa3\x02\x7f\xb3\xc0\xbf\xba\x56" \
    "\x6b\x6c\xad\xb9\xe0\xf9\x08\x63\xfe\x51\x05\x60" \
    "\xc3\xeb\x63\x1f\x5f\x0c\x9d\x1f\x9f\xe8\x33\x96" \
    "\xa5\x95\x31\x26\x50\x45\x83\xc1\x42\x1b\x13\xb0" \
    "\x82\xb9\x55\x8a\xf9\xeb\xda\x04\x59\xdf\x12\xa1" \
    "\x79\x35\x55\x18\xb4\x99\x7f\xbe\xe5\x5b\xfd\x09" \
    "\x36\x8e\xaf\xcd\x05\x0b\xbe\x0b\x60\xfd\xdf\xff" \
    "\x1d\xff\x0b\xd9\x03\xa5\x10\xde\x04\x0b\x01\x00" \
    "\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

class EspressoUI(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        self.image1 = QPixmap()
        self.image1.loadFromData(image1_data,"PNG")
        if not name:
            self.setName("EspressoUI")


        EspressoUILayout = QGridLayout(self,1,1,11,6,"EspressoUILayout")

        layout9_4_2_2 = QHBoxLayout(None,0,6,"layout9_4_2_2")
        spacer2_2_4_2_2 = QSpacerItem(280,16,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9_4_2_2.addItem(spacer2_2_4_2_2)

        self.logo_image = QLabel(self,"logo_image")
        self.logo_image.setPixmap(self.image0)
        self.logo_image.setScaledContents(1)
        layout9_4_2_2.addWidget(self.logo_image)
        spacer3_2_4_2_2 = QSpacerItem(161,16,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9_4_2_2.addItem(spacer3_2_4_2_2)

        EspressoUILayout.addMultiCellLayout(layout9_4_2_2,0,0,0,3)

        self.textLabel = QLabel(self,"textLabel")

        EspressoUILayout.addMultiCellWidget(self.textLabel,1,1,0,3)

        self.backButton = QPushButton(self,"backButton")

        EspressoUILayout.addWidget(self.backButton,3,1)

        self.nextButton = QPushButton(self,"nextButton")

        EspressoUILayout.addWidget(self.nextButton,3,2)

        self.cancelButton = QPushButton(self,"cancelButton")

        EspressoUILayout.addWidget(self.cancelButton,3,3)
        spacer31 = QSpacerItem(240,41,QSizePolicy.Expanding,QSizePolicy.Minimum)
        EspressoUILayout.addItem(spacer31,3,0)

        self.widgetStack = QWidgetStack(self,"widgetStack")
        self.widgetStack.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred,0,1,self.widgetStack.sizePolicy().hasHeightForWidth()))

        self.stepWelcome = QWidget(self.widgetStack,"stepWelcome")
        stepWelcomeLayout = QGridLayout(self.stepWelcome,1,1,11,6,"stepWelcomeLayout")

        self.introLabel = QLabel(self.stepWelcome,"introLabel")
        self.introLabel.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)

        stepWelcomeLayout.addWidget(self.introLabel,2,0)
        spacer10 = QSpacerItem(41,130,QSizePolicy.Minimum,QSizePolicy.Expanding)
        stepWelcomeLayout.addItem(spacer10,4,0)
        spacer7 = QSpacerItem(51,120,QSizePolicy.Minimum,QSizePolicy.Expanding)
        stepWelcomeLayout.addItem(spacer7,0,0)
        self.widgetStack.addWidget(self.stepWelcome,0)

        self.stepLanguage = QWidget(self.widgetStack,"stepLanguage")
        stepLanguageLayout = QGridLayout(self.stepLanguage,1,1,11,6,"stepLanguageLayout")

        self.language_treeview = KListView(self.stepLanguage,"language_treeview")
        self.language_treeview.addColumn(i18n("Language"))

        stepLanguageLayout.addMultiCellWidget(self.language_treeview,0,2,0,0)

        self.textLabel1_2 = QLabel(self.stepLanguage,"textLabel1_2")

        stepLanguageLayout.addWidget(self.textLabel1_2,0,1)

        self.line1_2 = QFrame(self.stepLanguage,"line1_2")
        self.line1_2.setFrameShape(QFrame.HLine)
        self.line1_2.setFrameShadow(QFrame.Sunken)
        self.line1_2.setFrameShape(QFrame.HLine)

        stepLanguageLayout.addWidget(self.line1_2,1,1)

        self.textLabel2_3 = QLabel(self.stepLanguage,"textLabel2_3")
        self.textLabel2_3.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred,0,1,self.textLabel2_3.sizePolicy().hasHeightForWidth()))
        self.textLabel2_3.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)

        stepLanguageLayout.addWidget(self.textLabel2_3,2,1)
        self.widgetStack.addWidget(self.stepLanguage,1)

        self.stepLocation = QWidget(self.widgetStack,"stepLocation")
        stepLocationLayout = QGridLayout(self.stepLocation,1,1,11,6,"stepLocationLayout")

        self.frame3 = QFrame(self.stepLocation,"frame3")
        self.frame3.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred,0,1,self.frame3.sizePolicy().hasHeightForWidth()))
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)

        stepLocationLayout.addWidget(self.frame3,1,0)

        layout9 = QGridLayout(None,1,1,0,6,"layout9")

        self.textLabel4 = QLabel(self.stepLocation,"textLabel4")
        self.textLabel4.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)

        layout9.addMultiCellWidget(self.textLabel4,2,2,0,2)

        self.textLabel2 = QLabel(self.stepLocation,"textLabel2")

        layout9.addWidget(self.textLabel2,0,0)
        spacer19 = QSpacerItem(161,31,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9.addItem(spacer19,2,3)

        self.textLabel3_2 = QLabel(self.stepLocation,"textLabel3_2")

        layout9.addWidget(self.textLabel3_2,1,0)

        self.timezone_city_combo = QComboBox(0,self.stepLocation,"timezone_city_combo")

        layout9.addWidget(self.timezone_city_combo,0,1)

        self.timezone_zone_text = QLabel(self.stepLocation,"timezone_zone_text")

        layout9.addWidget(self.timezone_zone_text,1,1)
        spacer18 = QSpacerItem(291,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9.addMultiCell(spacer18,1,1,2,3)
        spacer17 = QSpacerItem(291,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout9.addMultiCell(spacer17,0,0,2,3)

        stepLocationLayout.addLayout(layout9,2,0)

        self.textLabel1 = QLabel(self.stepLocation,"textLabel1")

        stepLocationLayout.addWidget(self.textLabel1,0,0)
        self.widgetStack.addWidget(self.stepLocation,2)

        self.stepKeyboardConf = QWidget(self.widgetStack,"stepKeyboardConf")
        stepKeyboardConfLayout = QGridLayout(self.stepKeyboardConf,1,1,11,6,"stepKeyboardConfLayout")
        spacer16_2_2 = QSpacerItem(21,193,QSizePolicy.Minimum,QSizePolicy.Expanding)
        stepKeyboardConfLayout.addItem(spacer16_2_2,0,0)
        spacer17_2_2 = QSpacerItem(21,193,QSizePolicy.Minimum,QSizePolicy.Expanding)
        stepKeyboardConfLayout.addItem(spacer17_2_2,2,0)

        self.textLabel1_3_2 = QLabel(self.stepKeyboardConf,"textLabel1_3_2")

        stepKeyboardConfLayout.addWidget(self.textLabel1_3_2,1,0)
        self.widgetStack.addWidget(self.stepKeyboardConf,3)

        self.stepUserInfo = QWidget(self.widgetStack,"stepUserInfo")
        stepUserInfoLayout = QGridLayout(self.stepUserInfo,1,1,11,6,"stepUserInfoLayout")

        self.warning_info = QLabel(self.stepUserInfo,"warning_info")
        self.warning_info.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)

        stepUserInfoLayout.addWidget(self.warning_info,3,0)

        self.ident_label_3 = QLabel(self.stepUserInfo,"ident_label_3")

        stepUserInfoLayout.addWidget(self.ident_label_3,0,0)
        spacer10_2 = QSpacerItem(41,91,QSizePolicy.Minimum,QSizePolicy.Expanding)
        stepUserInfoLayout.addItem(spacer10_2,4,0)

        layout7 = QGridLayout(None,1,1,0,6,"layout7")

        self.textLabel4_2 = QLabel(self.stepUserInfo,"textLabel4_2")

        layout7.addWidget(self.textLabel4_2,0,0)

        layout6_2 = QGridLayout(None,1,1,10,6,"layout6_2")
        spacer19_2 = QSpacerItem(161,31,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout6_2.addItem(spacer19_2,0,2)

        self.hostname = QLineEdit(self.stepUserInfo,"hostname")

        layout6_2.addWidget(self.hostname,0,1)

        self.hostname_label1_2 = QLabel(self.stepUserInfo,"hostname_label1_2")

        layout6_2.addWidget(self.hostname_label1_2,0,0)

        layout7.addLayout(layout6_2,1,0)

        stepUserInfoLayout.addLayout(layout7,2,0)

        layout8 = QGridLayout(None,1,1,0,6,"layout8")

        layout5_2 = QGridLayout(None,1,1,10,6,"layout5_2")

        self.pasword_label1_2 = QLabel(self.stepUserInfo,"pasword_label1_2")

        layout5_2.addWidget(self.pasword_label1_2,2,0)

        self.username_label1_2 = QLabel(self.stepUserInfo,"username_label1_2")

        layout5_2.addWidget(self.username_label1_2,1,0)

        self.fullname = QLineEdit(self.stepUserInfo,"fullname")

        layout5_2.addWidget(self.fullname,0,1)
        spacer16_3 = QSpacerItem(141,31,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout5_2.addItem(spacer16_3,1,2)
        spacer15_2 = QSpacerItem(141,31,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout5_2.addItem(spacer15_2,0,2)
        spacer17_3 = QSpacerItem(151,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout5_2.addItem(spacer17_3,2,2)

        self.verified_label_2 = QLabel(self.stepUserInfo,"verified_label_2")

        layout5_2.addWidget(self.verified_label_2,3,0)
        spacer18_2 = QSpacerItem(151,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout5_2.addItem(spacer18_2,3,2)

        self.username = QLineEdit(self.stepUserInfo,"username")

        layout5_2.addWidget(self.username,1,1)

        self.password = QLineEdit(self.stepUserInfo,"password")

        layout5_2.addWidget(self.password,2,1)

        self.verified_password = QLineEdit(self.stepUserInfo,"verified_password")

        layout5_2.addWidget(self.verified_password,3,1)

        self.fullname_label1_2 = QLabel(self.stepUserInfo,"fullname_label1_2")

        layout5_2.addWidget(self.fullname_label1_2,0,0)

        layout8.addLayout(layout5_2,1,0)

        self.user_label_2_2 = QLabel(self.stepUserInfo,"user_label_2_2")

        layout8.addWidget(self.user_label_2_2,0,0)

        stepUserInfoLayout.addLayout(layout8,1,0)
        self.widgetStack.addWidget(self.stepUserInfo,4)

        self.stepPartAuto = QWidget(self.widgetStack,"stepPartAuto")
        stepPartAutoLayout = QGridLayout(self.stepPartAuto,1,1,11,6,"stepPartAutoLayout")

        self.partition_label2 = QLabel(self.stepPartAuto,"partition_label2")

        stepPartAutoLayout.addWidget(self.partition_label2,2,0)

        self.drives = QComboBox(0,self.stepPartAuto,"drives")

        stepPartAutoLayout.addWidget(self.drives,1,1)

        self.drives_label2 = QLabel(self.stepPartAuto,"drives_label2")

        stepPartAutoLayout.addWidget(self.drives_label2,1,0)

        self.textLabel2_2 = QLabel(self.stepPartAuto,"textLabel2_2")

        stepPartAutoLayout.addMultiCellWidget(self.textLabel2_2,0,0,0,1)

        self.autopartition_frame = QFrame(self.stepPartAuto,"autopartition_frame")
        self.autopartition_frame.setFrameShape(QFrame.StyledPanel)
        self.autopartition_frame.setFrameShadow(QFrame.Raised)

        stepPartAutoLayout.addMultiCellWidget(self.autopartition_frame,3,3,0,1)
        spacer18_2_2 = QSpacerItem(31,140,QSizePolicy.Minimum,QSizePolicy.Expanding)
        stepPartAutoLayout.addItem(spacer18_2_2,5,0)

        self.new_size_frame = QFrame(self.stepPartAuto,"new_size_frame")
        self.new_size_frame.setFrameShape(QFrame.StyledPanel)
        self.new_size_frame.setFrameShadow(QFrame.Raised)
        new_size_frameLayout = QGridLayout(self.new_size_frame,1,1,11,6,"new_size_frameLayout")

        self.new_size_scale = QSlider(self.new_size_frame,"new_size_scale")
        self.new_size_scale.setMaxValue(100)
        self.new_size_scale.setOrientation(QSlider.Horizontal)

        new_size_frameLayout.addWidget(self.new_size_scale,0,1)

        self.new_size_label = QLabel(self.new_size_frame,"new_size_label")

        new_size_frameLayout.addWidget(self.new_size_label,0,0)

        self.partition_bar = QProgressBar(self.new_size_frame,"partition_bar")

        new_size_frameLayout.addMultiCellWidget(self.partition_bar,1,1,0,1)

        stepPartAutoLayout.addMultiCellWidget(self.new_size_frame,4,4,0,1)
        self.widgetStack.addWidget(self.stepPartAuto,5)

        self.stepPartAdvanced = QWidget(self.widgetStack,"stepPartAdvanced")
        stepPartAdvancedLayout = QGridLayout(self.stepPartAdvanced,1,1,11,6,"stepPartAdvancedLayout")

        self.textLabel6_2 = QLabel(self.stepPartAdvanced,"textLabel6_2")

        stepPartAdvancedLayout.addWidget(self.textLabel6_2,0,0)

        self.splitter2 = QSplitter(self.stepPartAdvanced,"splitter2")
        self.splitter2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Preferred,0,1,self.splitter2.sizePolicy().hasHeightForWidth()))
        self.splitter2.setOrientation(QSplitter.Horizontal)

        self.textLabel7_2 = QLabel(self.splitter2,"textLabel7_2")
        self.textLabel7_2.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)

        self.qtparted_frame = QFrame(self.splitter2,"qtparted_frame")
        self.qtparted_frame.setFrameShape(QFrame.StyledPanel)
        self.qtparted_frame.setFrameShadow(QFrame.Raised)

        stepPartAdvancedLayout.addWidget(self.splitter2,1,0)
        self.widgetStack.addWidget(self.stepPartAdvanced,6)

        self.stepPartMountpoints = QWidget(self.widgetStack,"stepPartMountpoints")
        stepPartMountpointsLayout = QGridLayout(self.stepPartMountpoints,1,1,11,6,"stepPartMountpointsLayout")

        layout14 = QGridLayout(None,1,1,0,6,"layout14")

        self.msg_error2 = QLabel(self.stepPartMountpoints,"msg_error2")

        layout14.addMultiCellWidget(self.msg_error2,0,1,2,2)
        spacer26 = QSpacerItem(21,31,QSizePolicy.Minimum,QSizePolicy.Expanding)
        layout14.addItem(spacer26,1,0)

        self.img_error2 = QLabel(self.stepPartMountpoints,"img_error2")
        self.img_error2.setPixmap(self.image1)
        self.img_error2.setScaledContents(1)

        layout14.addWidget(self.img_error2,0,0)
        spacer25 = QSpacerItem(31,21,QSizePolicy.Expanding,QSizePolicy.Minimum)
        layout14.addItem(spacer25,0,1)

        stepPartMountpointsLayout.addLayout(layout14,2,1)

        layout12 = QGridLayout(None,1,1,0,6,"layout12")

        self.mountpoint8 = QComboBox(0,self.stepPartMountpoints,"mountpoint8")
        self.mountpoint8.setEditable(1)

        layout12.addWidget(self.mountpoint8,8,0)

        self.size4 = QLabel(self.stepPartMountpoints,"size4")

        layout12.addWidget(self.size4,4,1)

        self.size2 = QLabel(self.stepPartMountpoints,"size2")

        layout12.addWidget(self.size2,2,1)

        self.mountpoint1 = QComboBox(0,self.stepPartMountpoints,"mountpoint1")
        self.mountpoint1.setEditable(1)

        layout12.addWidget(self.mountpoint1,1,0)

        self.mountpoint2 = QComboBox(0,self.stepPartMountpoints,"mountpoint2")
        self.mountpoint2.setEditable(1)

        layout12.addWidget(self.mountpoint2,2,0)

        self.textLabel4_2_2 = QLabel(self.stepPartMountpoints,"textLabel4_2_2")

        layout12.addWidget(self.textLabel4_2_2,0,1)

        self.partition7 = QComboBox(0,self.stepPartMountpoints,"partition7")

        layout12.addWidget(self.partition7,7,2)

        self.partition4 = QComboBox(0,self.stepPartMountpoints,"partition4")

        layout12.addWidget(self.partition4,4,2)

        self.size10 = QLabel(self.stepPartMountpoints,"size10")

        layout12.addWidget(self.size10,10,1)

        self.partition5 = QComboBox(0,self.stepPartMountpoints,"partition5")

        layout12.addWidget(self.partition5,5,2)

        self.partition8 = QComboBox(0,self.stepPartMountpoints,"partition8")

        layout12.addWidget(self.partition8,8,2)

        self.partition6 = QComboBox(0,self.stepPartMountpoints,"partition6")

        layout12.addWidget(self.partition6,6,2)

        self.size8 = QLabel(self.stepPartMountpoints,"size8")

        layout12.addWidget(self.size8,8,1)

        self.size5 = QLabel(self.stepPartMountpoints,"size5")

        layout12.addWidget(self.size5,5,1)

        self.partition10 = QComboBox(0,self.stepPartMountpoints,"partition10")

        layout12.addWidget(self.partition10,10,2)

        self.size9 = QLabel(self.stepPartMountpoints,"size9")

        layout12.addWidget(self.size9,9,1)

        self.partition3 = QComboBox(0,self.stepPartMountpoints,"partition3")

        layout12.addWidget(self.partition3,3,2)

        self.size1 = QLabel(self.stepPartMountpoints,"size1")

        layout12.addWidget(self.size1,1,1)

        self.textLabel3 = QLabel(self.stepPartMountpoints,"textLabel3")

        layout12.addWidget(self.textLabel3,0,0)

        self.textLabel5 = QLabel(self.stepPartMountpoints,"textLabel5")

        layout12.addWidget(self.textLabel5,0,2)

        self.partition2 = QComboBox(0,self.stepPartMountpoints,"partition2")

        layout12.addWidget(self.partition2,2,2)

        self.mountpoint4 = QComboBox(0,self.stepPartMountpoints,"mountpoint4")
        self.mountpoint4.setEditable(1)

        layout12.addWidget(self.mountpoint4,4,0)

        self.partition1 = QComboBox(0,self.stepPartMountpoints,"partition1")

        layout12.addWidget(self.partition1,1,2)

        self.size7 = QLabel(self.stepPartMountpoints,"size7")

        layout12.addWidget(self.size7,7,1)

        self.mountpoint10 = QComboBox(0,self.stepPartMountpoints,"mountpoint10")
        self.mountpoint10.setEditable(1)

        layout12.addWidget(self.mountpoint10,10,0)

        self.mountpoint3 = QComboBox(0,self.stepPartMountpoints,"mountpoint3")
        self.mountpoint3.setEditable(1)

        layout12.addWidget(self.mountpoint3,3,0)

        self.mountpoint7 = QComboBox(0,self.stepPartMountpoints,"mountpoint7")
        self.mountpoint7.setEditable(1)

        layout12.addWidget(self.mountpoint7,7,0)

        self.mountpoint9 = QComboBox(0,self.stepPartMountpoints,"mountpoint9")
        self.mountpoint9.setEditable(1)

        layout12.addWidget(self.mountpoint9,9,0)

        self.size3 = QLabel(self.stepPartMountpoints,"size3")

        layout12.addWidget(self.size3,3,1)

        self.mountpoint5 = QComboBox(0,self.stepPartMountpoints,"mountpoint5")
        self.mountpoint5.setEditable(1)

        layout12.addWidget(self.mountpoint5,5,0)

        self.mountpoint6 = QComboBox(0,self.stepPartMountpoints,"mountpoint6")
        self.mountpoint6.setEditable(1)

        layout12.addWidget(self.mountpoint6,6,0)

        self.size6 = QLabel(self.stepPartMountpoints,"size6")

        layout12.addWidget(self.size6,6,1)

        self.partition9 = QComboBox(0,self.stepPartMountpoints,"partition9")

        layout12.addWidget(self.partition9,9,2)

        stepPartMountpointsLayout.addLayout(layout12,1,1)

        self.mount_help = QLabel(self.stepPartMountpoints,"mount_help")
        self.mount_help.setAlignment(QLabel.WordBreak | QLabel.AlignVCenter)

        stepPartMountpointsLayout.addMultiCellWidget(self.mount_help,1,2,0,0)

        self.textLabel1_4 = QLabel(self.stepPartMountpoints,"textLabel1_4")

        stepPartMountpointsLayout.addMultiCellWidget(self.textLabel1_4,0,0,0,1)
        self.widgetStack.addWidget(self.stepPartMountpoints,7)

        self.stepReady = QWidget(self.widgetStack,"stepReady")
        stepReadyLayout = QGridLayout(self.stepReady,1,1,11,6,"stepReadyLayout")

        self.line2 = QFrame(self.stepReady,"line2")
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)
        self.line2.setFrameShape(QFrame.HLine)

        stepReadyLayout.addMultiCellWidget(self.line2,1,1,0,1)

        self.textLabel8 = QLabel(self.stepReady,"textLabel8")

        stepReadyLayout.addWidget(self.textLabel8,3,0)
        spacer35 = QSpacerItem(501,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        stepReadyLayout.addItem(spacer35,3,1)

        self.textLabel6 = QLabel(self.stepReady,"textLabel6")

        stepReadyLayout.addMultiCellWidget(self.textLabel6,0,0,0,1)

        self.textLabel7 = QLabel(self.stepReady,"textLabel7")

        stepReadyLayout.addMultiCellWidget(self.textLabel7,2,2,0,1)

        self.ready_textview = QTextEdit(self.stepReady,"ready_textview")

        stepReadyLayout.addMultiCellWidget(self.ready_textview,4,4,0,1)
        self.widgetStack.addWidget(self.stepReady,8)

        EspressoUILayout.addMultiCellWidget(self.widgetStack,2,2,0,3)

        self.languageChange()

        self.resize(QSize(620,552).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(i18n("Form1"))
        self.textLabel.setText(i18n("<span foreground=\"#9F6C49\"> <span foreground=\"white\" background=\"#9F6C49\"><b>Intro</b></span> > <b style=\"color: red\">Identification</b> > <b>Disk space</b> > <b>Installation</b> > <b>Ready!</b></span>"))
        self.backButton.setText(i18n("< Back"))
        self.nextButton.setText(i18n("Next >"))
        self.cancelButton.setText(i18n("Cancel"))
        self.introLabel.setText(i18n("textLabel2"))
        self.language_treeview.header().setLabel(0,i18n("Language"))
        self.textLabel1_2.setText(i18n("<b>Welcome</b>"))
        self.textLabel2_3.setText(i18n("Ready to install? Once you answer a few questions, Ubuntu can be installed on this computer so you can run the system at full speed and without the CD.\n"
"\n"
"Answering the questions should only take a few minutes."))
        self.textLabel4.setText(i18n("Specifying your location helps achieve faster downloads, and accurate number and currency settings."))
        self.textLabel2.setText(i18n("Nearest city:"))
        self.textLabel3_2.setText(i18n("Time zone:"))
        self.timezone_zone_text.setText(QString.null)
        self.textLabel1.setText(i18n("<h2>Where are you?</h2>"))
        self.textLabel1_3_2.setText(i18n("Some text (keyboard configurator goes here)"))
        self.warning_info.setText(QString.null)
        self.ident_label_3.setText(i18n("<h2>Identify yourself and your computer</h2>"))
        self.textLabel4_2.setText(i18n("<b>Computer Data</b>"))
        self.hostname_label1_2.setText(i18n("Hostname:"))
        self.pasword_label1_2.setText(i18n("Password"))
        self.username_label1_2.setText(i18n("User name:"))
        self.verified_label_2.setText(i18n("Verify Password:"))
        self.fullname_label1_2.setText(i18n("Real Name:"))
        self.user_label_2_2.setText(i18n("<b>Personal Data</b>"))
        self.partition_label2.setText(i18n("<b>How do you want to partition the disk?</b>"))
        self.drives_label2.setText(i18n("<b>Disk drives available:</b>"))
        self.textLabel2_2.setText(i18n("<h2>Please prepare some space for your new system</h2>"))
        self.new_size_label.setText(i18n("New partition size:"))
        self.textLabel6_2.setText(i18n("<h2>Please prepare some space for your new system</h2>"))
        self.textLabel7_2.setText(i18n("You have to make room in one or more of your hard disks in order to have GNU/Linux properly installed. 2 partitions are necessary:\n"
"· The root partition (“/”), with a minimum size of 1.5 GB.\n"
"· The swap partition (“swap”), with 256 MB or more.\n"
"You can now modify your existing partition table and select where you want what.\n"
"Remember that you can keep the data in a previous home partition – just leave it as it is and it will not be formatted.\n"
"Alternatively, it is possible to return to the previous page to select an easier partitioning method."))
        self.msg_error2.setText(i18n("You must supply a <b>\"/\"</b> mount point for your installed system."))
        self.mountpoint8.clear()
        self.mountpoint8.insertItem(QString.null)
        self.mountpoint8.insertItem(i18n("swap"))
        self.mountpoint8.insertItem(i18n("/"))
        self.mountpoint8.insertItem(i18n("/home"))
        self.mountpoint8.insertItem(i18n("/boot"))
        self.mountpoint8.insertItem(i18n("/usr"))
        self.mountpoint8.insertItem(i18n("/var"))
        self.size4.setText(QString.null)
        self.size2.setText(QString.null)
        self.mountpoint1.clear()
        self.mountpoint1.insertItem(QString.null)
        self.mountpoint1.insertItem(i18n("swap"))
        self.mountpoint1.insertItem(i18n("/"))
        self.mountpoint1.insertItem(i18n("/home"))
        self.mountpoint1.insertItem(i18n("/boot"))
        self.mountpoint1.insertItem(i18n("/usr"))
        self.mountpoint1.insertItem(i18n("/var"))
        self.mountpoint2.clear()
        self.mountpoint2.insertItem(QString.null)
        self.mountpoint2.insertItem(i18n("swap"))
        self.mountpoint2.insertItem(i18n("/"))
        self.mountpoint2.insertItem(i18n("/home"))
        self.mountpoint2.insertItem(i18n("/boot"))
        self.mountpoint2.insertItem(i18n("/usr"))
        self.mountpoint2.insertItem(i18n("/var"))
        self.textLabel4_2_2.setText(i18n("<b>Size</b>"))
        self.size10.setText(QString.null)
        self.size8.setText(QString.null)
        self.size5.setText(QString.null)
        self.size9.setText(QString.null)
        self.size1.setText(QString.null)
        self.textLabel3.setText(i18n("<b>Mountpoint</b>"))
        self.textLabel5.setText(i18n("<b>Partition</b>"))
        self.mountpoint4.clear()
        self.mountpoint4.insertItem(QString.null)
        self.mountpoint4.insertItem(i18n("swap"))
        self.mountpoint4.insertItem(i18n("/"))
        self.mountpoint4.insertItem(i18n("/home"))
        self.mountpoint4.insertItem(i18n("/boot"))
        self.mountpoint4.insertItem(i18n("/usr"))
        self.mountpoint4.insertItem(i18n("/var"))
        self.size7.setText(QString.null)
        self.mountpoint10.clear()
        self.mountpoint10.insertItem(QString.null)
        self.mountpoint10.insertItem(i18n("swap"))
        self.mountpoint10.insertItem(i18n("/"))
        self.mountpoint10.insertItem(i18n("/home"))
        self.mountpoint10.insertItem(i18n("/boot"))
        self.mountpoint10.insertItem(i18n("/usr"))
        self.mountpoint10.insertItem(i18n("/var"))
        self.mountpoint3.clear()
        self.mountpoint3.insertItem(QString.null)
        self.mountpoint3.insertItem(i18n("swap"))
        self.mountpoint3.insertItem(i18n("/"))
        self.mountpoint3.insertItem(i18n("/home"))
        self.mountpoint3.insertItem(i18n("/boot"))
        self.mountpoint3.insertItem(i18n("/usr"))
        self.mountpoint3.insertItem(i18n("/var"))
        self.mountpoint7.clear()
        self.mountpoint7.insertItem(QString.null)
        self.mountpoint7.insertItem(i18n("swap"))
        self.mountpoint7.insertItem(i18n("/"))
        self.mountpoint7.insertItem(i18n("/home"))
        self.mountpoint7.insertItem(i18n("/boot"))
        self.mountpoint7.insertItem(i18n("/usr"))
        self.mountpoint7.insertItem(i18n("/var"))
        self.mountpoint9.clear()
        self.mountpoint9.insertItem(QString.null)
        self.mountpoint9.insertItem(i18n("swap"))
        self.mountpoint9.insertItem(i18n("/"))
        self.mountpoint9.insertItem(i18n("/home"))
        self.mountpoint9.insertItem(i18n("/root"))
        self.mountpoint9.insertItem(i18n("/usr"))
        self.mountpoint9.insertItem(i18n("/var"))
        self.size3.setText(QString.null)
        self.mountpoint5.clear()
        self.mountpoint5.insertItem(QString.null)
        self.mountpoint5.insertItem(i18n("swap"))
        self.mountpoint5.insertItem(i18n("/"))
        self.mountpoint5.insertItem(i18n("/home"))
        self.mountpoint5.insertItem(i18n("/boot"))
        self.mountpoint5.insertItem(i18n("/usr"))
        self.mountpoint5.insertItem(i18n("/var"))
        self.mountpoint6.clear()
        self.mountpoint6.insertItem(QString.null)
        self.mountpoint6.insertItem(i18n("swap"))
        self.mountpoint6.insertItem(i18n("/"))
        self.mountpoint6.insertItem(i18n("/home"))
        self.mountpoint6.insertItem(i18n("/boot"))
        self.mountpoint6.insertItem(i18n("/usr"))
        self.mountpoint6.insertItem(i18n("/var"))
        self.size6.setText(QString.null)
        self.mount_help.setText(i18n("Now you should have at least 2 GNU/Linux partitions with space enough. It's time to specify where you want every component to be installed.\n"
"Proceed as follows: select one partition in the column on the left and link it with one mount point on the right. Repeat for every desired partition.\n"
"There are 2 necessary “mount points” – they must be associated with 2 partitions. They are “/” and “swap”.\n"
"If you kept an intact home partition, you can now link it with the “/home” mount point. It will not be formatted, so data is preserved."))
        self.textLabel1_4.setText(i18n("<h2>Please prepare some space for your new system</h2>"))
        self.textLabel8.setText(i18n("Details"))
        self.textLabel6.setText(i18n("<h2>Ready to install</h2>"))
        self.textLabel7.setText(i18n("Kubuntu is ready to install on this computer."))

