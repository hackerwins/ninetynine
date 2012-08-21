def decodeModified(l):
  return ''.join([i[0]*i[1] if type(i) == list else i for i in l])
  
print decodeModified([[4,"a"],"b",[2,"c"],[2,"a"],"d",[4,"e"]])
