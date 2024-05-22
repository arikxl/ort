students = ['adam','arik','shon','maria','linda','eva','boris','jackov','ben','david','yermiyahu','zrubavel','esterika','korl','gad','niso','dan']

print(len(students))
def a_students(student):
    return student.startswith('d')
filter1 = list(filter(a_students, students))
print(filter1)

def long_name(student):
    return len(student) >5
filter2 = list(filter(long_name, students))
print(filter2)

def both(student):
    return len(student) > 5 and student.startswith('e')
filter3 = list(filter(both, students))
print(filter3)
