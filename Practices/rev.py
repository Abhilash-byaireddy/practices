s = "Hello World"

# Define a recursive lambda and call it immediately
reverse = (lambda f: lambda x: f(f, x))(lambda f, s: s[-1] + f(f, s[:-1]) if s else "")

print(reverse(s))
