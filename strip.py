from bs4 import BeautifulSoup
import sys

assert __name__ == "__main__", "This script should be run directly, not imported"

assert len(sys.argv) == 3, "Usage: python strip.py <input_file> <output_file>"
input_file, output_file = sys.argv[1], sys.argv[2]

with open(input_file) as f:
    input_lines = f.readlines()

if input_lines[0].startswith("URL"):
    input_lines = input_lines[1:]
soup = BeautifulSoup("\n".join(input_lines), "html.parser")

with open(output_file, "w") as f:
    f.write(soup.get_text())
