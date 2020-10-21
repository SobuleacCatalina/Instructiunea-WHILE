"""
Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură.
"""
suma=0
produs=1
nr=1
n=eval(input("n= "))
while nr<=n:
    suma+=nr
    produs*=nr
    nr+=1
print("Suma= ",suma)
print("Produs= ",produs)
print("Media aritmetica= ",suma/n)