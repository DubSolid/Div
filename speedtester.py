import speedtest as st

st = st.Speedtest()

def test_speed():
    B = 1 # B = 1 byte
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)
    GB = float(KB ** 3)

    option = int(input('''What do you want to test? 

    1) Download Speed
    2) Upload Speed
    3) Ping

    '''))

    if option == 1:
        down_speed = (st.download())
        if down_speed > GB:
            print('Your download speed is',round(float(down_speed)/GB, 2), "Gbps")
        elif down_speed > MB:
            print('Your download speed is',round(float(down_speed)/MB, 2), "Mbps")
        elif down_speed > KB:
            print('Your download speed is',round(float(down_speed)/KB, 2), "Kbps")

    elif option == 2:
        up_speed = (st.upload())
        if up_speed > GB:
            print('Your upload speed is',round(float(up_speed)/GB, 2), "Gbps")
        elif up_speed > MB:
            print('Your upload speed is',round(float(up_speed)/MB, 2), "Mbps")
        elif up_speed > KB:
            print('Your upload speed is',round(float(up_speed)/KB, 2), "Kbps")

    elif option == 3:
        servernames = []
        st.get_servers(servernames)
        print(st.results.ping)

    else:
        print('Input correct option!')

test_speed()
