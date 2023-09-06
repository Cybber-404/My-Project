contacts = {
 'Amal': '0549115794', 'Wadud': '0246850933', 'Be Black': '0241992965', 'Mom': '0247946126',
 'Hussein': '0546834998', 'Masduuk': '0593886726', 'Mahama': '0207857253'
}
question = input('Would you like to open the program? ').lower()
while question == 'yes'.lower():
    print('WELCOME TO MY CONTACT PROGRAM!')
    name = input('What is your name? ')
    if name in contacts:
        print('Your number is: ')
        print(contacts.get(name))
        question3 = input('Would you like to continue? ').lower()
        if question3 == 'no'.lower():
            break
        else:
            continue    
    elif name not in contacts:
        print('Name Unrecognized')
        question2 = input('Would you like to add a new contact? ').lower()
        if question2 == 'yes'.lower():
            contacts.update(var=input('Add new contact: '))
            print('Your new number is ' + contacts.get('var'))
        elif question2 == 'no'.lower():
            print('Very Well then, Bye')
            break
        else:
            print('Wrong Input!')
            break
    else:
        print('Invalid Input!')
else:
    print('Invalid Input!')
