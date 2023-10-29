num_and_str = "1"
my_list = []
line = []

while num_and_str:
    num_and_str = input()
    if num_and_str:
        line = list(num_and_str.split())
        line[0] = int(line[0])
        my_list.append(line)
my_dict = dict(my_list)

target_value = input()
keys = [key for key, value in my_dict.items() if value == target_value]

if keys:
    for i in range(len(keys)):
        print(keys[i])
else:
    print("! value error !")
    
# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS

# ER_CANT_CREATE_DB
# 1006


# 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# 4108 ER_GIPK_COLUMN_EXISTS
# 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK

# ER_CANT_OPEN_FILE
# ! value error !
