#Task 1

questions =["What is the largest country?", "What country has the most islands?", "What country has the largest population?", "What is the oldest country in the world?"]
answers = ["Russia", "Norway", "India", "Egypt"]


#Task 2
'''
def quiz(qquestion, qanswer):
    for q in qquestion:
        ans = input(f"{q} ")

quiz(questions, answers)
'''


#Task 3

def quiz(quest, answ):
    an_list = []
    for a in answ:
        an_list.append(a)
    result = 0
    c = 0
    for q in quest:
        ans = input(f"{q} ")
        if ans == an_list[c]:
            print("That is correct!")
            result += 1
        else:
            print(f"That is incorrect, the answer is {an_list[c]}")
        c += 1
    print(f"You got {result} correct.")
        
quiz(questions, answers)