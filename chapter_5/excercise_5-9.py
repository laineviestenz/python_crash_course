usernames = ["admin", "joe", "peter", "josh", "laine"]

if usernames:
    for username in usernames:
        if username == 'admin':
            print("hello, " + username.title() + "! You have full privelages.")
        else:
            print("Hello, " + username.title() + "! Please contact the " +
                "adminisrator if you have any questions.")
else:
    print("No current users. Did you create an admin account?")