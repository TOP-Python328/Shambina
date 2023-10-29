binary_num = input()
prefix = "0b"
is_binary = True

if binary_num[1] == "b":
    prefix = binary_num[0:2]
    binary_num = binary_num[2:]

if binary_num[0] == "b":
    binary_num = binary_num[1:]
    
if not prefix == "0b":
    is_binary = False
    
binary_set = set(int(digit) for digit in binary_num)

bin_set = {0, 1}
if not (binary_set <= bin_set):
    is_binary = False
    
if is_binary:
    print("да")
else:
    print("нет")

# 0101
# да

# b11
# да

# 0b11001
# да

# 1b0101
# нет
