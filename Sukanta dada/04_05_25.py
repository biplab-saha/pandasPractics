import pandas as pd
file=pd.read_csv('student_scores.csv')

df=pd.DataFrame(file)
print(df)


#find the average marks for all the students
average_=df["marks"].mean()
print('the average marks of all the students is:',average_)
print("_"*50)

#Find out students who score d above 80
score_=df[df['marks']>80]
print("The scoe above 80:",score_)
print("_"*50)
#Sort students by marks in decending order
sort_=df.sort_values(by="marks",ascending=False)
print("Sorting students by marks in decending order:",sort_)
print("_"*50)

#Find how many students got grade 'A'
grade_=df[df['grade']=='A']
print(grade_)
print("_"*50)

#Show students who failed
fail_=df[df['marks']<60]
print("Students who have failed:",fail_)
print("_"*50)

abc=[df['grade']==df['marks']].apply(lambda x:'Pass' if x>=70 else 'fail')
print(abc)
#standerd deviation
'''abc=np.std(df['marks'])
print(abc)'''