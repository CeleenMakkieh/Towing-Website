import os
import glob
import re

root_dir = r"c:\Users\celee\OneDrive\Desktop\New folder (7)"

# 1. Rename folder if it exists
old_folder = os.path.join(root_dir, 'towing-light-duty')
new_folder = os.path.join(root_dir, 'towing-duty')
if os.path.exists(old_folder):
    os.rename(old_folder, new_folder)
    print("Renamed folder 'towing-light-duty' to 'towing-duty'")
else:
    print("Folder 'towing-light-duty' not found (it might be already renamed)")

count = 0
for filepath in glob.glob(os.path.join(root_dir, '**', 'index.html'), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # Fix broken visual text across line breaks (Towing-Light\nDuty -> Towing\nDuty)
    content = re.sub(r'Towing-Light\s+Duty', 'Towing Duty', content)
    
    # Fix URLs and aliases
    content = content.replace('towing-light-duty', 'towing-duty')
    
    # Also just double check if any old /towing-light-duty/ remaining
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        count += 1
        print(f"Updated {filepath}")

print(f"Processed {count} files.")
