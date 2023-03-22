current_users = ['john', 'mary', 'jane', 'steve', 'mike']
new_users = ['joe', 'JANE', 'steve', 'carol', 'MIKE']

for user in new_users:
    if user.lower() in [u.lower() for u in current_users]:
        print(f"Sorry, {user} is already taken. Please enter a new username.")
    else:
        print(f"Great, {user} is available!")