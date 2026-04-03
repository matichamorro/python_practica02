
def validate_email():
    email = input("Ingrese un email: ")
    validating = "El email no es válido."
    if email.count('@') == 1 and not email.startswith(('@','.')) and not email.endswith(('@','.')):
        email = email.split('@')
        if len(email[0]) >= 1 and email[1].count('.') >= 1:
                email_ending = email[1].split('.')
                if len(email_ending[1]) >= 2:
                    validating = "El email es válido."
    print(validating)
