import os

src = '/remember/cmd.txt'
dst = 'cmd.txt'
os.symlink(src, dst)
