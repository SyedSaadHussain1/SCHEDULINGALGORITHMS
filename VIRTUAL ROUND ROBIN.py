burst_time = []
process_name = []
order = []
wait = []
remaining_bt = []
wait_input = []
turn_around = []


print "ENTER THE I/O CYCLE TIME"
input_wait = input()

print "ENTER THE NUMBER OF PROCESSES"
n = input()

wait = [int(0) for i in range(n)]

print "PLEASE ENTER THE NAME OF THE PROCESS"

process_name = [str(raw_input()) for i in range(n)]

print "PLEASE ENTER THE QUANTUM OF TIME"
quantum = input()


order = [int(input()) for i in range(n)]
print "ARRIVAL TIME OF PROCESS IS CONSIDERED 0"

arrival_time = [int(0) for i in range(n)]

print "PLEASE ENTER THE BURST TIME"

burst_time = [int(input()) for i in range(n)]
for i in range(n):
    for j in range(n - i - 1):
        if order[i] > order[i + 1]:
            temp = order[i]
            order[i] = order[i + 1]
            order[i + 1] = order[i]
            temp2 = process_name[i]
            process_name[i] = process_name[i + 1]
            process_name[i + 1] = temp2
            temp3 = burst_time[i]
            burst_time[i] = burst_time[i + 1]
            burst_time[i + 1] = temp3

print "PROCESS NAME " + "PROCESS ORDER" + "BURST TIME "+ "ARRIVAL TIME"

for i in range(n):
    print process_name[i] + "\t", order[1], "\t", burst_time[i], "\t", arrival_time[i]

print "WAITING FOR THE PROCESSES TO COMPLETE THE I/O"

remaining_bt = [int(burst_time[i]) for i in range(n)]
for i in range(n):
    if i%2 == 0:
        wait_input=[int(burst_time[i]+input_wait)]

t = int(0)
done = int(0)

while done == int(1):
    done = int(1)

for i in range(n):
    if remaining_bt[i] > 0:
        done = int(0)
        if remaining_bt[i]>quantum:
            t+=quantum
            remaining_bt[i] -= quantum
        else :
            t = t + remaining_bt[i]
            wait[i] = t - burst_time[i]
            if done == 1:
                break
sum = int(0)
print "TOTAL WAITING TIME FOR THE PROCESSES"

for i in range(n):
    print wait[i]
    sum += wait[i]

print "AVERAGE WAITING TIME"
print sum
print "\tNOW WE WILL CALCULATE THE FINAL TURNAROUND TIME"

turn_around=[int(burst_time[i]+wait[i]) for i in range(n)]
print "TURN AROUND TIME OF THE PROCESSES"
turn = int(0)

for i in range(n):
    print turn_around[i]
    turn += int(turn_around[i])

print "AVERAGE TURN AROUND TIME"
print turn/n