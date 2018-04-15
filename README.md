# RansomwareDemo

based on https://github.com/deadPix3l/CryptSky

## Build .exe-file using pyinstaller
demo without options (encrypting everything in c:\temp)
```
pyinstaller build_danger.spec
```
demo
```
pyinstaller build.spec
```

## Run exe (without options)
```
C:\danger.exe
This is a demo ransomware. Basically it only encrypts files from a specific dire
ctory. If you accidently encryptedimportant files, just run this script again! T
o really encrypt files, use the -d parameter!
Encryption Key is: b'PAYMESOMERANSOM!'


Encrypting file C:\Temp\test_0.bak
Encrypting file C:\Temp\test_0.json
Encrypting file C:\Temp\test_1.json
Encrypting file C:\Temp\test_1.odt
Encrypting file C:\Temp\test_2.odp
Encrypting file C:\Temp\test_2.xml
Encrypting file C:\Temp\test_3.json
Encrypting file C:\Temp\test_3.ppt
Encrypting file C:\Temp\test_4.md
Encrypting file C:\Temp\test_4.rtf
Encrypting file C:\Temp\test_5.docx
Encrypting file C:\Temp\test_5.go
Encrypting file C:\Temp\test_6.docx
Encrypting file C:\Temp\test_6.odp
Encrypting file C:\Temp\test_7.go
Encrypting file C:\Temp\test_7.rtf
Encrypting file C:\Temp\test_8.md
Encrypting file C:\Temp\test_8.yaml
Encrypting file C:\Temp\test_9.bak
Encrypting file C:\Temp\test_9.pyc
```

## Run exe (with options)
```
C:\Users\>ransomware.exe
usage: ransomware.exe [-h] -c CONFIG [-g] [-d]
ransomware.exe: error: the following arguments are required: -c/--config

C:\Users\>ransomware.exe -c ../settings.cfg
This is a demo ransomware. Basically it only encrypts files from a specific dire
ctory. If you accidently encryptedimportant files, just run this script again! T
o really encrypt files, use the -d parameter!
Encryption Key is: b'PAYMESOMERANSOM!'


WOULD encrypt file C:\Temp\test_0.bak
WOULD encrypt file C:\Temp\test_0.json
WOULD encrypt file C:\Temp\test_1.json
WOULD encrypt file C:\Temp\test_1.odt
WOULD encrypt file C:\Temp\test_2.odp
WOULD encrypt file C:\Temp\test_2.xml
WOULD encrypt file C:\Temp\test_3.json
WOULD encrypt file C:\Temp\test_3.ppt
WOULD encrypt file C:\Temp\test_4.md
WOULD encrypt file C:\Temp\test_4.rtf
WOULD encrypt file C:\Temp\test_5.docx
WOULD encrypt file C:\Temp\test_5.go
WOULD encrypt file C:\Temp\test_6.docx
WOULD encrypt file C:\Temp\test_6.odp
WOULD encrypt file C:\Temp\test_7.go
WOULD encrypt file C:\Temp\test_7.rtf
WOULD encrypt file C:\Temp\test_8.md
WOULD encrypt file C:\Temp\test_8.yaml
WOULD encrypt file C:\Temp\test_9.bak
WOULD encrypt file C:\Temp\test_9.pyc

C:\Users\>ransomware.exe -c ../settings.cfg -g
Generating file C:\Temp\test_0.doc
Generating file C:\Temp\test_1.xlsx
Generating file C:\Temp\test_2.go
Generating file C:\Temp\test_3.ods
Generating file C:\Temp\test_4.xls
Generating file C:\Temp\test_5.bak
Generating file C:\Temp\test_6.md
Generating file C:\Temp\test_7.docx
Generating file C:\Temp\test_8.ppt
Generating file C:\Temp\test_9.py

C:\Users\>ransomware.exe -c ../settings.cfg -d
This is a demo ransomware. Basically it only encrypts files from a specific dire
ctory. If you accidently encryptedimportant files, just run this script again! T
o really encrypt files, use the -d parameter!
Encryption Key is: b'PAYMESOMERANSOM!'


Encrypting file C:\Temp\test_0.bak
Encrypting file C:\Temp\test_0.doc
Encrypting file C:\Temp\test_0.json
Encrypting file C:\Temp\test_1.json
Encrypting file C:\Temp\test_1.odt
Encrypting file C:\Temp\test_1.xlsx
Encrypting file C:\Temp\test_2.go
Encrypting file C:\Temp\test_2.odp
Encrypting file C:\Temp\test_2.xml
Encrypting file C:\Temp\test_3.json
Encrypting file C:\Temp\test_3.ods
Encrypting file C:\Temp\test_3.ppt
Encrypting file C:\Temp\test_4.md
Encrypting file C:\Temp\test_4.rtf
Encrypting file C:\Temp\test_4.xls
Encrypting file C:\Temp\test_5.bak
Encrypting file C:\Temp\test_5.docx
Encrypting file C:\Temp\test_5.go
Encrypting file C:\Temp\test_6.docx
Encrypting file C:\Temp\test_6.md
Encrypting file C:\Temp\test_6.odp
Encrypting file C:\Temp\test_7.docx
Encrypting file C:\Temp\test_7.go
Encrypting file C:\Temp\test_7.rtf
Encrypting file C:\Temp\test_8.md
Encrypting file C:\Temp\test_8.ppt
Encrypting file C:\Temp\test_8.yaml
Encrypting file C:\Temp\test_9.bak
Encrypting file C:\Temp\test_9.py
Encrypting file C:\Temp\test_9.pyc
```

