
# Ver se um número é primo
# Para ser primo, deve ser divisível apenas por 1 e por ele mesmo

a = int(input("Insira um número para verificar: "))
divisores = [0] * a
termo = 0

for i in range(1, a + 1):
    if a % i == 0:
        divisores[termo] = i
        termo += 1
        

print("Quantidade de divisores:", termo)
print(divisores[:termo])

if termo == 2:
    print("O número é primo")
else:
    print("O número não é primo")
