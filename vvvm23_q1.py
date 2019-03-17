import time
import sys

# My functions here
def align(seq_1, seq_2):
    # Set scores for alignments
    MATCH_A = 4 # A - A
    MATCH_C = 3 # C - C
    MATCH_G = 2 # G - G
    MATCH_T = 1 # T - T
    MISMATCH = -3 # X Y
    GAP = -2 # X - _

    # Generate scoring and trace matrix
    # Both matrices will be n+1 X m+1 where n is length of seq_1 and m is length of seq_2
    n = len(seq_1)
    m = len(seq_2)
    score = [[None for j in range(m+1)] for i in range(n+1)]
    trace = [[None for j in range(m+1)] for i in range(n+1)]

    # Define initial state
    # Could may redefine this using list comprehension
    score[0][0] = 0
    trace[0][0] = 'E'
    for j in range(1, m+1):
        score[0][j] = j*GAP
        trace[0][j] = 'L'
    for i in range(1, n+1):
        score[i][0] = i*GAP
        trace[i][0] = 'U'



# Template functions: 
def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# Template code to open file
'''
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()'''

# Start timer
start = time.time()

# My code here
best_score = 99999999999999999999999999999999999999999999
best_alignment = ['A', 'A']
# Stop the timer
stop = time.time()
time_taken=stop-start

align(['A', 'T', 'T', 'G'],['A', 'T', 'T', 'G'])

print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)