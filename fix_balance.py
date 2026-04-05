with open('index.html') as f:
    c = f.read()

# Walk through and find where balance goes wrong
import re
depth = 0
last_bad = 0
for m in re.finditer(r'<(/?)div', c):
    if m.group(1):
        depth -= 1
    else:
        depth += 1
    if depth < 0:
        print(f"WENT NEGATIVE at pos {m.start()}: {repr(c[m.start()-50:m.start()+20])}")
        depth = 0

print(f"Final depth: {depth}")

# Show end of file
print(repr(c[-400:]))
