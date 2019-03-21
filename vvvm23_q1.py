import time
import sys

# My functions here
def align(seq_1, seq_2):
    # Set scores for alignments
    # Could hardcode in values once debugging done
    score_dict = {'A': 4,
                  'C': 3,
                  'G': 2,
                  'T': 1}

    # Generate scoring and trace matrix
    # Both maenerating empty matrix..')
    #matrices will be n+1 X m+1 where n is length of seq_1 and m is length of seq_2
    #print('Geq_1)
    i_seq_1 = tuple(score_dict[b] for b in seq_1)
    i_seq_2 = tuple(score_dict[b] for b in seq_2)
    n = len(seq_1)
    m = len(seq_2)
    score = [[None for j in range(m+1)] for i in range(n+1)]
    trace = [[None for j in range(m+1)] for i in range(n+1)]

    # Define initial state
    # Could may redefine this using list comprehension
    #print('Setting matrix intial conditions..')
    # -1 E; 0 U; 1 D; 2 L;
    score[0][0] = 0
    trace[0][0] = -1
    for j in range(1, m+1):
        score[0][j] = j*-2
        trace[0][j] = 2
    for i in range(1, n+1):
        score[i][0] = i*-2
        trace[i][0] = 0
    # Move down columns and then across rows, filling in score and trace matrix
    #print('Populating score and trace matrix..')
    for i in range(1, n+1):
        '''print('{0}%'.format((i-1)*100 / n), end='\r')
        sys.stdout.flush()'''
        for j in range(1, m+1):
            if not i_seq_1[i-1] == i_seq_2[j-1]:
                '''score[i][j], trace[i][j] = max((score[i-1][j-1] + score_dict['M'], 'D'),
                                           (score[i][j-1] + score_dict['-'], 'L'),
                                           (score[i-1][j] + score_dict['-'], 'U'),
                                           key=k)'''
                score[i][j], trace[i][j] = max((score[i-1][j-1] -3, 1),
                                           (score[i][j-1] -2, 2),
                                           (score[i-1][j] -2, 0))
            else:
                '''score[i][j], trace[i][j] = max((score[i-1][j-1] + score_dict[seq_1[i-1]], 'D'),
                                           (score[i][j-1] + score_dict['-'], 'L'),
                                           (score[i-1][j] + score_dict['-'], 'U'),
                                           key=k)'''
                score[i][j], trace[i][j] = max((score[i-1][j-1] + i_seq_1[i-1], 1),
                                           (score[i][j-1] -2, 2),
                                           (score[i-1][j] -2, 0))

    # Traverse traceback until end found.
    #print('Computing alignment via traceback..')       
    alignment = ['', '']
    i, j = n, m # Current index
    direction = trace[i][j]
    # Maybe here loop until either i or j is 0. Then immediately append remainder of string and gaps.
    while not direction == -1:
        # Append to front
        if direction == 0:
            i -= 1
            alignment[0] += seq_1[i]
            alignment[1] += '-'
        elif direction == 2:
            j -= 1
            alignment[0] += '-'
            alignment[1] += seq_2[j]
        elif direction == 1:
            i -= 1
            j -= 1
            alignment[0] += seq_1[i]
            alignment[1] += seq_2[j]

        direction = trace[i][j] # Get next direction

    '''import numpy as np
    print(np.array(score))
    print(np.array(trace))'''

    alignment = list(map(lambda x: x[::-1], alignment))
    return score[n][m], alignment

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
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()

# Start timer
start = time.time()
# My code here
best_score, best_alignment = align(seq1, seq2)
# Stop the timer
stop = time.time()
time_taken=stop-start

print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)