#opening the input1.txt which contains list of college and the seats available
f1=open('input1.txt','r')


#getting the the colleges which are separated in lines
list_of_colleges=f1.read().splitlines()


#declaring an empty dictionary
colleges={}


#declaring an empty 2-dimensional list
cl=[[0,0]]


#appending the college number and seats available into c1 which are separated by comma
for c in list_of_colleges:
    cl.append(c.split(', '))


#now inserting the elements of 2D list c1 into a dictionary colleges where key is college number and value is seats available of that particular college
for c in cl:
    if c[0]!=0:
        colleges[c[0]]=int(c[1])
#print(colleges)


#closing input1.txt as we have extracted all that data into lists and dictionary
f1.close()


#opening input2.txt which contains the roll number,  rank and prefrence list of colleges
f2=open('input2.txt','r')


#getting data of each student which is separated by lines
list_of_students=f2.read().splitlines()


#declaring an empty dictionary, a 2D list and a list to store prefrence list of each student
seatAlloted={}
s=[[]]
prefList=[]
#print(list_of_students)


#now inserting the students of 'list_of_students' to a 2d list s using comma as separator
for student in list_of_students:
    #print(student)
    s.append(student.split(', '))

#removing the empty first element
s.remove(s[0])


#iterating the list 's' to get the preferred list of each student
for a in s:
    prefList.append(a[2:])


'''Here we are iterating through the lists so as to allot each student a seat in a preferred college according
to his preference also checking whether the seat is available in that college if available then allot seat to him
and append his roll number and college alloted to seatAlloted dictionary where key is roll number of student
and value is college number in which he is alloted seat
if seat is not available then we check availabilty of seat in the next college according to his preference
list which he provided
'''
for i in range(0,len(prefList)):
    for j in range(0,len(prefList[i])):
        if prefList[i][j] in colleges and colleges[prefList[i][j]]>=1:
            seatAlloted[s[i][0]]=prefList[i][j]
            colleges[prefList[i][j]]-=1
            #print("alloted")
            break
            
print("Seats Alloted")

#closing the file input2.txt
f2.close()


#opening a new file output.txt in write mode to add the output to it
f3=open('output.txt','w')


#iterating through the seatAlloted dictionary and writing allotment of each student to it separated by new line
for seats in seatAlloted:
    f3.write(seats+":"+seatAlloted[seats]+"\n")


#closing the output file
f3.close()


#again opening the output.txt file in read mode and printing the output
o=open('output.txt','r')
output=o.read()
print(output)
