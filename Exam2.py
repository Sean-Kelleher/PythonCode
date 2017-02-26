import Mods

def getTiming():
    timings = {}
    timingsList = Mods.fileList('timings.txt')
    for i in timingsList:
        line = i.split(",")
        line[1] = float(line[1].strip());
        if line[1] not in timings:
            timings[line[1]] = line[0]
        else:
            timings[line[1]] += line[0]
    return timings

def categorize(dic):
    
    chList = []
    smList = []
    atList = []
    itList = []
    amList = []
    pList = []
  
    for i in dic:
        if i < 10:
            chList.append(dic[i])
        if 20 > i >= 10 :
            smList.append(dic[i])
        if 30 > i >= 20:
            atList.append(dic[i])
        if 40 > i >= 30:
            itList.append(dic[i])
        if 60 > i >= 40:
            amList.append(dic[i])
        if i > 60:
            pList.append(dic[i])
    solvers = {'Cube Head' :  chList, 'Square Master' :  smList, 'Advanced Twister' : atList, 'Intermediate Turner' :  itList, 'Average Mover' :  amList, 'Pathetic' :  pList}
    return solvers
        
    

def main():
    t = getTiming()
    solvers = categorize(t)
    chList = solvers['Cube Head']
    smList = solvers['Square Master']
    atList = solvers['Advanced Twister']
    itList = solvers['Intermediate Turner']
    amList = solvers['Average Mover']
    pList = solvers['Pathetic']
    print "Cube Head (0-9.99):"
    Mods.printList(chList)
    print ' '
    print "Square Master (10-19.99):"
    Mods.printList(smList)
    print ' '
    print "Advanced Twister (20-29.99):"
    Mods.printList(atList)
    print ' '
    print "Intermediate Turner (30-39.99):"
    Mods.printList(itList)
    print ' '
    print "Average Mover (40-59.99):"
    Mods.printList(amList)
    print ' '
    print "Pathetic(60 and above):"
    Mods.printList(pList)
    print ' '
main()