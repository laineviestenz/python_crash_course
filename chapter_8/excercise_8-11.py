magician_names = ['tom', 'dick', 'harry', 'joe']

def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names):
    new_list = []
    while names:
        modified = names.pop() + ' the GREAT'
        new_list.append(modified)
    return new_list

mod_list = make_great(magician_names[:])

print(mod_list)
print(magician_names)