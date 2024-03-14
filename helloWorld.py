user_name_input = str(input("Please enter your name: "))

print(f"""
Hello {user_name_input}, welcome to your very own website.
This your website domain name: www.{user_name_input.lower().replace(" ", "")}.com
""")
