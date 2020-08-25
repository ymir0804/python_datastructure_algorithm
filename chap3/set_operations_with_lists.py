def remove_dup(parameter_set):
    # 중복값 제거 후 반환
    return list(set(parameter_set))


def intersection(parameter_set1, parameter_set2):
    # list(intersection(parameter_set1, parameter_set2)) 와 동일
    return list(set(parameter_set1) & set(parameter_set2))


def union(parameter_set1, parameter_set2):
    # list(union(parameter_set1, parameter_set2)) 와 동일
    return list(set(parameter_set1) | set(parameter_set2))
