import time

def focus_timer(minutes):
    focus_time = minutes * 60 # 转换为秒钟

    while focus_time:
        mins, secs = divmod(focus_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        focus_time -= 1
    
    print("时间到！")

focus_timer(25) # 专注时间为25分钟
