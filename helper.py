#!/usr/bin/python3

import configparser
import sys
import getopt

helper_file = '{path to ini file}'

def main(argv):
    """" Handle arguments passed """
    
    try:
        opts, args = getopt.getopt(argv, "hlt:a:d:", ["help", "list", "title=", "add=", "delete="])

    except getopt.GetoptError:
        print("check usage : \n helper --h \n helper --help")
        sys.exit(2)
    
    config = configparser.ConfigParser()
    config.read(helper_file)

    for opt, arg in opts:

        if(opt in ('-h','--help')):
            help_doc = """helper [-flag] [--option] [arguments]
                    -a : adds section
                    -l : list section
                    -d : delete section
                    -t : show section """
            print(help_doc)
            sys.exit()

        elif(opt in ('-l', '--list')):
            for sect in config.sections():
                print(f'\n[ {sect} ] \n ')
                for k,v in config.items(sect):
                    print(f'{k} = {v}')

        elif(opt in ('-a', '--add')):
            if(arg not in config.sections()):
                config.add_section(arg)
                config[arg] = add_input()
            else:
                print(f'section already present : section found with name {arg}')  

        elif(opt in ('-d', '--delete')):
            if(arg in config.sections()):
                config.remove_section(arg)
                print(f'section {arg} is removed from file')
            else:
                print(f'section not found : No section found with name {arg}')  


        elif(opt in ('-t', '--title')):
            if(arg in config.sections()):
                print(f'[ {arg} ] \n')
                for key, value in config[arg].items():
                    print(f'{key} = {value}')
            else:
                print(f'section not found : No section found with name {arg}')
        
    with open(helper_file, 'w') as f:
        config.write(f)

def add_input():
    keys = ['url', 'username', 'password', 'notes']
    user_input = {}
    for key in keys:
        value = input(f'{key} : ')
        user_input[key] = value
    return user_input

if __name__ == "__main__":
   main(sys.argv[1:])
