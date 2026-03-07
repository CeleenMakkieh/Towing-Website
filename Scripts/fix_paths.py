import os

root_dir = r"c:\Users\celee\OneDrive\Desktop\New folder (7)"
folders_to_fix = ['/Style/', '/Scripts/', '/Resources/', '/home/']

for root, dirs, files in os.walk(root_dir):
    # skip .git
    if '.git' in root: continue
    
    for file in files:
        if file.endswith('.html') or file.endswith('.css'):
            filepath = os.path.join(root, file)
            # count directories deeper than root_dir
            rel_path = os.path.relpath(filepath, root_dir)
            depth = 0
            if os.path.dirname(rel_path):
                depth = rel_path.count(os.sep)
            
            prefix = "./" if depth == 0 else "../" * depth
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            for folder in folders_to_fix:
                content = content.replace(f'"{folder}', f'"{prefix}{folder[1:]}')
                content = content.replace(f"'{folder}", f"'{prefix}{folder[1:]}")
                content = content.replace(f"url({folder}", f"url({prefix}{folder[1:]}")
                content = content.replace(f"url('{folder}", f"url('{prefix}{folder[1:]}")
                content = content.replace(f'url("{folder}', f'url("{prefix}{folder[1:]}')
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed paths in {rel_path}")
print("Done fixing paths.")
