import argparse

def getArgs(args):
    parser = argparse.ArgumentParser()

    for arg in args:
        if "--" in arg:
            parser.add_argument(arg,required=False)
        else:
            parser.add_argument(arg)
    
    return parser.parse_args()

