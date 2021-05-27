import psutil
import time 
import os

class network_stats:
    def __init__(self):
        self.last_recv_time= time.time()
        self.last_sent_time= time.time()
        try:
            self.wifi_net = psutil.net_io_counters(pernic=True)['Wi-Fi']
        except:
            self.wifi_net = None
    def get_wifi_net(self, num=5): #attempt to recheck for Wi-Fi in case of failure 
         try:
            self.wifi_net = psutil.net_io_counters(pernic=True)['Wi-Fi']
            self.last_recv_time= time.time()
            self.last_sent_time= time.time()
         except:
            self.wifi_net = None
            if(num==0):
                return 
            else:
                self.get_wifi_net(num-1)
    def check_conntected(self): # check if it can read any network stats
        if(self.wifi_net == None):
            self.get_wifi_net()
            if(self.wifi_net == None):
                return False
        return True
    def ping_speed(self): #ms #basic ping to google server 
        hostname = '8.8.8.8'
        time_1 = time.time()
        response = os.system('ping -c 1 '+hostname)
        time_2 = time.time()
        print(response)
        return (time_2 - time_1)*1000
    
    def download_upload_speed(self): #kBps #from the new updated readings, get current up/downlaod speed
        if(not self.check_conntected()):
                return -1,-1
        i = 0
        while i in range(10): # retries 10 times in case no changes are reported
            time.sleep(0.75) # tries to avoid instantaneous reading of the network
            wifi_net_2 = psutil.net_io_counters(pernic=True)['Wi-Fi']
            time_a = time.time()
            time_diff = time.time() - self.last_recv_time
            bytes_diff_d = wifi_net_2.bytes_recv - self.wifi_net.bytes_recv
            bytes_diff_u = wifi_net_2.bytes_sent - self.wifi_net.bytes_sent
            self.wifi_net = wifi_net_2
            self.last_recv_time = time_a
            download = bytes_diff_d/time_diff/1024 if time_diff!=0 else 0 #calc in kBps
            upload = bytes_diff_u/time_diff/1024 if time_diff!=0 else 0
            if(upload >=1 and download >=1):
                break
            i+= 1
        return [download, upload]