def extract(f):
    import py7zr

    archive = py7zr.SevenZipFile(f, mode='r')
    archive.extractall(path="")
    archive.close()
