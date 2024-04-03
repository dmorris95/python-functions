#Task 1

grades = [85, 90, 94, 76, 92, 78, 97, 72, 65, 99]

def average_grade(f_grades):
    total = 0
    for x in f_grades:
        total += x
    
    return(total/len(f_grades))

print(average_grade(grades))


#Task 2

def min_max_grade(mgrade):
    min = mgrade[0]
    max = mgrade[0]
    for m in mgrade:
        if m <= min:
            min = m
    for n in mgrade:
        if n >= max:
            max = n
    return(f"The lowest grade is {min} and the highest grade is {max}.")
           
print(min_max_grade(grades))


#Task 3

#takes existing list of grades and outputs them as letter grades
def categorize_grades(cgrade):
    letter = ""
    for x in cgrade:
        if x >= 90:
            letter = "A"
        elif x >= 80 and x < 90:
            letter = "B"
        elif x >= 70 and x < 80:
            letter = "C"
        elif x >= 60 and x < 70:
            letter = "D"
        else:
            letter = "F"
        print(f"Your grade of {x} while be a(n) {letter}")

categorize_grades(grades)

    

