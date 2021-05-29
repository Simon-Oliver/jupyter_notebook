import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", nargs=1)
parser.add_argument("-t", "--type", nargs=1)
parser.add_argument("-o", '--output', action="store_true")

args = parser.parse_args()

print(args.type[0])
