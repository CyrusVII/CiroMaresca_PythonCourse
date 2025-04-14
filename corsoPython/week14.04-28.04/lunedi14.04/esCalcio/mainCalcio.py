# creare una classe base MembroSquadra e diverse classi figlie che rappresentano ruoli specifici all'interno della squadra di calcio, 
# come Giocatore, Allenatore, e Assistente.
# L'esercizio consente di esplorare come differenti membri della squadra possono ereditare attributi comuni dalla classe base, 
# ma anche come possono differire nei loro comportamenti e responsabilità.
# Classe MembroSquadra:
# Attributi: nome (stringa)
# età (intero)
# Metodi:
# descrivi() (stampa una descrizione generale del membro della squadra)
# Classi Derivate:
# Giocatore:
# Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
# Metodi come gioca_partita() che possono includere azioni specifiche del giocatore Allenatore:
# Attributi aggiuntivi come anni_di_esperienza
# Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti Assistente:
# Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
# ■ Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team
import DbConnetion as db
import giocatore as g
import allenatore as a
import assistente as ass
import random
import time

nomeDb = "calcio"

def getData(nomeSquadra):
    myDb = db.db_connection(nomeDb)
    cursor = myDb.cursor()
    
    lista_squadra = {}

    # Giocatori
    query = """
            SELECT ms.id, ms.nome, ms.eta, ms.nome_squadra, g.ruolo, g.numero_maglia
            FROM MembroSquadra ms
            JOIN Giocatore g ON ms.id = g.id
            WHERE ms.nome_squadra = %s;"""
    cursor.execute(query, (nomeSquadra,))
    risultati = cursor.fetchall()
    for r in risultati:
        player = g.Giocatore(r[0], r[1], r[2], r[3], r[4], r[5])
        lista_squadra[r[0]] = player  # chiave = id giocatore

    # Allenatore
    query1 = """SELECT ms.id, ms.nome, ms.eta, ms.nome_squadra, a.anni_di_esperienza
                FROM MembroSquadra ms
                JOIN Allenatore a ON ms.id = a.id
                WHERE ms.nome_squadra = %s;"""
    cursor.execute(query1, (nomeSquadra,))
    risultati = cursor.fetchall()
    for r in risultati:
        coach = a.Allenatore(r[0], r[1], r[2], r[3], r[4])
        lista_squadra["Allenatore"] = coach

    # Assistente
    query2 = """SELECT ms.id, ms.nome, ms.eta, ms.nome_squadra, ass.specializzazione, ass.anni_di_esperienza
                FROM MembroSquadra ms
                JOIN Assistente ass ON ms.id = ass.id
                WHERE ms.nome_squadra = %s;"""
    cursor.execute(query2, (nomeSquadra,))
    risultati = cursor.fetchall()
    for r in risultati:
        assistente = ass.Assistente(r[0], r[1], r[2], r[3], r[4], r[5])
        lista_squadra["Assistente"] = assistente

    cursor.close()
    myDb.close()
    return lista_squadra

def simula_partita(squadra1, squadra2):
    nome1 = squadra1['Allenatore'].nome_squadra
    nome2 = squadra2['Allenatore'].nome_squadra
    
    print(f"\n🔥 Inizia la partita!\n")

    gol_squadra1 = 0
    gol_squadra2 = 0

    marcatori1 = []
    marcatori2 = []
    
    coachB1 = squadra1["Allenatore"].percAnni()
    coachB2 = squadra2["Allenatore"].percAnni()
    
    bonus_ass1 = sum([a.calcola_bonus() for a in squadra1.get("Assistenti", [])])
    bonus_ass2 = sum([a.calcola_bonus() for a in squadra2.get("Assistenti", [])])
    
    for i in range(5):  # 5 azioni per squadra
    
      if random.random() < 0.5 + coachB1 + bonus_ass1:
        time.sleep(0.6)
        marcatore = random.choice([p for k, p in squadra1.items() if isinstance(k, int)])
        gol_squadra1 += 1
        marcatori1.append(marcatore.nome)
        print(f"⚽ Gol di {marcatore.nome} per {nome1}!")
      if random.random() < 0.5 + coachB2 + bonus_ass2:
        time.sleep(0.6)
        marcatore = random.choice([p for k, p in squadra2.items() if isinstance(k, int)])
        gol_squadra2 += 1
        marcatori2.append(marcatore.nome)
        print(f"⚽ Gol di {marcatore.nome} per {nome2}!")

    print("\n📋 Risultato finale:")
    print(f"{nome1} {gol_squadra1} - {gol_squadra2} {nome2}")

    print("\n🎯 Marcatori:")
    print(f"{nome1}: {', '.join(marcatori1) if marcatori1 else 'Nessuno'}")
    print(f"{nome2}: {', '.join(marcatori2) if marcatori2 else 'Nessuno'}")

    print("\n👨‍🏫 Allenatori:")
    print(f"{nome1}: {squadra1['Allenatore'].nome}")
    print(f"{nome2}: {squadra2['Allenatore'].nome}")

cyrusFc = getData("CyrusFc")
mirkoFc = getData("MirkoFc")
simula_partita(cyrusFc,mirkoFc)