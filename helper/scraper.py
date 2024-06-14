import socket
import random
import threading
import os
import sys

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
print("[2] Proxy Scraper")
print(" ")
print(" ")

option = input(">  ")