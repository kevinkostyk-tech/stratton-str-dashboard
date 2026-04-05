with open('index.html') as f:
    c = f.read()

# The problem: </div></div><script>...</script> closes the content wrapper
# then tab-5 and tab-6 are placed outside it.
# Fix: remove the two closing </div> before <script>, move them after tab-6

# Find the closing divs + script block that precede tab-5
old = '</div>\n</div>\n\n<script>\nfunction showTab'
new = '\n<script>\nfunction showTab'

if old in c:
    c = c.replace(old, new, 1)
    print("Step 1 done: removed premature closing divs before script")
else:
    print("ERROR: pattern not found")
    print(repr(c[c.find('<script>')-50:c.find('<script>')+20]))
    exit(1)

# Now find end of tab-6 and add the two closing divs back before </body>
old2 = '\n</div>\n\n</body>'
new2 = '\n</div>\n\n</div>\n</div>\n\n</body>'

if old2 in c:
    # Replace last occurrence
    idx = c.rfind(old2)
    c = c[:idx] + new2 + c[idx+len(old2):]
    print("Step 2 done: added closing divs back before </body>")
else:
    print("ERROR: closing pattern not found")
    exit(1)

with open('index.html', 'w') as f:
    f.write(c)

# Verify div balance in full file
opens = c.count('<div')
closes = c.count('</div>')
print(f"Total div balance: {opens - closes} (should be 0)")

# Verify tab-5 and tab-6 are inside content wrapper
script_pos = c.find('<script>\nfunction showTab')
tab5_pos = c.find('id="tab-5"')
tab6_pos = c.find('id="tab-6"')
print(f"Script at: {script_pos}, tab-5 at: {tab5_pos}, tab-6 at: {tab6_pos}")
print(f"tab-5 after script: {tab5_pos > script_pos}")
