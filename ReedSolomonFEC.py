from reedsolo import RSCodec
rs = RSCodec(10)
chrString = '1001100111'
val = rs.encode(chrString)
print val

nval = rs.decode(val)
print nval



