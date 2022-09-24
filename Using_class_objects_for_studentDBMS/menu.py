from database import Database

obj = Database()


class Menu:

    def header(self):
        print('*****************')
        print('Chennai University')
        print('*****************')

    def homepage(self):
        print('\n1.Add Student Name\n2.Search Student Details\n3.Delete Student Name\n4.Show All Details\n5.Update '
              'Student Details\n0.exit')

    def process(self):
        user_action = int(input('Enter your action:'))
        self.header()
        match user_action:
            case 1:
                self.add_user()
            case 2:
                self.search_student_name()
            case 3:
                self.delete_student_name()
            case 4:
                obj.show_database()
            case 0:
                print('EXIT')
                exit()
            case default:
                print('Invalid Input')

    def add_user(self):
        student_name = input('Enter Student Name: ')
        student_age = input('Enter Age of the Student: ')
        student_phone = input('Enter Student Phone No: ')
        obj.insert_into_database(student_name, student_age, student_phone)

    def search_student_name(self):
        search_name = input('ENTER THE STUDENT NAME: ')
        obj.search_from_database(search_name)

    def delete_student_name(self):
        delete_name = input('Enter the Name to delete Student Details: ')
        obj.delete_from_database(delete_name)
