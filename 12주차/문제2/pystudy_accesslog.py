import re
class log_data :
    def __init__(self, ip, datetime, http_method, url, http_status, response, agent) :
        self.ip = ip
        self.datetime = datetime
        self.http_method = http_method
        self.url = url
        self.http_status = http_status
        self.response = response
        self.agent = agent
        return
    
class log :
    def __init__(self) :
        self.logs = []
        self.http_methods = []
        self.http_statuses = []
        self.agents = []
        self.ips = []
        return
    
    def read_log(self, path) :
        f = open(path, 'r')
        self.rl = f.readlines()
        f.close()
        return
    def check_valid(self) :
        self.check_ip = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
        self.check_datetime = '\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]) ([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])'
        self.check_http_method = '[A-Z]+ '   # 뒤에 한칸 띄어쓰기 사용하여 http method만 추출
        self.check_url = '/[a-z./]+[a-z]+'
        self.check_http_status = '[0-9]{3}'
        self.check_response = '[0-9]+'
        self.check_agent = '[A-Za-z]+/[0-9.]+'

        for i in self.rl :
            lenn = 0
            self.ip_match = re.match(self.check_ip, i)
            self.ip = str(self.ip_match.group())
            lenn += len(self.ip) + 4   # match를 쓰기 위해서 맨 앞을 같게 맞춰줌

            self.datetime_match = re.match(self.check_datetime, i[lenn:])
            self.datetime = str(self.datetime_match.group())
            lenn += len(self.datetime) + 3

            self.http_method_match = re.match(self.check_http_method, i[lenn:])
            self.http_method = str(self.http_method_match.group())
            lenn += len(self.http_method)

            self.url_match = re.match(self.check_url, i[lenn:])
            self.url = str(self.url_match.group())
            lenn += len(self.url) + 11

            self.http_status_match = re.match(self.check_http_status, i[lenn:])
            self.http_status = str(self.http_status_match.group())
            lenn += len(self.http_status) + 1

            self.response_match = re.match(self.check_response, i[lenn:])
            self.response = str(self.response_match.group())
            lenn += len(self.response) +2
            
            self.agent_match = re.match(self.check_agent, i[lenn:])
            self.agent = str(self.agent_match.group())

            ld = log_data(self.ip, self.datetime, self.http_method, self.url, self.http_status, self.response, self.agent)

            self.logs.append({'ip' : ld.ip, 'datetime' : ld.datetime, 'http_method' : ld.http_method, 'url' : ld.url, 'http_status' : ld.http_status, 'response' : ld.response, 'agent' : ld.agent})
            self.http_methods.append(ld.http_method)
            self.http_statuses.append(ld.http_status)
            self.agents.append(ld.agent)
            self.ips.append(ld.ip)

        self.http_methods = set(self.http_methods)
        self.http_statuses = set(self.http_statuses)
        self.agents = set(self.agents)
        self.ips = set(self.ips)

    def print_data(self):

        print("=== HTTP 메서드별 요청 수 ===")
        for i in self.http_methods :
            cnt = 0
            for j in self.logs :
                if i == j['http_method'] :
                    cnt += 1
            print("%s: %d" %(i, cnt))

        print("\n=== HTTP 상태 코드별 요청 수 ===")
        for i in self.http_statuses :
            cnt = 0
            for j in self.logs :
                if i == j['http_status'] :
                    cnt += 1
            print("%s: %d" %(i, cnt))

        print("\n=== 사용자 에이전트별 요청 수 ===")
        for i in self.agents :
            cnt = 0
            for j in self.logs :
                if i == j['agent'] :
                    cnt += 1
            print("%s: %d" %(i, cnt))

        print("\n=== 응답 시간이 가장 긴 요청 (상위 5개) ===")    
        logs_sort = sorted(self.logs, key=lambda x :int(x['response']), reverse = True)   # str으로 저장되어 있으므로 int형으로 변환 필요함
        for i in range(len(logs_sort)) :
            print("%d. IP: %s, URL: %s, 응답 시간: %sms" %(i+1, logs_sort[i]['ip'], logs_sort[i]['url'], logs_sort[i]['response']))

        print("=== 특정 IP 요청 수 ===")
        inputt = input("IP를 입력해주세요 : ex) 10.0.0.2\n")
        cnt = 0
        for i in self.logs :
            if i['ip'] == inputt :
                cnt += 1
        print("IP: %s, 요청 수 : %d" %(inputt, cnt))
        return
    
a = log()
a.read_log('access_logs.txt')
a.check_valid()
a.print_data()