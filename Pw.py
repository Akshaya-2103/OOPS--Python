from AbstractPassword import AbstractPassword

class Password(AbstractPassword):
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

