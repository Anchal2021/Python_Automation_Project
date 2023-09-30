#This script is used to Monitor process
#Ref : https://pypi.org/project/psutil/ for more info on psutil lib

import psutil

def print_processes():
    processes = psutil.process_iter()
    for proc in processes:
        info = proc.as_dict(attrs=["ppid","pid","name","username","threads"])
        info["vms"] = proc.memory_info().vms/(1024*1024)
        if info["threads"] is not None:
            info["threads"] = len(info["threads"])
        if info["threads"] is not None and info["threads"]>10:
            print(info)

def main():
    print_processes()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
