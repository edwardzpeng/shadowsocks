# Redirect attack on Shadowsocks stream ciphers

Shadowsocks is a secure split proxy loosely based on SOCKS5. It’s widely used in china.
I found a vulnerability in shadowsocks protocol which break the confidentiality of
shadowsocks stream cipher. A passive attacker can easily decrypt all the encrypted shadowsocks packet using our redirect attack. Even more, a man-in-the-middle attacker can modify traffic in real time like there is no encryption at all.

Details of the attack can be found in the pdf. And a POC can be found in the python code.

## Vulnerable versions
shadowsocks-py, shadowsocoks-go, go-shadowsocks2, shadowsocoks-nodejs

## Suggestions
Do not use : shadowsocks-py, shadowsocoks-go, shadowsocoks-nodejs.

Only Use: shadowsocks-libev, go-shadowsocks2 and only use the AEAD ciphers

## Credit
Zhiniang Peng (@edwardzpeng) of Qihoo 360 Core Security

## Timeline
28/12/2018: Vulnerability found

26/01/2019: Technique details upload

26/03/2019: POC upload 

12/02/2020: Published 
