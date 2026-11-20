
# Welcome Program

def display_welcome():
    print("=" * 35)
    print("       Welcome to My Python Project")
    print("=" * 35)


def display_user_info():
    name = "Manal"
    field = "Applied Linguistics"
    interest = "Software Development"

    print(f"\nHello! My name is {name}.")
    print(f"My academic field is {field}.")
    print(f"My interest is {interest}.")


def main():
    display_welcome()
    display_user_info()
    print("\nThank you for visiting my project!")


if __name__ == "__main__":
    main()
