from email_sender import is_valid


def send_user_notification(email):
    if not email or not is_valid(email):
        return

    print(f'Send user notification')