def descrizione():
  pass
  # Gestione dei file e del sistema operativo
  # os: interagisce con il sistema operativo (file, directory, variabili d'ambiente).
  # sys: accesso a variabili e funzioni del sistema Python (come sys.argv per argomenti da riga di comando).
  # shutil: operazioni avanzate sui file (copia, spostamento, compressione).
  # pathlib: manipolazione di percorsi in stile object-oriented.
  # glob: trova file e directory in base a pattern (es. *.txt).

  # 🧮 Matematica e numeri
  # math: funzioni matematiche di base (coseno, logaritmo, radici, ecc.).
  # random: generazione di numeri casuali.
  # statistics: calcolo di media, mediana, varianza, ecc.
  # decimal: aritmetica decimale ad alta precisione.
  # fractions: numeri razionali (es. 1/3).

  # ⏱️ Tempo e date
  # time: misurazione del tempo, pause (sleep), timestamp.
  # datetime: manipolazione e formattazione di date e orari.
  # calendar: gestione dei calendari.

  # 🔍 Test e debug
  # unittest: framework per test automatici.
  # doctest: verifica del comportamento direttamente da docstring.
  # logging: gestione dei log a vari livelli (info, warning, error, ecc.).
  # traceback: stampa stack trace per debug avanzato.

  # 📡 Internet e Web
  # urllib: libreria per URL, richiesta e risposta HTTP.
  # http: moduli per client/server HTTP.
  # json: lettura e scrittura di file JSON.
  # html, xml: parsing e manipolazione di markup.

  # 🧵 Concurrency / Multithreading
  # threading: thread a livello di sistema.
  # multiprocessing: esecuzione parallela su più processi.
  # asyncio: programmazione asincrona.

  # 🧰 Varie utilità
  # re: espressioni regolari.
  # collections: tipi di dati avanzati come deque, Counter, namedtuple.
  # itertools: strumenti per la manipolazione di iteratori.
  # functools: funzioni e decoratori utili.
  # enum: definizione di enumerazioni.
  # dataclasses: creazione di classi dati con sintassi semplificata.

#questo fa si che invece che importare tuttal la libria 
#fai si che dalla libreria importi le funzioni che ti servono
from random import randint,choice #choice prende un valore random dalla lista
print(randint(1,1999))#stampa un numero random
#cosi posso fare un import generale o dedicatgo di dati da un altro file
#se fosse stato ad esempio in una cartella sarebbe stato import nomeCartella.nomefile
#import fileDiEsempioPerImport 
#from fileDiEsempioPerImport import somma

import datetime
print(datetime.date(2025,4,8))
print(datetime.datetime.now())