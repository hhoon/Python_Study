import re, subprocess

class Server :
    def __init__(self, hostname, ip) :
        self.hostname = hostname
        self.ip = ip
        return
    
    def ping_test(self, ip_list) :
        try :
            ping_check = str(subprocess.check_output(['ping', '-t', '1', '%s' %(ip_list)]))   # subprocess 파이썬에서 쉘 명령어 사용가능, -t = timeout
            if 'ttl' in ping_check :
                self.status = 'OK'
            else :
                self.status = 'FAIL'
        except :
            self.status = 'FAIL'
        return
    
class PingTester :
    def __init__(self, path) :
        self.path = path
        self.servers = {}
        return
    
    def server_list(self) :
        check_ip = '(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
        check_hostname = '[a-zA-Z0-9_-]{4,15}'
        f = open(self.path, 'r')
        for i in f :
            ip_list = re.findall(check_ip, i)
            host_list = re.findall(check_hostname, i)
            if ip_list == [] or host_list == [] :
                print("유효하지 않은 IP 주소나 호스트네임이 있습니다.")
                print(i)
            else :
                host_list = str(host_list)[2:-2] # str과 슬라이싱으로 리스트를 str으로 변환
                ip_list = str(ip_list)[2:-2]
                host_list = Server(host_list, ip_list)
                host_list.ping_test(ip_list)
                self.servers[host_list.hostname] = host_list.ip + ' ' + host_list.status
        f.close()
        return
    
    def report(self, path) :
        f = open(path, 'w')
        for i in self.servers :
            f.write(str(i) + ' : ' + str(self.servers[i]) + '\n')
        f.close()

def main() :
    print("\n\nserver_list.txt파일을 확인 중입니다.")
    a = PingTester('server_list.txt')
    a.server_list()
    while True :
        print("\n1. 추출된 리스트 확인\n2. 핑 상태 확인\n3. 리스트를 저장 후 종료")
        num = input("원하는 옵션을 선택해주세요 : ")
        if num == str(1) :
            for i in a.servers :
                print(str(i))
        elif num == str(2) :
            host = input("리스트에서 확인된 호스트네임을 입력해주세요 : ")
            print("ping status : " + a.servers[host])
        elif num == str(3) :
            a.report('ping_report.txt')
            print("ping_report.txt파일에 핑 상태를 요약해 저장 후 프로그램을 종료하였습니다.")
            break
        else :
            print("다시 입력해주세요.")

main()