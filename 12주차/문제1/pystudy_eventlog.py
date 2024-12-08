import re

class event :
    def __init__(self, timestamp, event_type, device_id) :
        self.timestamp = timestamp
        self.event_type = event_type
        self.device_id = device_id

        return

class log :
    def __init__(self) :
        self.logs = []
        self.ids = []
        return
    
    def read_log(self, path) :
        f = open(path, 'r')
        self.rl = f.readlines()
        return
    
    def check_valid(self) :
        self.check_timestamp = '\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]) ([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])'
        self.check_event_type = r'[A-Z]+ [A-Z]+'
        self.check_device_id = r'ID:[0-9]+'

        for i in self.rl :
            self.timestamp_match = re.match(self.check_timestamp, i)
            self.event_type_match = re.findall(self.check_event_type, i)
            self.device_id_match = re.findall(self.check_device_id, i)
            if self.timestamp_match :
                self.timestamp = self.timestamp_match.group()
            if self.event_type_match :
                self.event_type = str(self.event_type_match)[1:-1]
            if self.device_id_match :
                self.device_id = str(self.device_id_match)[1:-1]
            id = event(self.timestamp, self.event_type, self.device_id)
            self.logs.append([id.event_type[1:-1], id.device_id[1:-1]])
            self.ids.append(id.device_id[1:-1])
        
        self.ids = set(self.ids)

    def print_event(self) :
        #장치 ID별 통계
        print("== 이벤트 통계 요약 ===")
        for i in self.ids :
            self.event_count = []
            for j in self.logs :
                if i in j :
                    self.event_count.append(j[0])

            self.set_event_count = set(self.event_count)
            print("장치 %s" %(i))
            for k in self.set_event_count :
                print("- %s: %s회" %(k, self.event_count.count(k)))
            print("\n")
        
        # 가장 자주 발생한 이벤트
        maxx = 0
        for l in self.logs :
            if maxx < self.logs.count(l) :
                maxx = self.logs.count(l)
                max_logs = l

        print("가장 자주 발생한 이벤트:")
        print("- 장치 %s, 이벤트: %s, 횟수: %d회" %(max_logs[1], max_logs[0], self.logs.count(max_logs)))
        return

a = log()
a.read_log('system_logs.txt')
a.check_valid()
a.print_event()