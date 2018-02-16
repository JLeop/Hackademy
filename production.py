def remove_duplicates(a_list):
    output = [a_list[0]]
    for i in a_list:
        if i in output:
            continue
        else:
            output.append(i)
    return output
