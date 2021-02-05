import psutil, time

while True:
    proc_iter = psutil.process_iter(attrs=["pid", "name", "cmdline"])
    for proc in proc_iter:
        if proc.name() == 'python.exe':
            # test_running = any("test.py" in proc.info["cmdline"])
            print(proc.cmdline())
            print(proc.memory_percent())
    print("*"*80)
    time.sleep(1)
           # print(test_running)