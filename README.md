cipher
======

An encoder and decoder written in Python 2.7.

Usage
======

To encrypt a message you'd use:
  python caesar.py

You can also specify to encrypt a text-file with:
  python caesar.py filename.txt
  
To decrypt a file you'd use:
  python cleopatra.py
  
You can also specify to decrypt a text-file with:
  python cleopatra.py filename.txt

Known Bugs
======

When using the program under Windows (any version) and you only have Python 3 or newer installed, it will not be able to handle all the functionality, as some is still using Python 2.x syntax. I'm going to fix that soon, so it will be able to run under Windows just as it would under OS X or Linux.
