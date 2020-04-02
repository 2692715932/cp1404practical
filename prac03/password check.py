"""Add password check program
   https://github.com/2692715932/cp1404practicals
"""
def main():
    name_of_user=input("Waht is your password? =>")
    number_of_password = method_name(name_of_user)
    print("*"*number_of_password)


def method_name(name_of_user):
    number_of_password = len(name_of_user)
    return number_of_password


main()