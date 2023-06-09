class Personal_Information:
    def __init__(self):
        self.first_name = input('Please enter your first name: ')
        self.lastname = input('Please enter your last name: ')
        self.age = float(input('Please enter your age as digits: '))
        self.national_code = input('Please enter your national code as digits: ')
        self.start_study_year = int(input('Please enter your study year as digits: '))

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
