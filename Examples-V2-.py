from SchoolManagementTool import SchoolManagementTool

university = "MSKU"
my_system = SchoolManagementTool(university)
my_system.add_student("AA", "BB", 1234, "student_class", "faculty_name", "department")


# my_system.list_all_students()
# my_system.add_student("John", "Doe", "12345", "Class A", "Faculty of Science", "Computer Science")
# my_system.add_students([
#     ("Jane", "Smith", "54321", "Class B", "Faculty of Arts", "English Literature"),
#     ("Alice", "Johnson", "98765", "Class C", "Faculty of Science", "Physics")
# ])
# my_system.list_all_students()
# my_system.remove_student("54321")
# my_system.edit_student("98765","Alice", "Johnson","Class C","Faculty of Science", "Physics","Ali")
# my_system.find_student_from_name("John")
# my_system.list_faculties()
# my_system.list_faculty_students("Faculty of Science")
# my_system.list_departments()
# my_system.list_department_students("Computer Science")
