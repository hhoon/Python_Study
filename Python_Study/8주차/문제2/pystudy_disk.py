from raid_disk_monitoring import raid_disk_manager
smart_dic = {}
raid_dic = {}
tmp = {}
Disks = []
good = {}
bad = {}

# smart값 딕셔너리에 정리
smart = raid_disk_manager.read_log('raid_disk_monitoring/smart_data.log')

for i in smart :
    if ',' in i :
        loc = i.split(',')[1].strip()
        tmp['time'] = i.split(',')[0]
    elif '\n' == i :
        smart_dic[loc] = tmp
        tmp = {}
    else :
        tmp[i.split(':')[0]] = i.split(':')[1].strip()
smart_dic[loc] = tmp


# raid값 딕셔너리에 정리
raid = raid_disk_manager.read_log('raid_disk_monitoring/raid_status.log')

for i in raid :
    if i.count(':') > 1 :
        raid_dic['time'] = i.strip()
    elif 'Disks:\n' == i :
        continue
    elif i[0] == '-' :
        Disks.append(i.split('-')[1].strip())
    else :
        raid_dic[i.split(':')[0]] = i.split(':')[1].strip()
raid_dic['Disks:'] = Disks


# smart값 체크
for i in smart_dic :
    if smart_dic[i]['Health_Status'] == 'GOOD' :
        good[i] = smart_dic[i]
    else :
        bad[i] = smart_dic[i]


# 출력
print('=== RAID 디스크 상태 리포트 ===')
print('분석시간:' + raid_dic['time'])
if raid_dic['RAID_Level'] == '1' :
    print('RAID 구성 : RAID ' + raid_dic['RAID_Level'] + ' (미러링)')

print('문제 발견된 디스크:')
cnt = 1
for i in bad :
    if bad[i]['Health_Status'] == 'WARNING' :
        print(str(cnt) + '. ' + i + ' (주의 필요)')
        print('     - 상태: 성능 저하')
        print('     - 문제:')
    if int(bad[i]['Reallocated_Sectors']) >= 10 :
        print('       * 재할당 섹터: '+ bad[i]['Reallocated_Sectors'] + '개 발견 ')
    if int(bad[i]['Temperature']) >= 30 :
        print('       * 온도 : ' + bad[i]['Temperature'] + '°C (높음)')
    if int(bad[i]['Power_On_Hours']) >= 30000 :
        print('       * 사용 시간: ' + bad[i]['Power_On_Hours'] + '시간')
    print('     - 권장: 백업 후 교체 고려')
    cnt += 1

print('\n정상 디스크:')
cnt = 1
for i in good :
    print(str(cnt) + '. ' + i)
    print('     - 상태: 정상')
    print('     - 온도: ' + good[i]['Temperature'] + '°C')
    print('     - 사용 시간: ' + good[i]['Power_On_Hours'] + '시간')

print('\nRAID 성능 상태 :')
if raid_dic['RAID_Level'] == '1' and int(raid_dic['Read_Speed_MB']) >= 200 :
    print(' - 읽기 속도: ' + raid_dic['Read_Speed_MB'] + 'MB/s (정상)')
if raid_dic['RAID_Level'] == '1' and int(raid_dic['Write_Speed_MB']) >= 150 :
    print(' - 쓰기 속도: ' + raid_dic['Write_Speed_MB'] + 'MB/s (정상)')
if int(raid_dic['Read_Speed_MB']) >= 200 and int(raid_dic['Write_Speed_MB']) >= 150 :
    print(' - 전체 상태: 정상 작동 중')

print('\n권장 조치사항:')
if len(bad) > 0 :
    for i in bad :
        print('1. ' + i + ' 디스크 교체 계획 수립')
        print('2. 정기적인 백업 확인')
    if int(bad[i]['Temperature']) >= 30 :
        print('3. 서버실 온도 점검')