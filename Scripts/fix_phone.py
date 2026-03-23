import os

directory = r"c:\Users\celee\OneDrive\Desktop\New folder (7)"

old_text = 'data-diy-text="">(214) 433-1070</div>'
new_text = 'data-diy-text=""><a href="tel:+12144331070" style="color: var(--color_8, #ffffff); text-decoration: none;">(214) 433-1070</a></div>'

count = 0

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith("index.html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_text in content:
                content = content.replace(old_text, new_text)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Updated {path}")

print(f"Total files updated: {count}")
