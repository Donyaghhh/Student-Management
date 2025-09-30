Student_Grades={
    "Armin Zareie":{"math":17,"physic":12,"chemistry":9},
    "Anahita Salimi":{"math":15,"physic":8,"chemistry":20},
    "Zohre Ghaderi":{"math":10,"physic":10,"chemistry":15}
}
#-----------section1--------------------
tedad=0
total=0
for key,value in Student_Grades.items():
        total=sum(value.values())
        tedad=len(value)
        avr=total/tedad
        print("avr_scores=",avr, end=",")

print (20 * "*")

#print max_score for each Lesson
#--------section 2-------------------------
max_score=0
max_scores=[]
max_scores_k=[]
for key,values in Student_Grades.items():
    for key,value in values.items():
        if value > max_score:
            max_score=value
            max_score_key=key
            max_scores.append(max_score)
            max_scores_k.append(max_score_key)
print(max_scores+max_scores_k)

print(25 * "-")
#print score up 18
#-------section 3--------------------
pass_student=[]
f=True
for student,scores in Student_Grades.items():
    for key,value in scores.items():
        if scores>=18:
            pass_student.append(student)
        else:
            continue
print("scores up 18=",pass_student)
