import time

while True:
    for i in range(1, 20):
        print((20-i)*' ' + (2*i-1)*'*')
        time.sleep(0.02)
