import requests


def check_username(name):
    headers = {
        "Host": "www.tiktok.com",
        "Referer": "https://www.tiktok.com/"
    }

    r = requests.get("https://www.tiktok.com/@" + name + "?lang=en&=", headers=headers)

    if len(r.text) > 178000:
        return True
    return False


def load_usernames(file):
    try:
        with open(file, "r") as f:
            for name in f:
                name = name.rstrip().lower()
                if check_username(name):
                    print("Username " + name + " is taken!")
                else:
                    print("Username " + name + " is available!")

    except FileNotFoundError:
        print("The file you provided could not be found!")


def main():
    while True:
        print("1. Check username by input.")
        print("2. Check username by .txt file.")
        try:
            choice = int(input(""))
            if choice > 2 or choice < 1:
                raise ValueError

            if choice == 1:
                name = input("Enter the username to check (without @): ").lower()
                if check_username(name):
                    print("Username " + name + " is taken!")
                else:
                    print("Username " + name + " is available!")

            elif choice == 2:
                load_usernames(input("Enter the path of the file to check: "))

        except ValueError:
            print("Invalid input!")
            pass
        except Exception as ex:
            print(ex)
            return


if __name__ == "__main__":
    main()