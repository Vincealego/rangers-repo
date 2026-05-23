# ==================== STUDENT DATA ====================
name = "John"
date_of_birth = "2005-10-15"
age = 25
location = "London"
country = "UK"
weight = 70.5
year_of_study = 2025
student_id = "12345"

classes = ["Math", "Science", "English"]
marks = {"Math": 10, "Science": 20, "English": 30}

majors = ("Math", "Science", "English")
minors = (("History", "Geography"), ("Biology", "Chemistry"))


def getName(name):
    return name


def getProfile(name, age, location, country, date_of_birth):
    print(f"My name is {name}")
    print(f"My age is {age}")
    print(f"My location is {location}")
    print(f"My country is {country}")
    print(f"My date of birth is {date_of_birth}")


def getClasses(classes):
    for i in classes:
        print(f"I am doing {i}")


def getMarks(marks):
    for key, value in marks.items():
        print(f"I got {value} in {key}")


def getGrade(marks):
    for key, value in marks.items():
        if value >= 90:
            print(f"I got {value} in {key} which is an A")
        elif value >= 80:
            print(f"I got {value} in {key} which is a B")
        elif value >= 70:
            print(f"I got {value} in {key} which is a C")
        elif value >= 60:
            print(f"I got {value} in {key} which is a D")
        else:
            print(f"I got {value} in {key} which is an F")


# ==================== MAIN PROGRAM ====================

print("=== Student Profile ===\n")

my_name = getName("Marie")
print(f"My name is {my_name}\n")

getGrade(marks)
print()

# 1. Print Majors
print("My Majors:")
for major in majors:
    print(f"- {major}")
print()

# 2. Print Minors
print("My Minors:")
for group in minors:
    print(f"- {group[0]} and {group[1]}")
print()

# 3. Interactive While Loop
print("You can now ask for information. Type 'close' to exit.\n")

while True:
    user_input = input("What information do you want? (name, profile, classes, marks, grades, majors, minors): ").lower().strip()
    
    if user_input == "close":
        print("Goodbye!")
        break
    elif user_input == "name":
        print(f"My name is {name}")
    elif user_input == "profile":
        getProfile(name, age, location, country, date_of_birth)
    elif user_input == "classes":
        getClasses(classes)
    elif user_input == "marks":
        getMarks(marks)
    elif user_input == "grades":
        getGrade(marks)
    elif user_input == "majors":
        for major in majors:
            print(f"- {major}")
    elif user_input == "minors":
        for group in minors:
            print(f"- {group[0]} and {group[1]}")
    else:
        print("Sorry, I don't understand that.")
    
    print()