invitations = ["corndog", "mildawg", "walnutz"]
def print_invite(list):
    for i in list:
        print(i.title() + ", you are invited!")

# Mildawg cant make it
invitations.remove("mildawg")
invitations.append("tamdawg")

print_invite(invitations)
