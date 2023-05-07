import time
import datetime
today_date = datetime.datetime.now()
birth_date = today_date + datetime.timedelta(days=45, hours=10, minutes= 29, seconds=46)
temps_restant = birth_date - today_date

temps_en_secondes = temps_restant.total_seconds() 
def compte_a_rebours(temps_en_secondes):
    while temps_en_secondes > 0:
        jours, reste = divmod(temps_en_secondes, 86400)
        heures, reste = divmod(reste, 3600)
        min, sec = (divmod(reste, 60))
        chrono='{:02d}:{:02d}:{:02d}:{:02d}'.format(int(jours), int(heures), int(min), int(sec))
        print(chrono, end="\r")
        time.sleep(1)
        temps_en_secondes -= 1
    else:
        print("HAPPY BIRTHDAY")
compte_a_rebours(temps_en_secondes)