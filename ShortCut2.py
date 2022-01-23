def mapStr(string,rules):
    for key, value in rules.items():
        string = string.replace(key,value)
    return string

def addRule(rules,short,outp):
    rules[str(short)] = str(outp)
    return rules

def removeRule(rules,short):
    rules.pop(short, None)
    return rules

def main():
    rules = {}
    string = ''
    while True:
        command = input('Enter A Command\n : ')
        if command == 'Add':
            rules = addRule(rules,input('  Enter The ShortCut You Want To Add\n   : '),input('  Enter The Result You Want To Add\n   : '))
        elif command == 'Remove':
            rules = removeRule(rules,input('  Enter The ShortCut You Want To Remove\n   : '))
        elif command == 'Look':
            print('    '+'#####################\n')
            for key, value in rules.items():
                print('    ',key,'→',value)
                print('')
            print('    '+'#####################')
        elif command == 'Write':
            string = mapStr(input('  Write The Input Word, Setence, String, Or Text\n   : '),rules)
            print(string)
            string = ''
        elif command == 'End':
            break
        else:
            print('  Not A Known Command')
            print('  Commands')
            print('    Add - Adds A ShortCut Rule')
            print('    Remove - Removes A ShortCut Rule')
            print('    Look - Shows The ShortCut Rules')
            print('    Write - Lets User Type Words, Setences, Strings, Or Texts Using The ShortCuts')
            print('    End - Ends Program')

if __name__ == "__main__":
    main()


