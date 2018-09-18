import bz2, sys

file_in = sys.argv[1]
file_out = sys.argv[2]

with bz2.open(file_in, 'r') as f:
    data = f.read() 
    print(data)
    
    