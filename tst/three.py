# create a interface which will accept email id from user and test whether it is valid or not.

def validate_email(email):

    if email.lower() == '@gmail.com' or email.lower() == '@yahoo.com':
        return False

    if email:
        if(email.lower().endswith('@gmail.com')) or (email.lower().endswith('@yahoo.com')):
            return True
    return False

print("Enter the email id: ")
email = input()

if validate_email(email):
    print("Valid email id")
else:
    print("Invalid email id")
