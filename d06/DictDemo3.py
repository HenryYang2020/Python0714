users={'John':(170, 60), "Mary":(160, 48)}
users = [
            {'name':'John', 'h':170, 'w':60},
            {'name':'Mary', 'h':160, 'w':48}
        ]
for user in users:
    h=users.get('h')/100
    print(h)