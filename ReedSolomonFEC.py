from reedsolo import RSCodec
rs = RSCodec(10)

def encodeFEC(chrString):
    val = rs.encode(chrString)
    return val

def decodeFEC(decodeVal):
    nval = rs.decode(decodeVal)
    return nval


chrString = '1001100111'
val = encodeFEC(chrString)
print val
newVal = decodeFEC(val)

