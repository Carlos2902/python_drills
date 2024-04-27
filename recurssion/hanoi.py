
def hanoi(n,start, end):
    if n == 1:
        pm(start, end)
    else:
        auxiliary_pilar = 6-(start + end)
        #the reside beside the base disk are gonna be transport to the auxiliary pilar
        hanoi(n-1, start, auxiliary_pilar)
        pm(start, end)
        #the last step, at the end, the disks from the auiliary pilar are gonna be placed in the last one
        hanoi(n-1, auxiliary_pilar, end)

    

#funtction for printing just the move
def pm(start,end):
     print('from pilar',start, 'to ->', 'pilar:',end)


hanoi(3, 1, 3)