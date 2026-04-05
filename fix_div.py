with open('index.html') as f:
    c = f.read()

# The issue: there's an extra </div> before </body> closing tab-6 prematurely
# Tab-6 ends with: </div>\n</div>\n\n  -- but needs only one closing </div> for tab-6 itself
# Find the end of tab-6 content and fix the closing

# Current ending of tab-6:
old = '</div>\n\n</div>\n</div>\n\n'
new = '</div>\n\n</div>\n\n'

if old in c:
    # Only replace the last occurrence (the one near </body>)
    idx = c.rfind(old)
    c = c[:idx] + new + c[idx+len(old):]
    with open('index.html', 'w') as f:
        f.write(c)
    
    # Verify
    with open('index.html') as f:
        v = f.read()
    start = v.find('id="tab-6"')
    end = v.find('</body>')
    tab6 = v[start:end]
    opens = tab6.count('<div')
    closes = tab6.count('</div>')
    print(f'Balance after fix: {opens - closes} (should be 0)')
else:
    print('Pattern not found - checking end of file')
    print(repr(c[-300:]))
