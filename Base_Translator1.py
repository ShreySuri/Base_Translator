import math

base = 13
clock = 84739



parts_list = []
index_list = []
append_count = 0
counter = 0
num_original = clock

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
    else:
        index_list[i] = str(index_list[i])
                   
new_num = "".join(index_list)
print(new_num)













