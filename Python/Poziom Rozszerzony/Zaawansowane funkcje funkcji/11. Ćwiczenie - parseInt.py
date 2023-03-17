import re
def parseInt(x, / ,base=10, * ,changeEndianness=False):
    x = int(str(x), base)
    
    if changeEndianness:
        #converted num TO hex
        x = hex(x)[2:]
        if len(x) % 2 == 1:
            x = '0' + x
        
        #swapping    
        x = re.findall('..', x)
        x.reverse()
        x = ''.join(map(str, x))
        
        return int(x, 16)
    return x
    