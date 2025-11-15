'''
Merge Dictionaries
Merge these two dictionaries:

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}


The result should combine both, updating values of duplicate keys.
'''

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

comm_dict = {}

comm_dict = dict1

comm_dict.update(dict2)

print(comm_dict)

comm_dict['d'] = 23

print(comm_dict)

comm_dict.update({'e': 45})
print(comm_dict)
