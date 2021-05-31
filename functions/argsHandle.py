import argparse


def getArgs(args,op):
    parser = argparse.ArgumentParser()

    for arg in args:
        if(op == "required"):
            parser.add_argument(arg)
        else:
            parser.add_argument("--"+arg,required=False)
    
    return parser.parse_args()

