#!/usr/bin/python

#
# Patch the binary in place: it want to dlopen stuff in /usr
#

def patch(file, address):
    exe.seek(address)
    value = exe.read(3)
    if value != b'usr':
        raise Exception("incorrect file")
    exe.seek(address)
    exe.write(b'app')

with open('/app/lib/x86_64-linux-gnu/epsonscan2/non-free-exec/es2intif', 'r+b') as exe:
    patch(exe, 0x20380 + 4)
    patch(exe, 0x20400 + 1)
