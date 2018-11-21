
size = int(raw_input("PLEASE ENTER THE TOTAL NUMBER OF PROCESSES"))

process = [0] * size
arrival = [0] * size
burst = [0] * size

for i in range(size):
    process[i] = (raw_input("PLEASE ENTER PROCESS NAME"))
    arrival[i] = int(raw_input("PLEASE ENTER THE ARRIVAL TIME"))
    burst[i] = int(raw_input("PLEASE ENTER THE BURST TIME"))


start = [0] * size
turn = [0] * size
waiting_Time = [0] * size
turn_Time = [0] * size


for i in range(0, size):
    min1 = i
    for j in range(i + 1, (size)):
        if burst[min1] > burst[j]:
            temp1 = burst[j]
            burst[j] = burst[min1]
            burst[min1] = temp1

            temp2 = arrival[j]
            arrival[j] = arrival[min1]
            arrival[min1] = temp2

            temp3 = process[j]
            process[j] = process[min1]
            process[min1] = temp3

for j in range(size):
    if j == 0:
        start[j] = arrival[j]
        turn[j] = arrival[j] + burst[j]
    if j >= 1:
        start[j] = turn[j - 1]
        turn[j] = burst[j] + turn[j - 1]

for j in range(size):
      print(process[j], 'ARRIVAL TIME IS', arrival[j], 'THE PROCESS STARTS AT', start[j], 'AND AFTER ALL IT ENDS AT', turn[j])

for m in range(size):
    waiting_Time[m] = start[m] - arrival[m]
    turn_Time[m] = turn[m] - arrival[m]


sum1 = 0
sum2 = 0


for l in range(size):
    sum1 += waiting_Time[l]
    sum2 += turn_Time[l]
    print(process[l], 'WAITING TIME IS', waiting_Time[l])
    print(process[l], 'TURN AROUND TIME IS', turn_Time[l])


awaiting_Time = sum1 / size
aturn_Time = sum2 / size

print('AVERAGE WT=', awaiting_Time)
print('AVERAGE TA TIME=', aturn_Time)
