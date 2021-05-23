import argparse

parser = argparse.ArgumentParser()
   
parser.add_argument('--name', required=False)

args = parser.parse_args()

name = args.name

if name == None:
    print("there is no name u.u")
else:
    print(name)

#print(f'Hello {args.name}')
