students =[ 
    {
        'name' : 'Ziba Ghaderi' ,
        'age' : 19 ,
        'ID' : 263123890 , 
        'field' : 'Computer' , 
        'lessons' : {
            'arabic' :{"id":100,"Country":"Arabestan","page_count":180} ,
            'geography' :{"id":46,"Country":"Iran","page_count":90},
            'history' :{"Teacher_name":"Fateme","unit":2,"page_count":200}
        }}, 
    {
            'name' : 'Ziba Mahmodi' ,
            'age' : 17 ,
            'ID' : '153173754' , 
            'field' : 'mathematics' , 
            'lessons' : {
            'mathematics' :{"id":100,"Country":"Arabestan","page_count":180},
            'physics' :{"id":46,"Country":"Iran","page_count":90},
            'chemistry' :{"Teacher_name":"Fateme","unit":2,"page_count":200},
            }


    }
]

n = int (input('enter the number of new students'))
NewS = 0
while NewS < n :
    new = {'name' :'' ,'age' : '' ,'ID' : '' , 'field' : '' ,'lessons' : {   } }
    new['name'] = input('name')
    new['age'] = int(input('age'))
    new['ID'] = input('ID')
    new['field'] = input('field')
    if new['field'] == 'Computer':
        new['lessons']['arabic'] = float(input('arabic'))
        new['lessons']['geography'] = float(input('geography'))
        new['lessons']['history'] = float(input('history'))
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
while i< len(students):
    p =list(students[i]['lessons']['arabic'].values())
    x=int(input("enter a new number"))
    students[0]['lessons']['geography']["page_count"]=x
    print(students)
    i+=1
    #print(f"Name : {students['name']} , Age : {students['age']} , StudentID : {students['ID']}, , average : {sum(p)/len(p)}",students['lessons']["page_count"])
