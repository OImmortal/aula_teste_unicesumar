# Algoritmo para verificar situação do aluno

# Lendo as 4 notas
notas = []
for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

# Calculando a média
media = sum(notas) / 4

# Verificando a situação
if media >= 7.0:
    print(f"Média = {media:.2f} → Aluno APROVADO!")
elif media >= 4.0:
    print(f"Média = {media:.2f} → Aluno em FINAL!")
else:
    print(f"Média = {media:.2f} → Aluno REPROVADO!")
