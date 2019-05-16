# DataConverter
I needed a tool that would convert data sizes.  It was a good candidate to put up.


added the zip file from pyinstaller for space.py.  Working EXE inside.

# Usage

First arguement will always be what the current data size level is in:
    pages = p
    kb = k
    mb = m
    gb = g
    tb = t
    
 any number values after that will be summed, then output to 4 conversions + the current data size level
 
 # Example
 
 p 100 200 300




 will output:


pages = 600.0


kb = 4800.0


mb = 4.6875


gb = 0.00457763671875


tb = 4.470348358154297e-06




t 1.5




will output:


pages = 201326592.0


kb = 1610612736.0


mb = 1572864.0


gb = 1536.0


tb = 1.5
