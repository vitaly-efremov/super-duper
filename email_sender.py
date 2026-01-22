def send_user_email(email: str | None):
    if not email:
        return

    print(f'Send super-duper email to {email}')