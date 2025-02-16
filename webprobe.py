from sys import argv
import threading
import requests

no_threads = 5
arguments = ["--thread", "-t", "-o", "--output"]

# Usage:
# python3 webprobe.py <SampleFile> 
# python3 webprobe.py --thread <NoOfThreads> <SampleFile>

length_of_arguments = len(argv)
file_name = argv[length_of_arguments -  1]

if length_of_arguments > 1:
    if argv[1] in arguments:
        if argv[1] == "--thread" or argv[1] == "-t":
            if int(argv[2]) <= 120 :
                no_threads = int(argv[2])
            else:
                print("Enter threads below 120.\n")
                exit(120)
        else:
            print("Enter the arguments with file.\n")
            exit(1)
elif length_of_arguments == 1:
    print("Pass arguments.\n")
    exit(2)
        
"""
Reading the file containing domain names.
"""
with open(file_name) as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    
def do_request():
    for line in lines:
        req = requests.get(line, verify=False)
        if req.ok:
            print(line, end = ' ')
            print(200)
        else:
            print("Oops unable to connect.\n")


# Connecting the domains from file using threads.

threads = []
for i in range(no_threads):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(no_threads):
    threads[i].start()

for i in range(no_threads):
    threads[i].join()


exit(0)

