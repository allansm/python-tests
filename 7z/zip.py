def extract(f):
    import py7zr

    archive = py7zr.SevenZipFile(f, mode='r')
    files = archive.getnames()
    archive.extract(targets=files)
    archive.close()

def test(f):
    from os import system

    system('7z x "'+f+'"')
