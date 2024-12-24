

x = 3
y = x
y = x+1

print("Memory address of x:", id(x))
print("Memory address of y:", id(y))
# Mutable dictionary
my_dict = {'a': 1, 'b': 2}

# Modify the dictionary in-place
my_dict['a'] = 10

# Both references point to the same dictionary
other_dict = my_dict

# Modifying through one reference affects the other
other_dict['c'] = 3

print(my_dict)     # Output: {'a': 10, 'b': 2, 'c': 3}
print(other_dict)  # Output: {'a': 10, 'b': 2, 'c': 3}

# Mutable list
my_list = [1, 2, 3]

# Modify the list in-place
my_list[0] = 10

# Both references point to the same list
other_list = my_list

# Modifying through one reference affects the other
other_list.append(4)

print(my_list)     # Output: [10, 2, 3, 4]
print(other_list)  # Output: [10, 2, 3, 4]


obj2 = {
    "a": 2

}

obj = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}


def stringifyNumbers(obj):
    # TODO
    for k, v in obj.items():
        if isinstance(v, int):
            if str(v) not in ['True', 'False']:
                obj[k] = str(v)

        elif isinstance(v, dict):
            stringifyNumbers(v)
    return obj


print(stringifyNumbers(obj))
obj = {
    "stuff": 'foo',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}


def collectStrings(obj):
    answer = []
    # TODO
    for _, v in obj.items():
        if isinstance(v, str):
            answer.append(v)

        elif isinstance(v, dict):
            answer.extend(collectStrings(v))
    return answer


print(collectStrings(obj))  # ['foo', 'bar', 'baz']
print([1]+[2, 3])
# cmd + / to comment
