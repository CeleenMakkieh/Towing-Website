import os
import glob
import re
import base64

root_dir = r"c:\Users\celee\OneDrive\Desktop\New folder (7)"

def process_base64_match(match):
    b64_str = match.group(1)
    try:
        decoded_bytes = base64.b64decode(b64_str)
        decoded_str = decoded_bytes.decode('utf-8')
        if 'Towing-Light Duty' in decoded_str or 'Towing- Duty' in decoded_str:
            decoded_str = decoded_str.replace('Towing-Light Duty', 'Towing Duty').replace('Towing- Duty', 'Towing Duty')
            new_b64_bytes = base64.b64encode(decoded_str.encode('utf-8'))
            return 'data-build-your-own="' + new_b64_bytes.decode('utf-8') + '"'
    except Exception as e:
        pass
    return match.group(0)

count = 0
for filepath in glob.glob(os.path.join(root_dir, '**', 'index.html'), recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    content = re.sub(r'data-build-your-own="([^"]+)"', process_base64_match, content)
    content = content.replace('Towing-Light Duty', 'Towing Duty')
    content = content.replace('Towing- Duty', 'Towing Duty')
    content = re.sub(r'data-link-text="Light & Medium Towing"([^>]+)>Light & Medium\s*Towing', r'data-link-text="Towing Duty"\1>Towing Duty', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print(f"Updated {filepath}")
        count += 1
print(f"Done updating {count} files.")
