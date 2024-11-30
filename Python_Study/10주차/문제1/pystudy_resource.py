class Server :
    def __init__(self, name, cpu_usage, memory_usage, disk_usage) :
        self.name = name
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.disk_usage = disk_usage
        self.cpu_max = 100
        self.memory_max = 128
        self.disk_max = 1024
        return
    
    def add_resources(self, cpu, memory, storage) :
        if (self.cpu_usage + cpu) <= self.cpu_max and (self.memory_usage + memory) <= self.memory_max and (self.disk_usage + storage) <= self. disk_max :
            self.cpu_usage += cpu
            self.memory_usage += memory
            self.disk_usage += storage
        else :
            print("리소스를 초과합니다.")
        return
    
    def get_status(self) :
        return print(" cpu_usage : %s\n memory_usage : %s\n disk_usage : %s" %(self.cpu_usage, self.memory_usage, self.disk_usage))
    def is_overloaded(self) :
        if self.cpu_usage >= 90 or self.memory_usage >= 120 : 
            self.status = "과부화"
        else :
            self.status = "정상" 
        return self.status
    
class DataCenter :
    def __init__(self, name) :
        self.name = name
        self.servers = []
        return
    def add_server(self, server) :
        self.servers.append(server)
        
        return
    def distribute_resources(self, server_name, cpu, memory, disk) :
        for i in self.servers :
            if i.name == server_name :
                a = i
            else :
                b = i
        a.cpu_usage += cpu
        a.memory_usage += memory
        a.disk_usage += disk
        self.recommend = ""
        print("=== 데이터센터 상태 ===")
        print("데이터센터 이름: %s\n" %datacenter.name)
        print("서버 상태:")
        for i in range(len(datacenter.servers)) :
            sv = datacenter.servers[i]
            print(str(int(i)+1) + ". " + sv.name)
            if sv.cpu_usage > sv.cpu_max :
                print("   - CPU 사용량 : %s%% (과부화)" %sv.cpu_usage)
            else :
                print("   - CPU 사용량 : %s%% " %sv.cpu_usage)
            if sv.memory_usage > sv.memory_max :
                print("   - 메모리 사용량 : %sGB (과부화)" %sv.memory_usage)
            else :
                print("   - 메모리 사용량 : %sGB " %sv.memory_usage)
            if sv.disk_usage > sv.disk_max :
                print("   - 디스크 사용량 : %sGB (과부화)" %sv.disk_usage)
            else :
                print("   - 디스크 사용량 : %sGB " %sv.disk_usage)
            print("   - 상태 : %s \n" %sv.is_overloaded())

        if a.is_overloaded() == "과부화" :
            self.recommend = "권장 조치:\n- %s의 과부하 리소스를 %s로 분산" %(a.name, b.name)
        return print(self.recommend)

# 서버 객체 생성
server1 = Server("Server1", 80, 100, 500)
server2 = Server("Server2", 50, 64, 300)

# 데이터센터 생성 및 서버 추가
datacenter = DataCenter("PGDC")
datacenter.add_server(server1)
datacenter.add_server(server2)

# 리소스 추가 및 분산
datacenter.distribute_resources("Server1", 15, 30, 100)