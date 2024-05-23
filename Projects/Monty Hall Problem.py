import random

doors = [1,2,3]
statistics = open(r'.\Projects\Monty Hall Problem.txt', 'a+')
results = ['Changed and won.', 'Changed and lost.', "Didn't change and Won.", "Didn't change and Lost."]
times = int(input("How many time you want to play?  "))
n = times
# print(statistics.readlines())
def selecting_door():
    global selected_door
    selected_door = random.choice(doors)
def money_door():
    global door_of_money
    door_of_money = random.choice(doors)
def door_revealation():
    doors.remove(door_of_money)
    try:
        doors.remove(selected_door)
    except: pass
    global revealed_door
    revealed_door = random.choice(doors)
    doors.remove(revealed_door)
    doors.append(door_of_money)
    if selected_door not in doors:
        doors.append(selected_door)
def change():
    global change_or_not
    change_or_not = random.choice([0,1])
    global my_selection
    if change_or_not == 0:
        my_selection, change_or_not = selected_door, False
    else:
        for door in doors:
            if door == selected_door: continue
            my_selection = door
        change_or_not = True
def result():
    if my_selection == door_of_money: 
        if change_or_not == True:
            print(results[0])
            statistics.write(results[0])
            statistics.write("\n")
        else:
            print(results[2])
            statistics.write(results[2])
            statistics.write("\n")
    else: 
        if change_or_not == True:
            print(results[1])
            statistics.write(results[1])
            statistics.write("\n")
        else:
            print(results[3])
            statistics.write(results[3])
            statistics.write("\n")
def analysis():
    statistics.seek(0)
    stats = statistics.readlines()
    for i in range(len(stats)):
        gg = stats[i]
        stats[i] = gg[:-1]
    res0, res1, res2, res3 = 0, 0, 0, 0
    for i in stats:
        if i == results[0]: res0 += 1
        elif i == results[1]: res1 += 1
        elif i == results[2]: res2 += 1
        else: res3 += 1
    print("\n\n")
    print('Chances of winning if you change'+' : '+str(float(((res0+res3)/len(stats))*100))+' %')
    print('Chances of winning if you stick'+'  : '+str(float(((res1+res2)/len(stats))*100))+' %')
    # print(results[2]+' : '+str(float((res2/len(stats))*100))+' %')
    # print(results[3]+' : '+str(float((res3/len(stats))*100))+' %')
    statistics.close()

def the_game():
    selecting_door()
    money_door()
    door_revealation()
    change()
    result()

while n > 0:
    n -= 1
    doors = [1,2,3]
    the_game()

analysis()

