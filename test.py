import os

# Access the secret as an environment variable
my_secret = os.environ.get("MY_SECRET")

if my_secret:
    print("Successfully retrieved the secret!")
else:
    print("Secret MY_SECRET is not set.")
