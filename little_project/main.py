import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", nargs=1)
parser.add_argument("-t", "--type", nargs=1)
parser.add_argument("-d", "--data", nargs="*")
parser.add_argument("-o", '--output', action="store_true")
parser.add_argument("-i", '--input', nargs=1)

args = parser.parse_args()

print(args)
data = "Test,Column,Something"
with open(args.input[0], "r") as file:
    for line in file:
        print(line.rstrip())
