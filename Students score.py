# rah dastresi be print nomarat va lesson name ba halghe while  
students = [
    {
        'name' : 'ali mohammadi' ,
        'age' : 17 ,
        'ID' : '263123890' , 
        'field' : 'humanities' ,
        'class' : '11th grade' , 
        'lessons' : {
            'arabic' : 16 ,
            'geography' : 17 ,
            'history' : 14 ,
            'religion and life' : 19.5
        } 
    }, 
    {
        'name' : 'mohsen rezaei' ,
        'age' : 15 ,
        'ID' : '153173754' , 
        'field' : 'mathematics' ,
        'class' : '10th grade' , 
        'lessons' : {
            'mathematics' : 18 ,
            'physics' : 11 ,
            'chemistry' : 16 ,
            'geometry' : 19       
        }
    },
    {
        'name' : 'ahmad mahmoudi' ,
        'age' : 18 ,
        'ID' : '1368093115' , 
        'field' : 'empirical science' ,
        'class' : '12th grade' , 
        'lessons' : {
            'biology' : 13 ,
            'chemistry' : 16 ,
            'physics' : 18 ,
            'mathematics' : 20       
        }
    }
]
n = int (input('enter the number of new students'))
NewS = 0
while NewS < n :
    new = {'name' :'' ,'age' : '' ,'ID' : '' , 'field' : '' ,'class' : '' ,'lessons' : {   } }
    new['name'] = input('name')
    new['age'] = int(input('age'))
    new['ID'] = input('ID')
    new['field'] = input('field')
    new['class'] = input('class')
    if new['field'] == 'humanities':
        new['lessons']['arabic'] = float(input('arabic'))
        new['lessons']['geography'] = float(input('geography'))
        new['lessons']['history'] = float(input('history'))
        new['lessons']['religion and life'] = float(input('religion and life'))
    elif new['field'] == 'mathematics':
        new['lessons']['mathematics'] = float(input('mathematics'))
        new['lessons']['physics'] = float(input('physics'))
        new['lessons']['chemistry'] = float(input('chemistry'))
        new['lessons']['geometry'] = float(input('geometry'))
    elif new['field'] == 'empirical science':
        new['lessons']['biology'] = float(input('biology'))
        new['lessons']['chemistry'] = float(input('chemistry'))
        new['lessons']['physics'] = float(input('physics'))
        new['lessons']['mathematics'] = float(input('mathematics'))
    else :
        print('invalid')
        continue
    NewS += 1
    students.append(new)
i=0
while i<len(students):
#for student in students :
    p = list(students[i]['lessons'].keys())
    x=list(students[i]['lessons'].values())
    print("lesson_name=", p ,"nomarat=",x )
    i+=1
    #print(f"Name : {student['name']} , Age : {student['age']} , StudentID : {student['ID']} , Field :{student['field']} , Class : {student['class']} , Grades : {student['lessons']} , average : {sum(p)/len(p)}")
