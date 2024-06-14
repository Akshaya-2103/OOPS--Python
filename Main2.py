from Accessing import Student

def main():
    student = Student("OM","A001","OM1234")
    print("Name (Public):", student.name)
    print("Roll Number (Protected):", student._roll_number)
    print("Password (Private):", student.get_password())

if __name__ == "__main__":
    main()