current_users = ["admin", "joe", "peter", "josh", "laine", "JOHN"]
new_users = ["josh", "Elaina", "johN", "Elizabeth", "peter"]

if new_users:
    #if there are new users: first, make the current list lowercase
    for i in current_users:
        current_users.append(current_users.pop().lower())
    #check the lowercase version of each new user against the new lowercase
    #list of current users and print availability
    for i in new_users:
        if i.lower() in current_users:
            print(i + ", sorry, that username is not available")
        else:
            print("good news! " + i + " is an available username")