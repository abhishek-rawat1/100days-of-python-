def data_of_student():
    """It  takes student data"""
    name = (input("Enter student name : "))
    marks = []
    for i in range(3):
        mark = float(input('Enter marks : '))
        marks.append(mark)
    return(name,marks)


def report_card():
    """it genrate report card"""
    print("     .....Report Card.....     ")
    print(f'     Student name {  name }')
    for i in (marks):
        print(f"     marks = {i}")

name , marks = data_of_student()
report_card()

