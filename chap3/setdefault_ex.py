def usual_dict(dict_data):
    """dict[key] 사용 """
    new_data = {}
    for key,value in dict_data:
        if key in new_data:
            new_data[key].append(value)
        else:
            new_data[key] = [value]
    return new_data


def setdefault_dict(dict_data):
    """setdefault() 메소드 사용"""
    new_data = {}
    for key, value in dict_data:
        new_data.setdefault(key, []).append(value)
    return new_data


def test_set_dict():
    dict_data = (("key1", "value1"),
                 ("key1", "value2"),
                 ("key2", "value3"),
                 ("key2", "value4"),
                 ("key2", "value5"),)
    print(usual_dict(dict_data))
    print(setdefault_dict(dict_data))


if __name__ == '__main__':
    test_set_dict()