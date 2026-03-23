import sys
import os

def fix_file(filename):
    try:
        with open(filename, 'rb') as f:
            raw = f.read()
        # Try to decode as utf-8 first; if fails, try unicode_escape
        try:
            decoded = raw.decode('utf-8')
        except UnicodeDecodeError:
            decoded = raw.decode('unicode_escape')
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(decoded)
        print(f"Fixed {filename}")
    except Exception as e:
        print(f"Error fixing {filename}: {e}")

if __name__ == '__main__':
    for root, dirs, files in os.walk('.'):
        for fname in files:
            if fname.endswith('.py'):
                path = os.path.join(root, fname)
                # skip __pycache__
                if '__pycache__' in path:
                    continue
                # read a small portion to check if contains escaped backslashes
                with open(path, 'rb') as f:
                    content = f.read(4096)
                if b'\\\\' in content:
                    print(f"File {path} contains escaped backslashes, fixing...")
                    fix_file(path)