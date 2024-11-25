import re

email_list = []
valid_emails = []

def read_email(file_path) :
    try :
        f = open(file_path, 'r')
        for i in f :
            email_list.append(i)
    except FileNotFoundError :
        print("로그 파일이 존재하지 않습니다.")
    return

def validate_email(email_list) :
    check_email = r"[a-zA-Z0-9._%-]+@dkt.com"
    for i in email_list :
        email = re.findall(check_email, i)
        if email != [] :
            valid_emails.append(email)
    return

def print_valid_emails(file_path) :
    f = open(file_path, 'r')
    print(f.read())
    f.close()
    return

def save_valid_emails(valid_emails, output_file) :
    try :
        f = open(output_file, 'x')
        f.write('유효한 이메일 주소\n')
        for i in valid_emails :
            f.write('- ' + ''.join(i) + '\n')
        f.close()
        print_valid_emails('save_valid_emails.txt')
    except :
        a = input("파일이 이미 존재합니다. 덮어 쓰시겠습니까? (Y or N)")
        if a == "Y" :
            f = open(output_file, 'w')
            f.write('유효한 이메일 주소\n')
            for i in valid_emails :
                f.write('- ' + ''.join(i) + '\n')
            f.close()
            print_valid_emails('save_valid_emails.txt')
        elif a == "N" :
            print("파일을 덮어쓰지 않고 종료하였습니다.\n")
            print_valid_emails('save_valid_emails.txt')
        else :
            print("Y or N만 골라주세요.")
    return

read_email('email.txt')
validate_email(email_list)
save_valid_emails(valid_emails, 'save_valid_emails.txt')