import threading
import time

# Thread işlevi
def thread_func():
    print("Thread başlatıldı.")
    time.sleep(5)  # 5 saniye boyunca uyutalım
    print("Thread tamamlandı.")

# Ana program
print("Program başladı.")

# Thread'i oluştur ve başlat
thread = threading.Thread(target=thread_func)
thread.start()

# Ana programın geri kalanı
print("Ana program devam ediyor.")
print("Ana program tamamlandı.")