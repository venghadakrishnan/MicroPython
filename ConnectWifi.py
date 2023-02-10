def connect():
    import network
    ssid = "Arun_5g"
    password = "Arun@123"
    #8939646436
    
    station = network.WLAN(network.STA_IF)
    
    if station.isconnected() == True:
        print("Already exists")
        return
    station.active(True)
    station.ifconfig()
    
    station.connect(ssid,password)
    while station.isconnected() == False:
        pass
    print("Connection successfully")
    print(station.ifconfig())