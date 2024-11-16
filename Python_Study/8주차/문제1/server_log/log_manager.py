li = []

def read_logs(file_path) :
    try :
        f = open(file_path, 'r')
        f.readlines()
        size = f.tell()
        f.seek(0)
        while size != f.tell() :
            try :
                a = f.readline()
                li.append(a)
            except ValueError :
                continue
        f.close()
        print(li)
    except FileNotFoundError :
        print("로그 파일이 존재하지 않습니다.")
    return

def filter_logs(logs, keyword) :
    error_log = []
    for i in logs :
        if keyword in i :
            error_log.append(i)
    return error_log

def save_logs(filtered_logs, output_file_path) :
    f = open(output_file_path, 'w')
    f.write(str(filtered_logs))
    f.close
    return print("에러 로그가 'error_logs.txt'에 저장되었습니다.")