import random
import time

OPERATORS =["+","-","*"]
MIN_OPERAND = 2
MAX_OPERAND = 15
TOTAL_PROBLEMS=10

def gen_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATORS)
    expr= str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr,answer

input("Press Enter to Start")
print("------------------------")

start_time =time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer=gen_problem()
    while True:
        guess=input("Problem #"+ str(i+1) + ": "+ expr + "= ")
        if guess==str(answer):
            break

end_time=time.time()
total_time= round(end_time-start_time,2)
print("------------------------")
print("Nice Work!",total_time,"Seconds!")
