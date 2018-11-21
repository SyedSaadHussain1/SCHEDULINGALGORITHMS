name =[]
burst_time = []
arrival_time = []
finish_time =[]
waiting_time =[]


sum =int(0)
print "ENTER THE NUMBER OF THE PROCESS"
n = int(input())
print "PLEASE ENTER THE NAME OF THE PROCESS"
name = [str(raw_input()) for i in range(n)]
print "PLEASE ENTER THE ARRIVAL TIME OF THE PROCESSES"
arrival_time = [int(input()) for i in range(n)]
print "ENTER THE BURST TIME OF THE PROCESSES"
burst_time = [int(input()) for i in range(n)]

for i in range(n):
    for j in range(n-i-1):
        if(arrival_time[j]>arrival_time[j+1]):
            temp=arrival_time[j]
            arrival_time[j]=arrival_time[j+1]
            arrival_time[j+1]=temp
            temp2=burst_time[j]
            burst_time[j]=burst_time[j+1]
            burst_time[j]=temp2
            temp3=name[j]
            name[j]=name[j+1]
            name[j]=temp3

print "PROCESS NAME"+"\t"+"ARRIVAL TIME"+"\t"+"BURST TIME"

for i in range(n):
    print name[i],"\t\t\t",arrival_time[i],"\t\t\t\t",burst_time[i]
    finish_time = [int(arrival_time[i] + burst_time[i]) for i in range(n)]
    waiting_time=[int(finish_time[i]-arrival_time[i]) for i in range(n)]

for  i in range(n):
        sum += int(waiting_time[i])

print "WAITING TIME OF THE PROCESS"

for i in range(n):
    print name[i],"\t\t",waiting_time[i]

print "AVERAGE WAITING TIME OF THE PROCESS ",sum/n








