import argparse

def getArgs(args):
    parser = argparse.ArgumentParser()

    for arg in args:
        if "--" in arg:
            parser.add_argument(arg,required=False)
        elif "??" in arg:
            arg = arg.replace("??","--")
            parser.add_argument(arg,action="store_false",dest=arg.replace("--",""))
        elif "?" in arg:
            arg = arg.replace("?","--")
            parser.add_argument(arg,action="store_true",dest=arg.replace("--",""))
        else:
            parser.add_argument(arg)
    
    return parser.parse_args()

