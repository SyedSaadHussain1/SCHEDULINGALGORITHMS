size = int(raw_input("ENTER THE NUMBER OF PROCESSES"))

process = [0] * size
arrival = [0] * size
burst = [0] * size
total_time = 0

for i in range(size):
    process[i] = (raw_input("PLEASE ENTER THE NAME OF THE PROCESS"))
    arrival[i] = int(raw_input("PLEASE ENTER THE ARRIVAL TIME"))
    burst[i] = int(raw_input("PLEASE ENTER THE BURST TIME"))
    total_time += burst[i]

quantum_time = int(raw_input("PLEASE ENTER THE QUANTUM TIME"))

turn = [0] * size
wt = [0] * size
rt = [0] * size
waiting_time = [0] * size
turn_time = [0] * size

for i in range(size):
    rt[i] = burst[i]


time = 0

while True:
    done = True
    for i in range(size):
        if rt[i] > 0:
            done = False
            if rt[i] > quantum_time:
                time += quantum_time
                rt[i] -= quantum_time
            else:
                time = time + rt[i]
                wt[i] = time - burst[i]
                rt[i] = 0

    if done == True:
        break

for i in range(size):
    turn[i] = burst[i] + wt[i]

for j in range(size):
    turn_time[j] = turn[j] - arrival[j]
    waiting_time[j] = turn[j] - arrival[j] - burst[j]

sum1 = 0
sum2 = 0

for k in range(size):
    sum1 += waiting_time[k]
    sum2 += turn_time[k]

awt = sum1 / size
atat = sum2 / size

for j in range(size):
    first1 = min(burst)
    runn = burst.index(first1)
    print(process[j], 'ARRIVAL IS AT', arrival[j],'EXECUTIONS STARTS AT',start[j], 'AND AFTER EXECUTION IT ENDS AT', turn[j])

print('AVERAGE WT=', awt)
print('AVERAGE TA TIME=', atat)


