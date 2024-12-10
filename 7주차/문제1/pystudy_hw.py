from hardware_inventory import inventory_manager
dic = inventory_manager.dic

while True :
    print("\n원하는 메뉴를 골라주세요")
    print(" 1. 장비 추가 \n 2. 장비 삭제 \n 3. 상태 조회 \n 4. 장비 히스토리 \n 5. 서버 파트 조회 \n 6. 종료")
    a = int(input())
    if a == 1 :
        print("장비 시리얼, 파트명, 설치된 서버의 IP주소, 현재 장비 상태를 입력해주세요")
        print("ex) s001 CPU 1.1.1.1 사용중")
        serial, name, server_ip, status = map(str, input().split())
        hw = inventory_manager.add_hw(serial, name, server_ip, status)
        dic[serial] = hw

    elif a == 2 :
        print("\n삭제하고 싶은 장비의 serial을 입력해주세요. ex) s001")
        serial = input()
        inventory_manager.remove_hw(serial)

    elif a == 3 :
        print("\n조회를 원하는 상태를 입력해주세요. ex) 수리중")
        status = input()
        inventory_manager.get_hw_status(status)

    elif a == 4 :
        print("\n유지보수 이력조회를 원하는 serial을 입력해주세요. ex) s001")
        serial = input()
        inventory_manager.get_log(serial)

    elif a == 5 :
        print("파트목록을 확인하고 싶은 서버를 입력해주세요. ex) 1.1.1.1")
        server_ip = input()
        inventory_manager.get_hw_server(server_ip)

    elif a == 6 :
        break

    else :
        print("\n다시 입력해주세요.")


"""
s001 CPU 1.1.1.1 사용중
s002 memory 1.1.1.1 사용중
s003 memory None 수리중
s004 SSD None 대기중
s005 CPU None 수리중
"""