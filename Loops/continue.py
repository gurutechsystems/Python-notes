#To move control from one iteration to another even when conditions are met, we use the 'continue' keyword.
#Continue keyword forces the loop to execute the next iteration of the loop while skipping the rest of the code inside the loopfor the current iteration only

#loop from 1 to 10

print('\n# Using continue statement in a loop')
for i in range(1,11):
    # If i is equals to 6,
	# continue to next iteration
	# without printing
    if i==3:
        continue
    else:
        # otherwise print the value of i
        #print(i) results will be displayed vertically
        print(i,end='') #results will be displayed horizontally