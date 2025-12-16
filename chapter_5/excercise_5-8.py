usernames = ["admin", "joe", "peter", "josh", "laine"]

for username in usernames:
    if username == 'admin':
        print("hello, " + username.title() + "! You have full privelages.")
    else:
        print("Hello, " + username.title() + "! Please contact the adminisrator if you have any questions.")