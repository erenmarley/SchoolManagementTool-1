"""
  @Author: Eren Mercan
  @Date: 14.10.2023
  @About: This is school management tool
"""

class SchoolManagementTool():

    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []
        self.faculties = []
        self.departments = []
        self.path = "data/"
        self.load_students_from_file()
        
        print("School Management System is Initialized.")


    def load_students_from_file(self):
        try:
            with open(self.path + "student_database.txt", "r") as file:
                for line in file:
                    student_info = line.strip().split(",")
                    self.students.append({
                        "ID": student_info[0],
                        "name": student_info[1],
                        "surname": student_info[2],
                        "student_no": student_info[3],
                        "student_class": student_info[4],
                        "faculty_name": student_info[5],
                        "department": student_info[6]
                    })
        except FileNotFoundError:
            print("No student database file found.")

    def save_students_to_file(self):
        with open(self.path + "student_database.txt", "w") as file:
            for student in self.students:
                file.write(f"{student['ID']},{student['name']},{student['surname']},{student['student_no']},{student['student_class']},{student['faculty_name']},{student['department']}\n")

    def list_all_students(self):
        if len(self.students) == 0:
            print("No students in the database.")
        else:
            print("All students:")
            for student in self.students:
                print(f"ID: {student['ID']}, Name: {student['name']}, Surname: {student['surname']},Student No: {student['student_no']},Student Class: {student['student_class']}")

    def add_student(self, name, surname, student_no, student_class, faculty_name, department):
        if len(self.students) == 0:
            new_id = 1
        else:
            ids = [int(student["ID"]) for student in self.students]
            new_id = max(ids) + 1
        self.students.append({
            "ID": new_id,
            "name": name,
            "surname": surname,
            "student_no": student_no,
            "student_class": student_class,
            "faculty_name": faculty_name,
            "department": department
        })
        print(f"Student {name} {surname} added successfully.")

    def add_students(self, students_list):
        for student in students_list:
            self.add_student(*student)
        print("Students added successfully.")

    def remove_student(self, student_id):
        for student in self.students:
            if student['ID'] == student_id:
                self.students.remove(student)
                print(f"Student with student ID {student_id} named {student['name']} {student['surname']} removed successfully.")
                return
        print(f"No student with student id {student_id} found.")

    def edit_student(self,student_no,name,new_qualification,):


        condition=input("What type of the qualification do you want to change? "
        "Please write: name / surname / student_class / faculty_name / department / student_no \n"
        "Please write 0 to exit. \n ")


        if condition =='name':
            for student in self.students:
               if student['student_no'] == student_no:
                student['name'] = new_qualification
                print(f"Qualification of student with student no {student_no} changed to {new_qualification}.")
        elif condition =='surname':
          for student in self.students:
            if student['student_no'] == student_no:
                student['surname'] = new_qualification
                print(f"Qualification of student with student no {student_no} changed to {new_qualification}.")
        elif condition =='student_class':
           for student in self.students:
            if student['student_no'] == student_no:
              student['student_class'] = new_qualification
              print(f"Qualification of student with student no {student_no} changed to {new_qualification}.")
        elif condition =='faculty_name':
          for student in self.students:
            if student['student_no'] == student_no:
              student['faculty_name'] = new_qualification
              print(f"Qualification of student with student no {student_no} changed to {new_qualification}.")
        elif condition =='department':
             for student in self.students:
              if student['student_no'] == student_no:
                student['department'] = new_qualification
                print(f"Qualification of student with student no {student_no} changed to {new_qualification}.")
        elif condition =='student_no':
          for student in self.students:
            if student['name'] == name:
                student['student_no'] = new_qualification
                print(f"Qualification of student with name {name} changed to {new_qualification}.")
        elif condition =="0":
          for student in department_students:
            break


          return

    def find_student_from_name(self, name):
        found_students = []
        for student in self.students:
            if student['name'] == name:
                found_students.append(student)
        if len(found_students) == 0:
            print(f"No student with name {name} found.")
        else:
            print(f"Students with name {name}:")
            for student in found_students:
                print(f"Name: {student['name']}, Surname: {student['surname']}, Student No: {student['student_no']}")

    def list_faculties(self):
        if len(self.faculties) == 0:
            print("No faculties in the database.")
        else:
            print("Faculties:")
            for faculty in self.faculties:
                print(faculty)

    def list_faculty_students(self, faculty_name):
        faculty_students = []
        for student in self.students:
            if student['faculty_name'] == faculty_name:
                faculty_students.append(student)
        if len(faculty_students) == 0:
            print(f"No students in the faculty {faculty_name}.")
        else:
            print(f"Students in the faculty {faculty_name}:")
            for student in faculty_students:
                print(f"Name: {student['name']}, Surname: {student['surname']}, Student No: {student['student_no']}")

    def list_departments(self):
        if len(self.departments) == 0:
            print("No departments in the database.")
        else:
            print("Departments:")
            for department in self.departments:
                print(department)

    def list_department_students(self, department):
        department_students = []
        for student in self.students:
            if student['department'] == department:
                department_students.append(student)
        if len(department_students) == 0:
            print(f"No students in the department {department}.")
        else:
            print(f"Students in the department {department}:")
            for student in department_students:
                print(f"Name: {student['name']}, Surname: {student['surname']}, Student No: {student['student_no']}")

    def __del__(self):
        self.save_students_to_file()
        print("Database saved successfully.")



