invitations = ["corndog", "mildawg", "walnutz"]

#make list lowercase for all values
#invitations = [x.lower() for x in invitations]
#wouldnt keep continuously updating, would have to add it to each step
#might as well just do it by hand

def print_invite(list):
    for i in list:
        print(i.title() + ", you are invited!")

# Mildawg cant make it
invitations.remove("mildawg")
invitations.append("tamdawg")

# Found a bigger table!
invitations.insert(0, "gram")
invitations.insert(2, "norbdawg")
invitations.append("gramps")
print_invite(invitations)