import bluetooth

search_time = 10
addr = None

print ("Welcome to the bluetoth detection demo! \n Make sure your desired bluetooth device is turned on and discoverable")

if addr==None:
    try:
        input("When yhou are ready, press the enter to continue...")
    except SyntaxError:
        pass
    
    print("Searching for devices...")

    nearby_devices = bluetooth.discover_devices(duration=search_time, flush_cache=True, lookup_names=True)

    if len(nearby_devices) > 0:
        print("Found % devices!" % len(nearby_devices))
    else:
        print("No devices found!")
        exit(0)

    i = 0 

    for addr, name in nearby_devices:
        print("%s. %s - %s" %(i, addr, name))
        i=+1

    

