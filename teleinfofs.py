#!/usr/bin/env python

import sys
import teleinfo

from collections import defaultdict
from errno import ENOENT
from stat import S_IFDIR, S_IFLNK, S_IFREG
from time import time

from fusepy.fuse import FUSE, Operations, LoggingMixIn

class TeleinfoOperations(LoggingMixIn, Operations):
    def __init__(self, serialPort):
        self.ti = teleinfo.Teleinfo(serialPort)
        
        self.files = {}
        self.data = defaultdict(str)
        self.fd = 0
    
    def update(self):
        for etiquette, valeur in self.ti.read().items():
            path = "/%s" % etiquette
            
            if not self.data[path]:
                self.fd += 1
            
            self.data[path] = valeur            
            self.files[path] = dict(st_mode=(S_IFREG | 0444), st_nlink=1,
                st_size=len(valeur), st_ctime=time(), st_mtime=time(), st_atime=time())
        
    def getattr(self, path, fh=None):
        if path not in self.files:
            raise FuseError(ENOENT)
        st = self.files[path]
        if path == '/':
            # Add 2 for `.` and `..` , subtruct 1 for `/`
            st['st_nlink'] = len(self.files) + 1
        return st
    
    def init(self):
        mode = S_IFDIR | 0555
        now = time()
        self.files['/'] = dict(st_mode=mode, st_ctime=now, st_mtime=now,
                st_atime=now)
        
    def open(self, path, flags):
        self.update()
        self.fd += 1
        return self.fd
    
    def read(self, path, size, offset, fh):
        return self.data[path][offset:offset + size]
    
    def readdir(self, path, fh):
        self.update()
        return ['.', '..'] + [x[1:] for x in self.files if x != '/']

    def statvfs(self, path):
        return dict(f_bsize=512, f_blocks=4096, f_bavail=2048)
    
    def utimens(self, path, atime, mtime):
        now = time()
        self.files[path]['st_atime'] = atime or now
        self.files[path]['st_mtime'] = mtime or now
        return 0

if __name__ == "__main__":        
    #logging.basicConfig(level=logging.DEBUG)
    if len(sys.argv) == 3:
        fuse = FUSE(TeleinfoOperations(serialPort=sys.argv[1]), 
                    mountpoint=sys.argv[2], foreground=False,
                    fsname="TeleinfoFS", allow_other=True)
    else:
        print "Usage : %s <serialport> <mountpoint>\nExample : %s /dev/ttyS0 /mnt/teleinfo" % (sys.argv[0],sys.argv[0])