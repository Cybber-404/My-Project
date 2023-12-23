# This is a trial of my skills and what I've learnt so for now
# I have no idea how to generate GUI's yet but this will have to do for
print('WELCOME TO MY SITE')
print('PLEASE SIGN UP TO CONTINUE')
acc_name = var1 = input('Name: ')
acc_email = var2 = input('Email: ')
acc_pass = var3 = input('Password: ')
acc_pass2 = var4 = input('Confirm Password: ')
if acc_pass != acc_pass2:
    print('Password does not match')
# I have no idea how the breakpoint function works, but it seems to do what I want, so I will use it for now.
    breakpoint(acc_pass2)
ans = input('Would you like to review your account info? ').lower()
if ans == 'yes':
    print('')
    print('Account name is > ' + acc_name)
    print('Your email is > ' + acc_email)
    print('Your password is > ' + acc_pass)
    print('')
elif ans == 'no':
    print('Very well then please login to have full access')
# This is the log-in section
print('PLEASE LOG IN HERE!')
log_acc_name = input('Name: ')
if log_acc_name != acc_name:
    print('Name does not exist in the database!')
    breakpoint(log_acc_name)
log_acc_email = input('Email: ')
if log_acc_email != acc_email:
    print('Email is not recognized!')
    breakpoint(log_acc_email)
log_acc_pass = input('Password: ')
if log_acc_pass != acc_pass2:
    print('Wrong password!')
    breakpoint(log_acc_pass)
print('WELCOME TO MY TRAINING SITE\nTHANK YOU FOR LOGGING IN\nENJOY!')
