def remove_duplicates(a_list):
    b_list = []
    for i in a_list:
        if i in b_list:
            continue
        else:
            b_list.append(i)
    return b_list
