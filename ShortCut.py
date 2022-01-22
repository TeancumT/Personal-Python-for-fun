def mapStr(string,rules):
    for i in rules:
        string = string.replace(i[0],i[1])
    return string

def addRule(rules,start,end):
    rules += [[str(start),str(end)]]
    return eval(str(rules))

def removeRule(rules,start,end):
    a = ''
    for i in range(len(rules)):
        if rules[i] == [str(start),str(end)]:
            a = i
    
    if a != '':
        del rules[a]
        return eval(str(rules))
    else:
        print("Not Able To Remove")



def main():
    rules = []
    string = ''
    while True:
        command = input('Enter A Command\n : ')
        if command == 'Add':
            rules = addRule(rules,input('  Enter The ShortCut You Want To Add\n   : '),input('  Enter The Result You Want To Add\n   : '))
        elif command == 'Remove':
            rules = removeRule(rules,input('  Enter The ShortCut You Want To Remove\n   : '),input('  Enter The Result You Want To Remove\n   : '))
        elif command == 'Look':
            print('    '+'#####################\n')
            for i in rules:
                print('    ',i[0],'→',i[1])
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

