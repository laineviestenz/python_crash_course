invitations = ["corndog", "mildawg", "walnutz"]

#make list lowercase for all values
#invitations = [x.lower() for x in invitations]
#wouldnt keep continuously updating, would have to add it to each step
#might as well just do it by hand

def print_invite(list):
    while list:
        x = list.pop()
        print(x.title() + ", you are invited!")


# Mildawg cant make it
invitations.remove("mildawg")
invitations.append("tamdawg")

# Found a bigger table!
invitations.insert(0, "gram")
invitations.insert(2, "norbdawg")
invitations.append("gramps")
# print_invite(invitations)

#table wont arrive in time :(
while len(invitations) > 2:
    take_off = invitations.pop()
    print(take_off + ", sorry you are uninvited:(")

print_invite(invitations)