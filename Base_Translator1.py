import math

base = 0.5
while base % 1 != 0 or base < 2 or base > 36:
    base = input(print("Please choose an integer base from 2 - 36, inclusive. "))
    base = float(base)
base = int(base)


                 
num_original = 0.5
while num_original % 1 != 0 or  num_original < 1:
     num_original = input(print("Please choose a positive integer to convert to base %s. " % base))
     num_original = float(num_original)
num_original = int(num_original)



parts_list = []
index_list = []
append_count = 0
counter = 0
char_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
used_char_list = []

while num_original != 0:
    place_val = 0
    while base ** place_val <= num_original:
        place_val = place_val + 1
    place_val = place_val - 1

    part = base ** place_val
    parts_list.append(part)
    append_count = append_count + 1
    num_original = num_original - part


leading_val = parts_list[0]
digits = math.log(leading_val, base)
new_digits = int(digits + 1)

while digits >= 0:
    for i in range (0, append_count):
        if parts_list[i] == base ** digits:
            counter = counter + 1
        else:
            counter = counter + 0

    index_list.append(counter)
    counter = 0
    digits = digits - 1

for i in range (0, new_digits):
    if index_list[i] == 10:
        index_list[i] = "a"
    elif index_list[i] == 11:
        index_list[i] = "b"
    elif index_list[i] == 12:
        index_list[i] = "c"
    elif index_list[i] == 13:
        index_list[i] = "d"
    elif index_list[i] == 14:
        index_list[i] = "e"
    elif index_list[i] == 15:
        index_list[i] = "f"
    elif index_list[i] == 16:
        index_list[i] = "g"
    elif index_list[i] == 17:
        index_list[i] = "h"
    elif index_list[i] == 18:
        index_list[i] = "i"
    elif index_list[i] == 19:
        index_list[i] = "j"
    elif index_list[i] == 20:
        index_list[i] = "k"
    elif index_list[i] == 21:
        index_list[i] = "l"
    elif index_list[i] == 22:
        index_list[i] = "m"
    elif index_list[i] == 23:
        index_list[i] = "n"
    elif index_list[i] == 24:
        index_list[i] = "o"
    elif index_list[i] == 25:
        index_list[i] = "p"
    elif index_list[i] == 26:
        index_list[i] = "q"
    elif index_list[i] == 27:
        index_list[i] = "r"
    elif index_list[i] == 28:
        index_list[i] = "s"
    elif index_list[i] == 29:
        index_list[i] = "t"
    elif index_list[i] == 30:
        index_list[i] = "u"
    elif index_list[i] == 31:
        index_list[i] = "v"
    elif index_list[i] == 32:
        index_list[i] = "w"
    elif index_list[i] == 33:
        index_list[i] = "x"
    elif index_list[i] == 34:
        index_list[i] = "y"
    elif index_list[i] == 35:
        index_list[i] = "z"
    else:
        index_list[i] = str(index_list[i])
                   

new_num = "".join(index_list)
print(new_num)

library = input(print("If you would like a map of each character's value, type 'map'. If not, type anything else. "))
library = library.lower()

if library == "map":
    for i in range (0, base):
        x = char_list[i]
        used_char_list.append(x)
        
    print("Character --> Value")

    for i in range(0, base):   
        x = used_char_list[i]
        print("%s --> %s" % (x, i))
    print("")
    print("Thank You for using this program")
else:
    print("Thank You for using this program")
    












