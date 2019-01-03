#Zoltan Bedo    zoltan.bedo@ifsworld.com
#I'm new in python, but I thought, this language is the most effective for this interesting exercise :)
#
#C:\Python\python.exe -i "C:\Python\my_python\brk_the_code\brkthecode.py"

import json

#read the dataset JSON in
dataset = open(r'C:\Python\my_python\brk_the_code\IFSLabs_BrkTheCode_DataSet.txt').read()
info = json.loads(dataset)

print (info['id'])
print (info['generatedOn'])
#print (info['data'])

act = 0
steps = list()

#calculate and collect the maximum distance from the specific station into an array (steps)
for item in info['data']:
    step = 0
    cnt = act
    battery = item[0]
    sum_weight = item[1]
    
    while (battery >= sum_weight):
        try:
            step += 1
            cnt += 1
            sum_weight += info['data'][cnt][1]
        except:
            #print('reached last station')
            battery = sum_weight - 1

    try:
        steps.append(step);
    except:
        steps.append(step-1);

    act += 1

#for check the maximum steps from each stations
print (steps)

#for check, just print all station with its position in the array and with the maximum distance the drone can fly (steps)
s = 0
for item in info['data']:
    print (s, ':  ', item, ':  ', steps[s])
    s += 1
    


# it's a recursive function to find the possibly longest distance in the next segment
# I know the maximum distance that the drone can fly from the actual station (for example: the start station [0], the maximum distance is 6)
# I check the next 6 elements in the array (steps[]) from which station can the drone fly maximum
# so, if my actual position is 0 (steps[0]), then I investigate next 6 stations (steps[1..6]) which distance + position is the maximum:
# 0 :   [27, 7] :   6
# 1 :   [32, 5] :   7   1+7=8
# 2 :   [27, 3] :   6   2+6=8
# 3 :   [21, 1] :   4   3+4=7
# 4 :   [26, 8] :   5   4+5=9
# 5 :   [21, 3] :   4   5+4=9
# 6 :   [19, 3] :   3   6+3=9
#
# I choose the first one maximum: 4 :   [26, 8] :   5   4+5=9
#repeat the function until finish the array
#
#

stations = list()

def find_max(p_max_value, p_place):
    if p_place + p_max_value >= len(steps)-1:
        stations.append(p_place + p_max_value)
        return()
        
    next_range = p_max_value
    i = 0
    max_value = 0
    place = p_place
    
    while i < next_range:
        i += 1
        if steps[p_place + i] + p_place + i > max_value:
            max_value = steps[p_place + i] + p_place + i
            place = i
        
    stations.append(p_place + place)
    find_max(steps[p_place + place], p_place + place)

#call the recursive function
find_max(steps[0], 0)
print (len(stations), 'stops:',stations)

#export to JSON txt file
solution = {}
solution['answer'] = stations
with open (r'C:\Python\my_python\brk_the_code\answer.txt', 'w') as outfile:
    json.dump(solution, outfile)

