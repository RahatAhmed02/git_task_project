# Ask user to enter their name and store as variable
user_name_input = str(input("Please enter your name: "))

# Print greeting message and domain name using f-string embedded variable containing user name
print(f"""
Hello {user_name_input}, welcome to your very own website.
This your website domain name: www.{user_name_input.lower().replace(" ", "")}.com
""")
