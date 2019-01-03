#C:\Python\python.exe -i "C:\Python\my_python\brk_the_code\brkthecode.py"

import json
from anytree import Node, RenderTree, Walker

dataset = open(r'C:\Python\my_python\brk_the_code\IFSLabs_BrkTheCode_DataSet.txt').read()
#print(dataset)

info = json.loads(dataset)
#print (info)

print (info['id'])
print (info['generatedOn'])
#print (info['data'])
#cnt = 0
act = 0
routes = list()
steps = list()
shortest = list()
#s = 0

for item in info['data']:
#    print (s, ':  ', item)
#    s += 1
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
    #print (sum_weight)
    #print (cnt)

    try:
        #print('farest station: ', info['data'][cnt])
        routes.append(info['data'][cnt])
        steps.append(step);
    except:
        #print('farest station: ', info['data'][cnt-1])
        routes.append(info['data'][cnt-1])
        steps.append(step-1);

    act += 1
    
#print (routes)
#print (steps)

s = 0

for item in info['data']:
    print (s, ':  ', item, ':  ', steps[s])
    s += 1
    
    
    
'''
tree_list = list()
#tree_list.append(Node(info['data'][0]))
tree_list.append(Node(0))
j = 0

for step in steps:
    i = 1
    while i <= step:
        #if j == 0:
        #    tree_list.append(Node(info['data'][i+j]))
        #else:
        #tree_list.append(Node(info['data'][i+j], parent = tree_list[j]))
        tree_list.append(Node(i+j, parent = tree_list[j]))
        i += 1
    
    
    
    j += 1


print (tree_list)
print (RenderTree(tree_list[0]))
print (j)

w = Walker()
print(w.walk(tree_list[0], tree_list[-1]))
'''

'''
#legegyszerűbb fifo út: - út:43
list2 = list()
i = 0
sum_route = 0
next_step = steps[i]
sum_route += next_step

while sum_route < len(steps)-1 and i < 200:
    next_step = steps[sum_route]
    list2.append(sum_route)
    sum_route += next_step
    i += 1
    

print (sum_route)
print (i)
print (list2)
'''
#todo: amit előre látunk listát(steps lista) azokon belül a MAX érték keresése és azokon ugyanez
'''
next_range = steps[0]
i = 0
max_value = 0
place = 0
while i < next_range:
    i += 1
    if steps[i] > max_value:
        max_value = steps[i]
        place = i

print (place, ':', max_value)

next_range = max_value #steps[place]
i = 0
max_value = 0
#place = 0
while i < next_range:
    i += 1
    if steps[place + i] > max_value:
        max_value = steps[place + i]
        place += i

print (place, ':', max_value)

next_range = max_value #steps[place]
i = 0
max_value = 0
#place = 0
while i < next_range:
    i += 1
    if steps[place + i] > max_value:
        max_value = steps[place + i]
        place += i

print (place, ':', max_value)
'''

'''
# MAX értékek választásával - út:49
stations = list()

def find_max(p_max_value, p_place):
    if p_place + p_max_value >= 199:
        return()
    next_range = p_max_value
    i = 0
    max_value = 0
    place = p_place
    
    while i < next_range:
        i += 1
        #print ('i=',i, 'place+i:',place+i, ':', steps[place+i], ':', max_value)
        if steps[p_place + i] >= max_value:
            max_value = steps[p_place + i]
            place = i
        
    #print ('place=', place, 'p_place=', p_place, 'max_v:', max_value)
    print ('stop_station:', p_place + place)
    stations.append(p_place + place)
    find_max(max_value, p_place + place)

find_max(steps[0], 0)

print (len(stations), 'stops:',stations)
'''

stations = list()
# MAX(actual position + max_step) --> út:40
def find_max(p_max_value, p_place):
    if p_place + p_max_value >= len(steps)-1:#199:
        stations.append(p_place + p_max_value)
        return()
    next_range = p_max_value
    i = 0
    max_value = 0
    place = p_place
    
    while i < next_range:
        i += 1
        #print ('i=',i, 'place+i:',place+i, ':', steps[place+i], ':', max_value)
        if steps[p_place + i] + p_place + i > max_value:
            max_value = steps[p_place + i] + p_place + i
            place = i
        
    #print ('place=', place, 'p_place=', p_place, 'max_v:', max_value)
    #print ('stop_station:', p_place + place)
    stations.append(p_place + place)
    find_max(steps[p_place + place], p_place + place)

find_max(steps[0], 0)

print (len(stations), 'stops:',stations)

#export to JSON
solution = {}
solution['answer'] = stations
#print (solution)
with open (r'C:\Python\my_python\brk_the_code\answer.txt', 'w') as outfile:
    json.dump(solution, outfile)



