from datetime import date
 

def days_between(d1, d2):
    return abs(d2 - d1).days
def Fecha():
    print("Fecha de inicio")
    mi = 13
    di = 32
    mf = 13
    df = 32
    ai=int(input("Digite el año de inicio: "))

    while(mi>=13):
        mi=int(input("Digite el mes de inicio: "))
    while(di>=32):
        di=int(input("Digite el dia de inicio: "))
    print("Fecha final")

    af=int(input("Digite el año final: "))
    while(mf>=13):
        mf=int(input("Digite el mes final: "))
    while(df>=32):
        df=int(input("Digite el dia final: "))

    d1 = date(ai,mi,di)
    d2 = date(af,mf,df)

    print ("%s dias de diferencia entre %s y el %s" % (days_between(d2, d1), d1, d2))
    print ("%s años de diferencia entre %s y el %s" % (int(days_between(d2, d1)/365), d1, d2))