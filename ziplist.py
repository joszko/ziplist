import zipfile
import csv
import sys
import getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hi:')
    except getopt.GetoptError:
        print("Syntax: ziplist.py -i <inputfile>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Syntax: ziplist.py -i <inputfile>')
            sys.exit()
        elif opt == '-i':
            if arg[-3:] == 'zip':
                zf = zipfile.ZipFile('test.zip', 'r')

                with open(''.join([arg[:-3], 'csv']), 'w') as output:
                    wr = csv.writer(output, delimiter="\n")
                    wr.writerow(zf.namelist())

            else:
                print('Need a zip file to work')
                sys.exit()
        elif len(opt) > 2:
            print('Syntax: ziplist.py -i <inputfile>')


if __name__ == "__main__":
    main(sys.argv[1:])
