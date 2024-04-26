import copy

orig_list = [1, 2, [3, 4]]

shallow_list = copy.copy(orig_list)

orig_list[2][0] = 'a'

print('Original:', orig_list)
print('Shallow Copy:', shallow_list)




orig_dict = {'key1': 'value1', 'key2': {'key3': 'value3'}}

deep_dict = copy.deepcopy(orig_dict)

orig_dict['key2']['key3'] = 'new value'

print('Original:', orig_dict)

print('Deep Copy:', deep_dict)




