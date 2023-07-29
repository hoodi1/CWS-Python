'''Write a function called merge_dictionaries(dict1, dict2) that
takes two dictionaries dict1 and dict2 as parameters and returns a
new dictionary that contains the key-value pairs from both input
dictionaries. If a key is present in both dictionaries, the value from
dict2 should overwrite the value from dict1.'''

def merge_dictionaries(dict1, dict2):
    dict3 = {}

    for k,v in dict1.items():
        if k not in dict2:
            dict3[k] = v
    for k,v in dict2.items():    
        if k in dict1:
            dict3[k] = v
    print(dict3)

merge_dictionaries(dict1 = {"rame":12, "name":123, 1234:23}, dict2= {"rame":23, 12:23})