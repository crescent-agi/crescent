def bulk_read(pattern="*.py", max_files=100):
    import glob
    files = glob.glob(pattern)[:max_files]
    return {f: open(f).read() for f in files if os.path.exists(f)}