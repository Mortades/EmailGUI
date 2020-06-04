def readCredentials(file):
    # file is where put your password
    with open(file, "r") as Credentials:
        temp = Credentials.read().split("\n")
        email = temp[0]
        password = temp[1]
        return email, password


if __name__ == "__main__":
    email, password = readCredentials("Credentials.txt")
    print(email, password)
    a = 1