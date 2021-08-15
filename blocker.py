import sys
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('-c', action='store_true')
args = parser.parse_args()

sitesPath = 'blocklist.txt'  # path of files to block
hostsPath = '/etc/hosts'  # path of host files, for now assume linux
hostsComment = '\n# ' + 'start:site-blocker'  # used for commenting in hosts file


def main():
    sitesFile = open(sitesPath, 'r')
    sites = sitesFile.read()
    if not sites or sites.isspace():  # make sure the text file is not blank
        sys.exit('blocklist.txt is blank')
    sitesList = sites.splitlines()
    hostsFile = open(hostsPath, 'r')
    hostsContent = hostsFile.read()
    if hostsComment in hostsContent:
        sys.exit('site blocker is active! Clear using sudo python3 --clear')
    hostsFile.close()  # copy hosts into memory
    hostsFile = open(hostsPath, 'w')
    hostsContent = hostsContent + hostsComment  # add comment

    for s in sitesList:
        hostsContent = hostsContent + ('\n127.0.0.1   ' + s)

    hostsFile.write(hostsContent)
    print('Done! Enjoy being distraction free.')


def clear():
    hostsFile = open(hostsPath, 'r')
    hostsContent = hostsFile.read()
    hostsFile.close()  # copy hosts into memory

    clearContent = hostsContent.split(hostsComment)[0]
    hostsFile = open(hostsPath, 'w')
    hostsFile.write(clearContent)

    print('Blocking stopped! Time to procrastinate!')


if __name__ == "__main__":
    if args.c == True:
        clear()
    else:
        main()
