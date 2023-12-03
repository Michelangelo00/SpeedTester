import speedtest
import time
from datetime import datetime

def test_internet_speed():
    try:
        print("Inizio rilevamento velocità della rete...")
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        ping = st.results.ping
        download = st.results.download / 1e6 
        upload = st.results.upload / 1e6      
        print(f"Rilevamento completato. Download: {download:.2f} Mbit/s, Upload: {upload:.2f} Mbit/s, Ping: {ping} ms")
        return download, upload, ping
    except Exception as e:
        print(f"Errore durante il rilevamento: {e}")
        return None, None, None

def main(intervallo_minuti, durata_minuti):
    print(f"Inizio scansione della rete. Durata: {durata_minuti} minuti, Intervallo: {intervallo_minuti} minuti.")
    fine_tempo = time.time() + durata_minuti * 60
    while time.time() < fine_tempo:
        download, upload, ping = test_internet_speed()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp_file_name = datetime.now().strftime("%Y-%m-%d")
        if download is not None and upload is not None and ping is not None:
            risultato = f"{timestamp} - Download: {download:.2f} Mbit/s, Upload: {upload:.2f} Mbit/s, Ping: {ping} ms\n"
            print(f"Salvataggio dei risultati: {risultato}")
            with open(f"risultati_rete_{timestamp_file_name}.txt", "a") as file:
                file.write(risultato)
        else:
            print("Impossibile rilevare la velocità della rete, tentativo successivo in corso...")
            risultato = f"{timestamp} - Impossibile rilevare la velocità della rete\n"
            with open(f"risultati_rete_{timestamp_file_name}.txt", "a") as file:
                file.write(risultato)
        time.sleep(intervallo_minuti * 60)
    print("Scansione della rete completata.")

intervallo_minuti = 2  
durata_minuti = 60     

if __name__ == "__main__":
    main(intervallo_minuti, durata_minuti)
