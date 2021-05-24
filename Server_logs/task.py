import re


content = []

def read_file():
    with open ('server_logs.log', 'rt') as myfile:
        contents = myfile.readlines()
    return contents

def write_ip_to_file(content):
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    #init list
    store_ip = []
    
    for line in content:
        store_ip.append(ip_pattern.search(line)[0])
    
    #print(store_ip)
    

    writing = open('ip.log', 'w')

    for el in store_ip:
        writing.write(el + '\n')
    
    writing.close()
    
def total_status_codes():
    content = read_file()
    status_code_pattern = re.compile(r'(\s\d{1}\d{1}\d{1}\s)')
    count = 0
    store_status_code = []
    
    for code in content:
        store_status_code.append(status_code_pattern.search(code)[0])
    
    #print(store_status_code)

    print("Number of 100 status codes: ", store_status_code.count(" 100 "))
    print("Number of 200 status codes: ", store_status_code.count(" 200 "))
    print("Number of 201 status codes: ", store_status_code.count(" 201 "))
    print("Number of 203 status codes: ", store_status_code.count(" 203 "))
    print("Number of 301 status codes: ", store_status_code.count(" 301 "))
    print("Number of 302 status codes: ", store_status_code.count(" 302 "))
    print("Number of 304 status codes: ", store_status_code.count(" 304 "))
    print("Number of 400 status codes: ", store_status_code.count(" 400 "))
    print("Number of 401 status codes: ", store_status_code.count(" 401 "))
    print("Number of 403 status codes: ", store_status_code.count(" 403 "))
    print("Number of 404 status codes: ", store_status_code.count(" 404 "))
    print("Number of 405 status codes: ", store_status_code.count(" 405 "))
    print("Number of 406 status codes: ", store_status_code.count(" 406 "))
    print("Number of 500 status codes: ", store_status_code.count(" 500 "))
    print("Number of 501 status codes: ", store_status_code.count(" 501 "))
    print("Number of 502 status codes: ", store_status_code.count(" 502 "))
    print("Number of 503 status codes: ", store_status_code.count(" 503 "))
    print("Number of 504 status codes: ", store_status_code.count(" 504 "))

def get_404():
    content = read_file()
    write = open('log_get_404.csv', 'w')
    for i in range(len(content)):
        if " 404 " in content[i] and "GET" in content[i]:
            write.write(content[i])


if __name__ == "__main__":
    write_ip_to_file(content)
    total_status_codes()
    get_404()
