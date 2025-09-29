from user import User

def main():
    while True:
        print("\n=== User System ===")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            User.signup(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            User.login(username, password)

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
