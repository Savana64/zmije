import threading

user_input = input("Zadej numera oddělené mezerou: ")
numbers_str = user_input.split(" ")
print ("numbers_str = ", numbers_str)
numbers_int = [int(x) for x in numbers_str]
print ("numbers_int = ", numbers_str)

def sumo(l):
    print(sum(numbers_int))

def average(l):
    print(sum(numbers_int)/len(numbers_int))

t1 = threading.Thread(target=sumo, args =[numbers_int])
t2 = threading.Thread(target=average, args =[numbers_int])

t1.start()
t2.start()
print("Threads are runninng............")

t1.join()
t2.join()
