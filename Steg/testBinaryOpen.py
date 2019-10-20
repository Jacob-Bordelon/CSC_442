fileToRead = raw_input()
#with open(fileToRead, 'rb') as f:
#   p = f.read(1)
#    print p, type(p)
#    res = ''.join(format(i, 'b') for i in bytearray(p, encoding ='utf-8')) 
#    print res
wrapper = open(fileToRead,'rb').read(8)
print type(wrapper),":\n",wrapper

res = bytearray(wrapper,encoding='base64')
print type(res),":\n",res
next = [format(i,'b') for i in res]
print type(next[0]),":\n",next
final = ''.join(next)
print type(final),":\n",final
