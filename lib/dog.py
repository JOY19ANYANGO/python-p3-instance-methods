#!/usr/bin/env python3

class Dog:
    def bark(self):
        print("Woof!")
        
    def sit(self):
        print("The dog is sitting.")

fido = Dog()
fido.bark()
fido.sit() 
# Woof!
# The dog is sitting.
snoopy = Dog()
snoopy.bark() 
snoopy.bark()
# Woof!
# The dog is sitting.