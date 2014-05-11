#!/usr/bin/python

# importing some modules
import sys
import argparse
import os
import time
import binascii
import base64

# add parsing functionality to provide files
parser = argparse.ArgumentParser(description="Caesar: a command line key based encryption tool",
                                 epilog='''This is very basic-level encryption and will probably not keep you safe from
                                 the NSA or other high-level organizations. Use with caution and common sense.''')
parser.add_argument("-m", "--mode", dest="mode", help="specify whether encryption, or decryption should be used",
                    metavar="encrypt|decrypt")
parser.add_argument("-f", "--file", dest="filename", help="file to be used for encryption",
                    metavar="filename")
parser.add_argument("-k", "--key", dest="keyfile", help="keyfile to be used for decryption",
                    metavar="filename")
args = parser.parse_args()


# redefine encoding functions for easier use
def tobase(n):
    return base64.encodestring(n)


def unbase(n):
    return base64.decodestring(n)


def tohex(n):
    return binascii.hexlify(n)


def unhex(n):
    return binascii.unhexlify(n)


# prints the 1337 intro message
# bitches love 1337 intro messages
print(
    '''\n  ,---. ,--,--. ,---.  ,---.  ,--,--.,--.--.
 | .--'' ,-.  || .-. :(  .-' ' ,-.  ||  .--'
 \\ `--.\\ '-'  |\\   --..-'  `)\\ '-'  ||  |
   `---' `--`--' `----'`----'  `--`--'`--''''')
print("\n        =========================")
print("        Key based encryption tool")
print("        =========================")


# function is called, when "encrypt" was passed through args.mode
def encrypt():
    # probe whether a file to encrypt was provided or not
    if args.filename:
        m = open(args.filename, 'r').read()
    else:
        m = raw_input("\nWhat should I encrypt?\n>>> ")

    # assign other variables to be used for encryption
    k = raw_input("\nWhat should I use as a password?\n>>> ")
    print ("k " + k)
    r = len(k)
    print ("r " + str(r))
    bm = tohex(m)
    #bm = m.encode('hex')
    print("bm " + bm)  # TODO: delete line once code works
    bk = tohex(k)
    #bk = k.encode('hex')
    print("bk " + bk)  # TODO: delete line once code works
    w = len(bm)
    print("w " + repr(w))  # TODO: delete line once code works
    nl = bm[0:0 + w // 2]
    print("nl " + nl)  # TODO: delete line once code works
    nr = bm[0 + w // 2:]
    print("nr " + nr)  # TODO: delete line once code works
    #test1 = int(bk) ^ int(nl)
    #test1 = str(test1).encode('base64')
    #test2 = test1.encode('rot13')
    #test3 = test2.encode('hex')

    if r > 7:
        print("\nEncryption might take a while, depending on the length and complexity of the password.\n")
    if r > 12:
        r = 12
    for i in range(r):
        print("Round " + str(i + 1) + " of " + str(r))
        # manipulate left split
        nl = str(int(bk, 16) ^ int(nl, 16))
        print("xor links " + str(nl))  # TODO: delete line once code works
        #nl = tohex(tobase(nl).encode('rot13'))
        #nl = nl.encode('base64').encode('rot13').encode('hex')
        #print("encode links " + str(nl))  # TODO: delete line once code works
        # manipulate right split
        nr = str(int(bk, 16) ^ int(nr, 16))
        print("xor rechts " + str(nr))  # TODO: delete line once code works
        #nr = tohex(tobase(nr).encode('rot13'))
        #nr = nr.encode('base64').encode('rot13').encode('hex')
        #print("encode rechts " + str(nr))  # TODO: delete line once code works

    print(nl)  # TODO: delete line once code works
    print(nr)  # TODO: delete line once code works
    cipher = nl + nr
    #cipher = cipher.encode('base64')  # TODO: uncomment code once process works
    bk = bk.encode('base64').encode('rot13').encode('base64')

    # provide different values for enc_filename depending on
    # whether or not we used a file for encryption
    if args.filename:
        enc_filename = os.path.splitext(args.filename)
        enc_filename = enc_filename[0]
    else:
        timefile = time.strftime("%Y%m%d%H%M%S")
        prefile = "caesar-"
        enc_filename = prefile + timefile
    key_filename = enc_filename + "-key.txt"
    enc_filename += "-encrypted.txt"

    #print >> open("debug", 'w'), test1 + test2 + test3
    print >> open(enc_filename, 'w'), cipher
    print >> open(key_filename, 'w'), bk
    print("\nAll done. Following files were created:")
    print(enc_filename + ", " + key_filename)


# function is called, when "decrypt" was passed through args.mode
def decrypt():
    # probe whether a file to decrypt was provided or not
    if args.filename:
        cipher = open(args.filename, 'r').read()
    else:
        cipher = raw_input("\nWhat should I decrypt?\n>>> ")

    # probe whether a key for decryption was provided or not
    if args.keyfile:
        bk = open(args.keyfile, 'r').read()
    else:
        bk = raw_input("\nPlease enter the encrypted password.\n>>> ")

    #cipher = cipher.decode('base64')  # TODO: uncomment code once process works
    bk = bk.decode('base64').decode('rot13').decode('base64')
    print(bk)  # TODO: delete line once code works
    r = len(bk.decode('hex'))
    w = len(cipher)
    print(w)  # TODO: delete line once code works
    nl = cipher[0:0 + w // 2]
    print("nl " + nl)  # TODO: delete line once code works
    nr = cipher[0 + w // 2:]
    print("nr " + nr)  # TODO: delete line once code works

    if r > 12:
        r = 12
    for i in range(r):
        print("Round " + str(i + 1) + " of " + str(r))
        # manipulate left split
        #nl = nl.decode('hex').decode('rot13').decode('base64')
        #print("encode links " + nl)  # TODO: delete line once code works
        nl = str(int(nl) ^ int(bk, 16))
        print("xor links " + str(nl))  # TODO: delete line once code works
        # manipulate right split
        #nr = nr.decode('hex').decode('rot13').decode('base64')
        #print(" encode rechts" + nr)  # TODO: delete line once code works
        nr = str(int(nr) ^ int(bk, 16))
        print("xor rechts " + str(nr))  # TODO: delete line once code works

        nl = nl.decode('hex')
        print("nl " + nl)  # TODO: delete line once code works
        nr = nr.decode('hex')
        print("nr " + nr)  # TODO: delete line once code works
        clear = nl + nr
        clear_filename = os.path.split(args.filename)
        clear_filename = clear_filename
        print(clear)
        print(clear_filename)


# function is called, when no mode was passed through args.mode
def nocrypt():
    print(('\nNo mode selected.\n'
           'Please specify a mode by using the following:\n'
           'caesar.py -m [encrypt | decrypt] \n'
           'Use -h for all available commands.'))


# check for what mode was selected
if args.mode == "encrypt":
    # use encryption protocol
    encrypt()
elif args.mode == "decrypt":
    # use decryption protocol
    decrypt()
else:
    # no mode selected
    nocrypt()
sys.exit()