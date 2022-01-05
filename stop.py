
cuenta=50000

riesgo=cuenta*0.006



while 1:

    pips=float(input("pips: "))

    lote=0.01

    while lote*pips<=riesgo:
        lote+=0.001

    print(lote)



