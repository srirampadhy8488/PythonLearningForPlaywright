user_emails = ["alice@test.com", "bob@test.com", "carol@test.com"]
user_active = [True, False, True]
for email, active in zip(user_emails, user_active):
    if active:
        print(email)
