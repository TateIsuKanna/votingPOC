import secrets
for i in range(int(input("人数:"))):
    print("http://example.com/?id="+secrets.token_urlsafe())
