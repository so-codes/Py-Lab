# create a interface which will accept email id from user and test whether it is valid or not.

def validate_email(email):

    if email == '@gmail.com':
        return False

    if len(email) > 7:
        if email.count("@") == 1:
            if email.count(".") == 1:
                return True
    return False

print("Enter the email id: ")
email = input()
if validate_email(email):
    print("Valid email id")
else:
    print("Invalid email id")
