# LIST
#
# a = [1, 2, 3, 4, 5, 6]
#
# print(a[1:5:2])
# print(a[::-2])
#
# # learn to next lesson
# # a.append()
# # a.insert()
# # a.pop()
# # a.sort()
# # a.remove()
#
# b = [3, 4]
# c = [10000]
# print( a + b + c)


# # TUPLE
# a = tuple()
# a = (1, 2, 3, 4, 5, 6)
# b = [1, 2, 3, 4, 5, 6]
#
# # error
# # a[4] = 6
#
# print(a.__sizeof__())
# print(b.__sizeof__())

# DICT
# d = {}
# d = dict()
# d = {
#     'name': 'Dasha',
#     'phone': '+380631735096',
#     1 : 'number'
# }
#
# d.update()
# d.get('fff', 'nothing was defined')
#
#
# print(d)
# print(d["name"])
#
# d.items()
# d.keys()
# d.clear()
# d.pop()
# d.popitem()
# d.update()
# d.values()

d = {
    'name': 'Dasha',
    'phone': '+380631735096',
    1 : 'number'
}

for (key, value) in d.items():
    print(f'My {key} is {value}')

print(d.keys())

