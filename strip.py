from bs4 import BeautifulSoup
import sys
import os

assert __name__ == "__main__", "This script should be run directly, not imported"

assert len(sys.argv) == 3, "Usage: python strip.py <input_folder> <output_folder>"
input_folder, output_folder = sys.argv[1], sys.argv[2]
unicode_errors = 0

def decode_fixed(s):
    # dirty hack for broken utf-8
    while True:
        try:
            return s.decode("utf-8")
        except UnicodeDecodeError as e:
            global unicode_errors
            unicode_errors += 1
            print(f"Unicode error {unicode_errors} at {e.start} in {filename}")
            s = s[:e.start] + "�".encode() + s[e.end:]

def process_file(filename):

    print("Processing ", filename)

    with open(f"{input_folder}/{filename}", "rb") as f:
        input_lines = decode_fixed(f.read()).split("\n")

    if input_lines[0].startswith("URL"):
        input_lines = input_lines[1:]
    soup = BeautifulSoup("\n".join(input_lines), "html.parser")

    with open(f"{output_folder}/{filename}", "w") as f:
        f.write(soup.get_text())

try:
    os.mkdir(output_folder)
except FileExistsError:
    pass

for filename in os.listdir(input_folder):
    process_file(filename)

print(f"Total unicode errors: {unicode_errors}")