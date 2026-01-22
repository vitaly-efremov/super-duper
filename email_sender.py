def send_user_email(email: str | None):
    if not email and is_valid(email):
        return

    print(f'Send super-duper email to {email}')


def is_valid(email: str):
    return True