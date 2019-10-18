# A module that allows you allow to use random features
import random
 
# A list of characters
letters = ["a", "b", "c", "d", "e",
"f", "g", "h", "i", "j", "k",
"l", "m", "n", "o", "p", "q",
"r", "s", "t", "u", "v", "w",
"x", "y", "z", "A", "B", "C",
"D", "E", "F", "G", "H", "I",
"J", "K", "L", "M", "N", "O",
"P", "Q", "R", "S", "T", "U",
"V", "W", "X", "Y", "Z", "1",
"2", "3", "4", "5", "6", "7",
"8", "9", "0", "!", "£", "$",
"%", "*", "@", "#", "~", "&"]
 
# Initialises a variable to store the password
password = []
 
# Loops it for 8 times to generate an 8 character
# password.
for i in range(0,8):
 # Used to select an index from the list of letters
 # to make this random password
 num = random.randint(0,len(letters)-1)
 password.append(letters[num])

p = password[0]
a = password[1]
s = password[2]
s = password[3] 
w = password[4]
o = password[5]
r = password[6]
d = password[7]

random_password = p + a + s + s + w + o + r + d

# Displays the randomly generated password
print("Your randomly generated password is:", random_password)
