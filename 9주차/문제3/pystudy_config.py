import re
config_lines = []
old_ip = []
old_port = []
new_config = []

def read_config(file_path) :
    try :
        f = open(file_path, 'r')
        for i in f :
            config_lines.append(i.strip())
    except FileNotFoundError :
        print("로그 파일이 존재하지 않습니다.")
    return

def extract_ip_port(config_lines) :
    try :
        check_ip = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
        check_port = r":[0-9]+"
        for i in config_lines :
            ip = re.findall(check_ip, i)
            port = re.findall(check_port, i)
            old_ip.append(ip)
            old_port.append(port)
    except ValueError :
        print("IP와 포트가 올바른 형식이 아닙니다.")
    return

def update_ip_port(config_lines, old_ip, old_port, new_ip, new_port) :
    if len(old_ip) == len(old_port) == len(new_ip) == len(new_port) :
        for i in range(len(config_lines)) :
            a = config_lines[i].replace(str(old_ip[i][0]) + str(old_port[i][0]), str(new_ip[i]) + str(new_port[i]))
            new_config.append(a)
    else :
        print("기존 ip와 포트가 새로운 ip와 포트수와 다릅니다.")
    return

def save_update_config(config_lines, output_file_path) :
    try :
        f = open(output_file_path, 'x')
        for i in config_lines :
            f.write(i + '\n')
        f.close()
        print("변경된 설정 파일이 'updated_network_config.txt'에 저장되었습니다.")
    except :
        a = input("파일이 이미 존재합니다. 덮어 쓰시겠습니까? (Y or N)")
        if a == "Y" :
            f = open(output_file_path, 'w')
            for i in config_lines :
                f.write(i + '\n')
            f.close()
            print("변경된 설정 파일이 'updated_network_config.txt'에 저장되었습니다.")
        elif a == "N" :
            print("파일을 덮어쓰지 않고 종료하였습니다.\n")
            
        else :
            print("Y or N만 골라주세요.")
    return

read_config('network_config.txt')
extract_ip_port(config_lines)
new_ip = ['10.0.0.1', '192.168.1.2', '192.168.1.3']
new_port = [':8000', ':8081', ':9090']

print("변경 전 IP 주소와 포트")
for i in config_lines :
    print("- " + str(i.split()[0]) + " : " + str(i.split()[1]))

update_ip_port(config_lines, old_ip, old_port, new_ip, new_port)

print("\n변경 후 IP 주소와 포트")
for i in new_config :
    print("- " + str(i.split()[0]) + " : " + str(i.split()[1]))

save_update_config(new_config, "updated_network_config.txt")