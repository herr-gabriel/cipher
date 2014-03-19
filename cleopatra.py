#!/usr/bin/python

import sys, string, codecs

# This works exactly like caesar.py, except in reverse order

values = ('base64', 'hex', 'uu', 'quopri', 'rot13', 'none')
choice = ('yes', 'no')

print ("This is the decoder. To encrypt a message, use the provided encoder.")

# Check if there was a file provided to encode, or if we should await input from the user?
if len(sys.argv) > 1:
	str = open(sys.argv[1], 'r').read().decode("utf-8")
	print ("\n\nUsing file input for decoding.")
	file = 1
else:
	str = raw_input("\n\nPlease enter the phrase to decode: ")
	
# Check for a possible offset
offset_check = 0
while offset_check < 1:
	offset_used = raw_input("Was a character offset used?\n(yes/no): ")
	if offset_used in choice:
		offset_check = 1
		if offset_used == "yes":
			salt_in_range = 0
			while salt_in_range < 1:
				salt = int(raw_input("Please provide an offset value (1-32): "))
				if salt in range(1, 33):
					print ("\n\nWARNING!\n\nDecoding might take up a lot of resources, if a high offset was chosen.\n\n")
					# This loop will check if the correct_value is smaller than the value provided in salt
					# If it is, it will keep using rot13 and then base64 to encode the string until correct_value = salt
					correct_value = 0
					while correct_value < salt:
						correct_value = correct_value + 1
						print ("Crunching... ") + repr(correct_value) + ("/") + repr(salt)
						str = str.decode('base64').decode('rot13')
					print ("\n\nAll done!\n\n")
					untangled = str
					salt_in_range = 1
				else:
					print ("Your value did not meet the criteria: ") + repr(salt)
					print ("Please choose an offset value between 1-32.")

		else:
			print ("No offset used in encoding.")
			untangled = str
	else:
		print ("Please answer with yes or no.")
		
post_salt = untangled.decode('base64', 'strict')
		
# 4 loops to decode the message
stage = 0
while stage < 1:
    enc1 = raw_input("Please define decoding 1/4: ")
    if enc1 in values:
        if enc1 != "none":
            print ("Decoding selected: ") + enc1
            enc1d = post_salt.decode(enc1, 'strict')
        else:
            print ("No algorithm selected in stage 1, skip decoding.")
            enc1d = post_salt
        stage = stage + 1
    else:
        print ("I\'m sorry, you entered a wrong value.\nPlease make sure to use the correct value.\n")

while stage < 2:
    enc2 = raw_input("\n\nPlease define decoding 2/4: ")
    if enc2 in values:
        if enc2 != "none":
            print ("Decoding selected: ") + enc2
            enc2d = enc1d.decode(enc2, 'strict')
        else:
            print ("No algorithm selected in stage 2, skip decoding.")
            enc2d = enc1d
        stage = stage + 1
    else:
        print ("I\'m sorry, you entered a wrong value.\nPlease make sure to use the correct value.\n")

while stage < 3:
    enc3 = raw_input("\n\nPlease define decoding 3/4: ")
    if enc3 in values:
        if enc3 != "none":
            print ("Decoding selected: ") + enc3
            enc3d = enc2d.decode(enc3, 'strict')
        else:
            print ("No algorithm selected in stage 3, skip decoding.")
            enc3d = enc2d
        stage = stage + 1
    else:
        print ("I\'m sorry, you entered a wrong value.\nPlease make sure to use the correct value.\n")

while stage < 4:
    enc4 = raw_input("\n\nPlease define decoding 4/4: ")
    if enc4 in values:
        if enc4 != "none":
            print ("Decoding selected: ") + enc4
            decoded = enc3d.decode(enc4, 'strict')
        else:
            print ("No algorithm selected in stage 4, skip decoding.")
            decoded = enc3d
        stage = stage + 1
    else:
        print ("I\'m sorry, you entered a wrong value.\nPlease make sure to use the correct value.\n")

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
    print >> open(save, 'w'), decoded
else:
    print ("This is your encrypted message:\n\n") + decoded
