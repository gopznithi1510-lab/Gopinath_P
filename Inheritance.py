class School:
    def __init__(self):
        self.name = input("Enter your name: ")
        
        try:
            self.SSLC_Mark = int(input("Enter your 10th Mark: "))
        except ValueError:
            print("Invalid input! Setting marks to 0.")
            self.SSLC_Mark = 0

    def group(self):
        if self.SSLC_Mark > 400:
            print("You are going to Group1")
            self.stream = "Group1"

        elif 300 < self.SSLC_Mark <= 400:
            print("You are going to Group2")
            self.stream = "Group2"

        elif 200 <= self.SSLC_Mark <= 300:
            print("You are going to Group3")
            self.stream = "Group3"

        else:
            print("Marks too low for group allocation")
            self.stream = None

        try:
            self.HSC_Mark = int(input("Enter your 12th Mark: "))
        except ValueError:
            print("Invalid input! Setting marks to 0.")
            self.HSC_Mark = 0


class College(School):
    def courses(self):
        if self.stream == "Group1" and self.HSC_Mark > 500:
            print("You are eligible to become a Doctor or Engineer")

        elif self.stream == "Group2" and self.HSC_Mark > 500:
            print("You are eligible to become a Nurse or Teacher")

        elif self.stream == "Group3" and self.HSC_Mark > 500:
            print("You are eligible to become a Manager or Accountant")

        else:
            print("You are not eligible based on your marks.")


# Creating object
obj = College()
obj.group()
obj.courses()
