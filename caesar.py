#!/usr/bin/python

import sys, string, codecs

print ("This is the encoder. To decipher a message, use the provided decoder.")

# Check if there was a file provided to encode, or if we should await input from the user?
if len(sys.argv) > 1:
    string = open(sys.argv[1], 'r').read().decode("utf-8")
    print ("\n\nUsing file input for encoding.")
    file = 1
else:
    string = raw_input("\n\nPlease enter the phrase to encode: ")

print ("Use base64, hex, uu, quopri, rot13 or none as encoding types.")

stage = 0
values = ('base64', 'hex', 'uu', 'quopri', 'rot13', 'none')
choice = ('yes', 'no')
matrix = {'10100': 'base64', '10010': 'hex', '10001': 'uu', '01100': 'quopri', '01010': 'rot13', '01001': 'none'}

# Creating loops to let the user choose what encoding method they'd like to use
# TODO Merge all 4 loops into one loop to optimize
while stage < 1:
    enc1 = raw_input("Please define encoding 1/4: ")
    if enc1 in values:
	if enc1 != "none":
	    print ("Encoding selected: ") + enc1
	    enc1d = string.encode(enc1, 'strict')
	else:
	    print ("No algorithm selected in stage 1, skip encoding.")
	    enc1d = string
	stage = stage + 1
	# Generate a Key value (kn) for automated decoding through cleopatra
	for key, value in matrix.items():
	    if value == enc1:
		k1 = key
    else:
	print ("I\'m sorry, you entered a wrong value.\nPlease make sure to use the correct value.\n")

while stage < 2:
    enc2 = raw_input("\n\nPlease define encoding 2/4: ")
    if enc2 in values:
        if enc2 != "none":
            print ("Encoding selected: ") + enc2
            enc2d = enc1d.encode(enc2, 'strict')
        else:
            print ("No algorithm selected in stage 2, skip encoding.")
            enc2d = enc1d
        stage = stage + 1
        for key, value in matrix.items():
	    if value == enc2:
		k2 = key
    else:
        print ("I\'m sorry, you entered a wrong value.\nPlease make sure to use the correct value.\n")

while stage < 3:
    enc3 = raw_input("\n\nPlease define encoding 3/4: ")
    if enc3 in values:
        if enc3 != "none":
            print ("Encoding selected: ") + enc3
            enc3d = enc2d.encode(enc3, 'strict')
        else:
            print ("No algorithm selected in stage 3, skip encoding.")
            enc3d = enc2d
        stage = stage + 1
        for key, value in matrix.items():
	    if value == enc3:
		k3 = key
    else:
        print ("I\'m sorry, you entered a wrong value.\nPlease make sure to use the correct value.\n")

while stage < 4:
    enc4 = raw_input("\n\nPlease define encoding 4/4: ")
    if enc4 in values:
        if enc4 != "none":
            print ("Encoding selected: ") + enc4
            enc4d = enc3d.encode(enc4, 'strict')
        else:
            print ("No algorithm selected in stage 4, skip encoding.")
            enc4d = enc3d
        stage = stage + 1
        for key, value in matrix.items():
	    if value == enc4:
		k4 = key
    else:
        print ("I\'m sorry, you entered a wrong value.\nPlease make sure to use the correct value.\n")

# Encode to base64 so we can more easily shift characters, no matter the last encoding chosen by the user
pre_salt = enc4d.encode('base64', 'strict')

# Last but not least, let's add a little salt to obscure the encoding even further
# The chosen offset has to be known by the receipient of the message to decode it
saltq = raw_input("\n\nDo you want to create a character-offset for the message?\n(yes/no): ")

if saltq in choice:
    if saltq == "yes":
        value_in_range = 0
        while value_in_range < 1:
            salt = int(raw_input("Please provide an offset value (1-32): "))
            if salt in range(1, 33):
                print ("\n\nWARNING!\n\nEncoding might take up a lot of resources, if a high offset was chosen.\n\n")
                # This loop will check if the correct_value is smaller than the value provided in salt
                # If it is, it will keep using rot13 and then base64 to encode the string until correct_value = salt
                correct_value = 0
                while correct_value < salt:
                    correct_value = correct_value + 1
                    print ("Crunching... ") + repr(correct_value) + ("/") + repr(salt)
                    pre_salt = pre_salt.encode('rot13').encode('base64')
                print ("\n\nAll done!\n\n")
                salted = pre_salt
                value_in_range = 1
                k5 = eval(repr(bin(salt)))
                key = k5 + ' ' + k4 + ' ' + k3 + ' ' + k2 + ' ' + k1
            else:
                print ("Your value did not meet the criteria: ") + repr(salt)
                print ("Please choose an offset value between 1-32.")
    else:
        salted = pre_salt
        key = k4 + ' ' + k3 + ' ' + k2 + ' ' + k1

# Ask the user wether the file should be saved or not
confirmed = 0

while confirmed < 1:
    save_as = raw_input("Do you want to save the message as a file?\n(yes/no): ")
    if save_as in choice:
        if save_as == "yes":
            file = 1
        else:
	    file = 0
    confirmed = 1
if file == 1:
    save = raw_input("Please choose a filename: ")
    savekey = save + '-key'
    print >> open(save, 'w'), salted
    print >> open(savekey, 'w'), key
else:
    print ("This is your encrypted message:\n\n") + salted
    print ("This is the key for decryption:\n\n") + key
