import secrets
n=int(input("人数:"))
for i in range(n):
    print("http://example.com/?id="+secrets.token_urlsafe())
