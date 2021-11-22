# Seat-Allocation-Algorithm
# IIT Seat Allocation : 

Given 2 input files, the first file contains seats available for each of the 20 courses, such that total seats available are 10,000. Second file contains 10,000 lines, one for each rank holder. Each line contains roll number, rank, preference of course (in the order most preferred to least preferred)
Write a program that publishes the seat allotment (which student has got which course), such that each student gets their highest priority course possible.

Example Input file 1 : 

1, 620 

2, 480

.

.

.

20, 500


Example input file 2 : 

BECP1, 1234, 20,12,13,4,5,7,2,9,1,3,19,6,18,8,17,10,16,11,15,14

.

.

.


Example Output file : 

BECP1, 3

BECP2, 4

**Run the ```SeatAllotment.py```**

The input1.txt file should contain ```college number, seats available```

The input2.txt file should contain ```Roll no, Rank, list of college numbers``` i.e. prefrenced list

The output.txt file contains ```Roll no, college no``` i.e. where the seat is alloted of each student
