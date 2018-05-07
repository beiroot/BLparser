import re
import argparse
import sys

re1 = '(.+?)'       # 212 or www
re2 = '(\[\.\])'    # [.]
re3 = '(.+?)'       # 213 or com

re4 = '(.+?)'       # the same but with ( )
re5 = '(\(\.\))'
re6 = '(.+?)'

re7 = '(hxxp)'      # http/https obfuscated

argp = argparse.ArgumentParser()
argp.add_argument("-f", metavar="FILE", default="input.txt",
                  help="file to parse. default: input.txt")
args = argp.parse_args()

rgurl1 = re.compile(re1 + re2 + re3, re.IGNORECASE | re.DOTALL)
rgurl2 = re.compile(re4 + re5 + re6, re.IGNORECASE | re.DOTALL)
rgurl3 = re.compile(re7, re.IGNORECASE | re.DOTALL)

lista = []
lista_parsed = []


def parse(line):
    parsed_line = line.replace('hxxp', 'http').\
        replace('[', '').replace(']', '').replace('(', '').replace(')', '').strip()
    return parsed_line


try:
    with open(args.f, encoding="ascii", errors="ignore") as file:
        read = file.readlines()
        for line in read:
            if re.search(rgurl1, line) is not None or re.search(rgurl2, line) is not None or \
                    re.search(rgurl3, line) is not None:
                parsed = parse(line)
                lista.append(parsed)

except FileNotFoundError:
    print("You have not provided the file or there's no such file")
    print("use: pars_BL -f FILE")
    print("or you could put""input.txt"" in the same folder as this source/executable")
    sys.exit()

lista.sort()

with open("output.txt", 'w') as output:
    for element in lista:
        output.write(element+"\n")
