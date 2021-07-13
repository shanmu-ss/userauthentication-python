import os
import sys

#
def Groupinfo(group):
        if not group:
        print('Error: missing group')
        else:
        try:
            with open('tables/groups/' + group + '.txt') as f:
                lines = f.readlines()
                for line in lines:
                    print(line.replace('\n',''))
        except FileNotFoundError:
            print ('Error: invalid group')
            pass

#
def SetBuildingType(building, type):
    if not building:
    print('Error: missing building name')
    elif not type:
    print('Error: missing setbuilding type')
    else:
    with open('tables/buildings' + type + '.txt', 'a+') as f:
        f.write(building + '\n')
        print('Sucess')

#
def printUsage():
    print('usage: portal <operation> [<args>]\n')
    print('These are supported operation:\n')
    print('\tAddUser username password')
    print('\tAuthenticate username password')
    print('\tSetGroup username group')
    print('\tGroupInfo group')
    print('\tSetBuildingType building buildingType')
    print('\tAddAccess when group buildingType')
    print('\tCanAccess when user building')

def main():
    try:
        if not os.path.exists('tables'):
            os.mkdir('tables')
        if not os.path.exists('tables/groups'):
            os.mkdir('tables/groups')
        if not os.path.exists('tables/buildings'):
            os.mkdir('tables/buildings')
        if not os.path.exists('tables/access'):
            os.mkdir('tables/access')
        
        open('tables/user.txt', 'a+')
    except OSError:
        print('Error: unable to create storage')
    
    operation, arg1, arg2, arg3 = '', '', '', ''

    try:
        operation = sys.argv[1]
        arg1 = sys.argv[2]
        arg2 = sys.argv[3]
        arg3 = sys.argv[4]
    except Exception:
        pass

    if len(sys.argv) == 1:
        printUsage()
    else:
        if(arg1.find('') != -1 or arg2.find('') != -1 or arg3.find('') != -1):
            print('Error: invalid arguments. arguments can not contain space')
        else:
            if operation == 'AddUser':
                AddUser(arg1, arg2)
            elif operation == 'Authenticate':
                Authenticate(arg1, arg2)
            elif operation == 'SetGroup':
                SetGroup(arg1, arg2)
            elif operation == 'GroupInfo':
                Groupinfo(arg1)
            elif operation == 'SetType':
                SetType(arg1, arg2)
            elif operation == 'TypeInfo':
                TypeInfo(arg1)
            elif operation == 'AddAccess':
                AddAccesss(arg1, arg2, arg3)
            elif operation == 'CanAccess':
                CanAccess(arg1,arg2,arg3)
            else:
                print('Error: invalid operation')

if __name__ == '__main__':
    main()
