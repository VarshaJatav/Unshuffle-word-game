import random
def fun1(word):
    random.shuffle(word)
    return word

def fun2():
    l_word=[]
    l1=['Rainbow','Check','Huge','Chair','Bookmark','Class','Cloud','Water','Blanket','Pencil','Book','Smile','Copy','Entertainment','Pillow','Phone','Serious','Rain','Snowfall','Mountain','House']
    word=random.choice(l1)
    l_word=list(word)
    (random.shuffle(l_word))
    print("".join(l_word))
    return list(word)



count_1,count_2=0,0
print("Welcome to Game...")
player_1=input("Enter first player name: ")
player_2=input("Enter second player name: ")
choice=1
while choice==1:
    print("Welcome ",player_1," your ques is : ")
    c_ans=(fun2())
    ans=input("Your answer is : ")
    if list(ans)==(c_ans):
        count_1 = count_1 + 1
    else:
        print("Correct answer  is : ","".join((c_ans)))
    

    print("Welcome ",player_2," your ques is : ")
    c_ans=fun2()
    ans=input("Your answer is : ")
    
    if list(ans)==(c_ans):
        count_2 = count_2 + 1
    else:
        print("Correct answer is : ","".join(c_ans))

    choice=int(input("Do you want to continue:  Enter 1 for yes, 0 for no :  "))



print(player_1," score is : ",count_1)
print(player_2," score is : ",count_2)

if count_1>count_2:
    print(player_1," won....")
elif count_1<count_2:
    print(player_2," won...")
else:
    print("Draw...")
