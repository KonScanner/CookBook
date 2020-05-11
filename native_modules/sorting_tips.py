""" In general sorted() sorts by capitalizad characters,
then alphabetical letter; when it comes to strings.
By numbers when it comes to integers or floats."""

obj_list = ['This', 'is', 'an', 'example']
obj_list2 = ['this', 'is', 'an', 'example']
obj_list3 = [5, 4, 3, 2, 1]


print(sorted(obj_list))
print(sorted(obj_list2))
print(sorted(obj_list3))

""" Even though that is the case, you could always create a key,
to help you sort by element of importance."""


def find_example(val):
    if val == 'example':
        return 1
    return len(val)


print(sorted(obj_list, key=find_example))
