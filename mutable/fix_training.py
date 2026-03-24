import sys
import os

def fix_file(filename):
    with open(filename, 'rb') as f:
        raw = f.read()
    try:
        decoded = raw.decode('unicode_escape')
    except UnicodeDecodeError:
        # maybe already fine
        decoded = raw.decode('utf-8')
    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(decoded)
    print(f"Fixed {filename}")

if __name__ == '__main__':
    fix_file('train_gen49_variance.py')
    fix_file('train_gen49_test.py')
    # also fix any other .py files that may be corrupted
    for fname in os.listdir('.'):
        if fname.endswith('.py'):
            # skip patches maybe
            if fname.startswith('patch_'):
                continue
            # check if contains escaped backslashes
            with open(fname, 'rb') as f:
                content = f.read()
            if b'\\' in content:
                print(f"File {fname} contains escaped backslashes, fixing...")
                fix_file(fname)