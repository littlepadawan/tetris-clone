import time

tick_rate = 1
starttime = time.time()
while True:
    print ("tick")
    time.sleep(tick_rate - ((time.time() - starttime) % tick_rate))


# import threading
# 
# def test_function():
#     print('woop')
#     
# timer = threading.Timer(0.6, test_function)
# 
# #def start_time():