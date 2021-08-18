def run(that):
    import os
    from os.path import dirname

    tmp = os.getcwd()

    os.chdir(dirname(__file__))
    that = that()
    os.chdir(tmp)
    that()
def that():
    from cdirSize import getSize
    return getSize

run(that)

