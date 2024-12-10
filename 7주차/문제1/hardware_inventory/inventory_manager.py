dic = {}
log = []

def add_hw(serial, name, server_ip, status) :
    hw = {}
    hw['serial'] = str(serial)
    hw['name'] = str(name)
    hw['server_ip'] = str(server_ip)
    hw['status'] = str(status)
    
    logg = [serial, name, server_ip, status]
    if logg not in log :
        log.append(logg)

    return hw

def remove_hw(serial) :
    try :
        del dic[serial]
        print(serial + "이 삭제되었습니다.")
    except :
        print("serial을 잘못 입력하셨습니다.")
    return

def get_hw_status(status) :
    try :
        for i, j in dic.items() :
            if j['status'] == status :
                print(j)
    except :
        print("status를 잘못 입력하셨습니다.")
    return

def get_log(serial) :
    for i in range(len(log)) :
        if log[i][0] == serial :
            print(log[i])
    return

def get_hw_server(server_ip) :
    try :
        for i, j in dic.items() :
            if j['server_ip'] == server_ip :
                print(j['name'])
    except :
        print("status를 잘못 입력하셨습니다.")
    return