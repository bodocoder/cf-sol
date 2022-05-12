def get_set_username(filename):
    file = open(filename,"r")
    users = set(file.readlines())
    file.close()
    return users


first_user_list = get_set_username("fe1.txt")
second_user_list = get_set_username("file2.txt")

common_users = []

for user in first_user_list:
    if user in second_user_list:
        common_users.append(user)

print("common users are: ", common_users)