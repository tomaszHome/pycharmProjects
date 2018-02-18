dic = {'item0': 'A', 'item1': ['B', 'C'], 'item2': [10, 11, 'D']}
dic2 = {'item3': 'G', 'item4': [2, 4], 'item5': ['L', 'P', 'D']}


def dic_count_values(dictionary):
    for key, value in dictionary.items():
        # print value
        counter = key, len([item for item in value if item])
        print(counter)


def dic_items(dictionary):
    for items in dictionary.items():
        print(items)


def dic_keys(dictionary):
    print(dic.keys())
    for keys in dic.keys():
        print(keys)


# MAIN
if __name__ == '__main__':

    print("Dictionaries:")
    print("dic = " + str(dic))
    print("dic2 = " + str(dic2))

    print("\nPrint dictionary items:")
    dic_items(dic)

    print("\nPrint dictionaries keys:")
    dic_keys(dic)

    print("\nPrint dictionary key values:")
    for values in dic.values():
        print(values)

    print("\nCount keys in dictionary:")
    print len(dic)

    print("\nCount number of values in each key:")
    dic_count_values(dic)







