# DataConverter
I needed a tool that would convert data sizes.  It was a good candidate to put up.

# Usage

First arguement will always be what the current data size level is in:
    pages = p
    kb = k
    mb = m
    gb = g
    tb = t
    pb = pb
    
 any number values after that will be summed, then output to 4 conversions + the current data size level. 

 You can also mix and repeat arguments!  
 
 p num num k num num pb 1 p num num num k num ...

 This makes the tool more versitile than originally implemented. 
 
# Example
 
 p 100 200 300 k 400 250 512 pb 1 g 400 25 p 50000

 will yield:


Bytes : 1126356662822912.0

Pages : 137494709817.25

Kilobytes : 1099957678538.0

Megabytes : 1074177420.4472656

Gigabytes : 1049001.3871555328

Terabytes : 1024.415417144075

Petabytes : 1.0004056808047608





 



