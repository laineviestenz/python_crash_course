states = ["florida", "California", "Illinois","louisiana", "Texas"]

lower_states = []
for i in states:
    new = i.lower()
    lower_states.append(new)

print("texas" in lower_states)