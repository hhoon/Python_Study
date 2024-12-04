def read_log(file_path) :
    li = []
    f = open(file_path, 'r')
    for i in f :
        if '#' not in i :
            li.append(i)
    f.close()
    return li