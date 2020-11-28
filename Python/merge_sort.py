def merge(l, r):
    m = []
    l_index, r_index = 0

    while l_index < len(l) and r_index < len(r):
        if l[l_index] < r[r_index]:
            m.append(l[l_index])
            l_index += 1
        else:
            m.append(r[r_index])
            r_index += 1

    if l_index = len(l):
        m.extend(r[r_index:])
    else:
        r_index = len(r):
        m.extend(l[l_index:])

    return m

    

def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)