import re, time, collections

class UserActivity :
    def __init__(self, id, activity, dt) :
        self.id = id
        self.activity = activity
        self.dt = dt

class LogAnalyzer :
    def read_log(self, path) :
        try :
            f = open(path , 'r')
            self.rr = f.readlines()
            f.close()
        except :
            print("파일을 읽을 수 없습니다.")


    def check_valid(self) :
        self.check_log = '\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]) ([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]) [a-z]+[0-9] [A-Z]+'
        self.check_dt = '\d{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01]) ([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])'
        self.check_id = '^[a-z]+[0-9]$'
        self.check_activity = '[A-Z]+'
        self.total_count = 0
        self.right_count = 0
        self.wrong_count = 0
        self.total = []

        try :
            for i in self.rr :
                log = re.match(self.check_log, i)
                self.total_count += 1
                if log :
                    self.right_count += 1
                    dt_match = re.match(self.check_dt, i)
                    dt = dt_match.group()
                    category = i[20:].split()

                    for j in category :
                        id_match = re.match(self.check_id, j)
                        activity_match = re.match(self.check_activity, j)
                        if id_match :
                            id = id_match.group()
                        if activity_match :
                            activity = activity_match.group()
                    ua = UserActivity(id, activity, dt)
                    self.total.append(ua.id + ' - ' + ua.activity)
                else :
                    self.wrong_count += 1
                    print("잘못된 형식입니다. -> " + i)
        except :
            print("파일을 읽을 수 없습니다.")
    
    def report(self, path) :
        text = str()
        text += "=== 사용자 활동 보고서 ===\n"
        text += "분석 시간: %s\n" %time.strftime('%Y-%m-%d %H:%M:%S')
        text += "총 로그 개수: %d\n" %self.total_count
        text += "유효한 로그: %d\n" %self.right_count
        text += "무시된 로그: %d\n" %self.wrong_count
        text += "\n유저별 활동 통계:\n"

        self.total.sort()
        cc = dict(collections.Counter(self.total))
        for i in cc :
            text += str(i) + ' : ' + str(cc[i]) + '\n'
        f = open(path, 'w')
        f.write(text)
        f.close()
        print('\n' + text)

a = LogAnalyzer()
a.read_log('log_file.txt') 
a.check_valid()
a.report('user_report.txt')