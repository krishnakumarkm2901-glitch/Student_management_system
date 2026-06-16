import json
import os
class Student:
    def __init__(self,student_id,name,address,phone_number,age,course):
        self.student_id = student_id
        self.name = name
        self.address =address
        self.phone_number =phone_number
        self.age  =age
        self.course =course
    
    def to_dict(self):
        return{
        "student_id" : self.student_id,
        "name" : self.name,
        "address" : self.address,
        "phone_number" : self.phone_number,
        "age" : self.age,
        "course" : self.course
        }
    
class Student_management_system:
    FILE_NAME = "student.json"

    def login(self):
        user={
            "admin":{
                "password" :  "admin1234",
                "role" : "admin"
                },
                "staff" : {
                    "password" : "staff1234",
                    "role" : "staff"
                } 
            }
        print("****LOGIN****")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username in  user and user[username]["password"] == password:
            self.role = user[username]["role"]
            print("\nLogin Successful!!..")
            return True
        else:
            print("Invalid Login..")
            return False

    def __init__(self):
        self.students = self.load_data()
        self.role = None
        
        # if self.students is None:
        #     self.students = []

    def load_data(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as file:
                return json.load(file)
            return []
        
    def save_data(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(self.students, file,indent=6)

    def add_student(self):
        student_id=input("Enter the Student ID: ")
        for student in self.students:
            if student[student_id] == student_id:
                print("This Student aldready exist. ")
                return
        name = input("Enter the Name: ")
        address =input("Enter the Address:")
        phone_number = input("Enter the Phone Number: ")
        age = input("Enter the Age: ")
        course = input("Enter the Course: ")

        New_student=Student(student_id,name,address,phone_number,age,course)
        
        self.students.append(New_student.to_dict())
        self.save_data()

        print("Student Added Sucessfully: ")
    
    def view_student(self):
        if not self.students:
            print("No Student record found. ")
            return
        print(" \n{:<10}{:<50}{:<75}{:<10}{:<3}{:<30}".format  )
        print("-" * 100)

        for student in self.students:
            print("{:<10}{:<50}{:<75}{:<10}{:<3}{:<30}".format(
            student["student_id"],
            student["name"],
            student["address"],
            student["phone_number"],
            student["age"],
            student["course"]
            ))
    
    def search_student(self):
        student_id=input("Enter the Student_ID: ")
        for student in self.students:
            if student["student_id"] == student_id:
                print("\nStudent is found. ")
                print(student)
                return
        print("Student is not found. ")
    
    def update_student(self):
        student_id = input("Enter the Student_ID: ")
        for student in self.students:
            if student["student_id"] == student_id:
                student["name"]=input(f"Enter the name:({student['name']}):") or student["name"]
                student["address"]=input(f"Enter the Address:({student['address']}):") or student["address"]
                phone_number =input(f"Enter the phone_number:({student['phone_number']}):")
                if phone_number:
                    student["phone_number"] = phone_number 
                age =input(f"Enter the age:({student['age']}):")
                if age:
                    student["age"] = int(age) 
                student["course"]=input(f"Enter the course:({student['course']}):") or student["course"]
                self.save_data()
                print("Student updated. ")

                return
            print("Student not found. ")
    def delete_student(self):
                student_id = input("Enter the Student_ID to delete: ")
                for student in self.students:
                    if student["student_id"] == student_id:
                        self.students.remove(student)
                        self.save_data()
                        print("Student deleted Successfully. ")
                        return
                    print("Student not found. ")

    def menu(self):
        while True:
            print("****Student_management_system****")
            if self.role =="admin":
                print("1. Add Student")
                print("2. View Student")
                print("3. Search Student")
                print("4. Update Student")
                print("5. Delete Student")
                print("6.Exit")
            
            elif self.role == "staff":
                print("1. View Student")
                print("2. Search Student")
                print("3. Update Student")
                print("4. Exit")

            choice=input("Enter the Choice: ")

            if self.role == "admin":
                if choice == "1":
                    self.add_student()
                elif choice == "2":
                    self.view_student()
                elif choice == "3":
                    self.search_student()
                elif choice == "4":
                    self.update_student()
                elif choice == "5":
                    self.delete_student()
                elif choice == "6":
                    print("Thankyou for using the Student Management System")
                else:
                    print("Your choice is invalid so please enter the correct choice. ")

            elif self.role == "staff":
                if choice == "1":
                    self.view_student()
                elif choice == "2":
                    self.search_student()
                elif choice == "3":
                    self.update_student()
                elif choice == "4":
                    print("Thankyou for using the Student Management System")
                else:
                    print("Your choice is invalid so please enter the correct choice. ")

if __name__ == '__main__':
    sms=Student_management_system()
    
    if sms.login():
        sms.menu()