
def get_set_username(filename):
    file = open(filename,"r")
    users = set(file.readlines())
    file.close()
    return users


old_user_list = get_set_username(".txt")
new_user_list = get_set_username(".txt")

removed = []
added = []

for user in old_user_list:
    if user in new_user_list:
        continue
    else:
        removed.append(user)

for user in new_user_list:
    if user in old_user_list:
        continue
    else:
        added.append(user)

print("removed users are: ",removed)
print("newly added users are: ", added)