def get_student_info():
    ni = input('Enter your National code to search: ')
    try:
        with open(f"{ni}.txt", "r") as file:
            info = file.read()
            return info
    except FileNotFoundError:
        return "There is no Report Card with this National code"


Yn = input('Do you want to use the search engine?(Y/N) ')
if Yn.lower() == 'y':
    print(get_student_info())
else:
    import personal_information as ps


    class Personal_Information:
        def __init__(self, first_name, lastname, age, national_code, start_study_year):
            self.first_name = first_name
            self.lastname = lastname
            self.age = age
            self.national_code = national_code
            self.start_study_year = start_study_year

        def p_display(self):
            print(f'First Name: {self.first_name}\n'
                  f'Last Name: {self.lastname}\n'
                  f'Age: {self.age}\n'
                  f'National Code: {self.national_code}\n'
                  f'Start Study Year: {self.start_study_year}')


    class Scores:
        def __init__(self):
            self.MS = float(input('Please enter your mathematics score: '))
            self.PS = float(input('Please enter your Physics score: '))
            self.CS = float(input('Please enter your Computer Science score: '))
            self.HS = float(input('Please enter your History score: '))

        def s_display(self):
            print(f'Mathematics Score: {self.MS}\n'
                  f'Physics_Score: {self.PS}\n'
                  f'Computer_Science_Score: {self.CS}\n'
                  f'History_Score: {self.HS}')


    obj1 = Personal_Information(ps.First_Name, ps.Last_name, ps.Age, ps.National_code,
                                ps.Start_Study_year)

    obj2 = Scores()

    obj1.p_display()
    obj2.s_display()

    f = open(f'{ps.National_code}.txt', 'w+')
    f.write('First_Name: %s\n' % ps.First_Name)
    f.write('Last_name: %s\n' % ps.Last_name)
    f.write('Age: %d\n' % ps.Age)
    f.write('National_code: %s\n' % ps.National_code)
    f.write('Start_Study_year: %d\n' % ps.Start_Study_year)
    f.write('Mathematics_Score: %d\n' % obj2.MS)
    f.write('Physics_Score: %d\n' % obj2.PS)
    f.write('Computer_Science_Score: %d\n' % obj2.CS)
    f.write('History_Score: %d\n' % obj2.HS)
    f.close()


