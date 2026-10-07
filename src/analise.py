import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# CARREGAR OS DADOS
# ==========================================

df = pd.read_csv("dados/exames.csv")


# ==========================================
# CADASTRAR NOVO EXAME
# ==========================================

print("===================================")
print("       NOVO EXAME BIOMÉDICO")
print("===================================")

idade = int(input("Idade: "))
sexo = input("Sexo (F/M): ").upper()
glicose = float(input("Glicose: "))
colesterol = float(input("Colesterol: "))
hemoglobina = float(input("Hemoglobina: "))


# ==========================================
# CLASSIFICAÇÃO
# ==========================================

alteracoes = []

if glicose >= 100:
    alteracoes.append("Glicose alterada")

if colesterol > 200:
    alteracoes.append("Colesterol alterado")


if len(alteracoes) == 0:
    diagnostico = "Normal"
else:
    diagnostico = "Alterado"


# ==========================================
# MOSTRAR RESULTADO
# ==========================================

print("\n===================================")
print("          RESULTADO DO EXAME")
print("===================================")

print(f"Idade: {idade}")
print(f"Sexo: {sexo}")
print(f"Glicose: {glicose}")
print(f"Colesterol: {colesterol}")
print(f"Hemoglobina: {hemoglobina}")

print("\nClassificação:", diagnostico)

if diagnostico == "Alterado":
    print("\nAlterações encontradas:")

    for alteracao in alteracoes:
        print("-", alteracao)

else:
    print("\nNenhuma alteração encontrada pelos critérios do programa.")


# ==========================================
# SALVAR NOVO EXAME
# ==========================================

novo_exame = pd.DataFrame({
    "idade": [idade],
    "sexo": [sexo],
    "glicose": [glicose],
    "colesterol": [colesterol],
    "hemoglobina": [hemoglobina],
    "diagnostico": [diagnostico]
})

df = pd.concat([df, novo_exame], ignore_index=True)

df.to_csv("dados/exames.csv", index=False)


# ==========================================
# ESTATÍSTICAS
# ==========================================

print("\n===================================")
print("          ESTATÍSTICAS")
print("===================================")

media_glicose = df["glicose"].mean()
media_colesterol = df["colesterol"].mean()
media_hemoglobina = df["hemoglobina"].mean()

print(f"Média de glicose: {media_glicose:.2f}")
print(f"Média de colesterol: {media_colesterol:.2f}")
print(f"Média de hemoglobina: {media_hemoglobina:.2f}")

alterados = (df["diagnostico"] == "Alterado").sum()
normais = (df["diagnostico"] == "Normal").sum()

print(f"\nExames normais: {normais}")
print(f"Exames alterados: {alterados}")


# ==========================================
# CORRELAÇÃO
# ==========================================

correlacao = df["idade"].corr(df["colesterol"])

print(f"\nCorrelação entre idade e colesterol: {correlacao:.2f}")


# ==========================================
# GRÁFICO - IDADE X COLESTEROL
# ==========================================

plt.figure(figsize=(8, 5))

for diagnostico, grupo in df.groupby("diagnostico"):

    plt.scatter(
        grupo["idade"],
        grupo["colesterol"],
        label=diagnostico
    )

plt.title("Relação entre idade e colesterol")
plt.xlabel("Idade")
plt.ylabel("Colesterol")

plt.legend()
plt.grid(True)

plt.show()