class Password:
    def __init__(self, original_password, attempts):
        self.original_password = "Akshaya123"
        self.attempts = 3

    def authentication(self):
        while self.attempts > 0:
            user_input = input("Enter the password : ")

            if user_input == self.original_password:
                print("Welcome!")
                break
            else:
                self.attempts -= 1
                if self.attempts > 0:
                    print(f"Wrong password! You have {self.attempts} attempts left.")
                else:
                    print("Account blocked.")
                    break

pw = Password("Akshaya123",3)
pw.authentication()