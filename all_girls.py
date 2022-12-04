import random
'''
50% having girls

girls are preferred: if girl, then stop giving birth.

ratio of girls and boys in this world?


'''

def generate_0_1(p=0.5):
    total = 1000 * p
    val = random.randint(0, 1000)
    if val < p * 1000:
        return 1
    return 0

def generate_bg(p=0.5):
    temp = generate_0_1(p)
    bg = [0,0]
    while temp != 1:
        bg[temp] += 1
        temp = generate_0_1(p)
    bg[temp] += 1
    return bg



def sample_world(n=1000, p=0.5):
    i = 2
    bg = [1, 1]
    #boys_created = 1
    while i < n:
        temp = generate_bg(p)
        bg = [bg[0] + temp[0], bg[1] + temp[1]]
        #boys_created += temp[0]
        i += (temp[0] + temp[1])
        #boys_created -= 1

    return bg[1]/(bg[0]+bg[1])



def main():

    print(sample_world(10000,0.7))


main()
