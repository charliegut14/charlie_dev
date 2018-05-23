import os

network = input("Input first 3 octets for sweep: [ex 192.168.1.]")
while len(network) < 10:
    network = input("Input first 3 octets for sweep: [ex 192.168.1.]")


for x in range(1,255):
    response = os.system("ping -c 1 " + str(network) + str(x) + "> /dev/null 2>&1")
    if response == 0:
        print(str(network) + str(), 'is up!')
    else:
        print(str(network) + str(x), 'is down!')


