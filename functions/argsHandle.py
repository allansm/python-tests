import argparse
#deprecated
'''
def getArgs(args,op):
    parser = argparse.ArgumentParser()

    for arg in args:
        if(op == "required"):
            parser.add_argument(arg)
        else:
            parser.add_argument("--"+arg,required=False)
    
    return parser.parse_args()
'''
def getArgs(args):
    parser = argparse.ArgumentParser()

    for arg in args:
        if "--" in arg:
            parser.add_argument(arg,required=False)
        else:
            parser.add_argument(arg)
    
    return parser.parse_args()

