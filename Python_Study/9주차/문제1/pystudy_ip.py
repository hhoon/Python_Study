import re

log_lines = []
ip_list = []
str_ip_list = []
rm_ip_list = []

def read_log(file_path) :
    try :
        f = open(file_path, 'r')
        for i in f :
            log_lines.append(i)
    except FileNotFoundError :
        print("로그 파일이 존재하지 않습니다.")
    return

def extract_ip(log_lines) :
    check_ip = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    for i in log_lines :
        ip = re.findall(check_ip, i)
        ip_list.append(ip)
    return

def remove_ips(ip_list) :
    for i in ip_list :
        str_ip_list.append(''.join(i))   # 리스트를 str으로 변환
    
    for i in str_ip_list :   # 중복값 제거
        if i not in rm_ip_list :
            rm_ip_list.append(i)
    return


read_log('access.log')
extract_ip(log_lines)
remove_ips(ip_list)

# 출력
print("고유 IP 주소 목록")
for i in rm_ip_list :
    print("- " + str(i))