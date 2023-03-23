import time
import threading
import random

number = 0
wrong = 0
_time = 0
stop_thread = False
stop_main = False

def leave():
    global number
    global wrong
    global _time
    global stop_main

    stop_main = True

    right = number - wrong
    print("正确题目："+str(right)+"道\n错误题目："+str(wrong)+"道\n总题目："+str(number)+"道\n用时："+str(_time)+"秒。")
    exit()
    
def work():

    global number
    global wrong
    global _time
    global stop_thread
    
    while (not stop_thread):
        
        if(number == 10):
            print("已进行10道题目")
            leave()

        if(wrong == 5):
            print("已经错误5道题目")
            leave()
        
        b=random.randint(10,99)
        a=random.randint(b+1,100)

        result = a - b

        last_time = 120 - _time

        print("被减数等于"+str(a)+"，减数等于"+str(b)+"，剩余时间："+str(last_time)+"秒。请告诉我答案，或输入q退出")
        guess = input()
        
        if(guess == 'q'):
            leave()
        
        if(str(result) == guess):
            print("回答正确")
            number = number + 1
        else:
            print("回答错误")
            number = number + 1
            wrong = wrong + 1


t = threading.Thread(target=work)
t.start()

while (not stop_main):
    time.sleep(1)
    
    _time = _time + 1
    
    if(_time == 120):
        print("时间到！程序将在完成这道题后结束！")
        stop_thread = True
        t.join()
        leave()
