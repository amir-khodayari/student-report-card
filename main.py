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
    from Information import *

    obj1 = Personal_Information()
    obj2 = Scores()

    obj1.p_display()
    obj2.s_display()

    f = open(f'{obj1.national_code}.txt', 'w+')
    f.write('First_Name: %s\n' % obj1.first_name)
    f.write('Last_name: %s\n' % obj1.lastname)
    f.write('Age: %d\n' % obj1.age)
    f.write('National_code: %s\n' % obj1.national_code)
    f.write('Start_Study_year: %d\n' % obj1.start_study_year)
    f.write('Mathematics_Score: %d\n' % obj2.MS)
    f.write('Physics_Score: %d\n' % obj2.PS)
    f.write('Computer_Science_Score: %d\n' % obj2.CS)
    f.write('History_Score: %d\n' % obj2.HS)
    f.close()
