# 🧬 Análise de Dados Biomédicos

Projeto desenvolvido para praticar **Python, análise de dados, estatística e visualização aplicada à Biomedicina**.

O sistema utiliza dados fictícios de exames laboratoriais para realizar análises, calcular estatísticas, classificar resultados e gerar gráficos.

> ⚠️ **Aviso:** todos os dados utilizados neste projeto são fictícios e foram criados exclusivamente para fins educacionais. O sistema não deve ser utilizado para diagnóstico médico ou interpretação clínica de pacientes reais.

---

## 🎯 Objetivo

O objetivo deste projeto é unir conhecimentos de **Biomedicina e programação**, utilizando Python para analisar informações semelhantes às encontradas em exames laboratoriais.

O programa permite:

- 📋 Cadastrar dados de um exame;
- 🧪 Analisar glicose, colesterol e hemoglobina;
- 🤖 Classificar o resultado como **Normal** ou **Alterado**;
- 🔎 Identificar quais parâmetros apresentaram alteração;
- 📊 Calcular médias e estatísticas;
- 📈 Calcular correlação entre idade e colesterol;
- 📉 Gerar gráficos para visualização dos dados;
- 💾 Armazenar os dados em um arquivo CSV.

---

## 🧪 Dados analisados

O projeto utiliza as seguintes informações:

| Variável | Descrição |
|---|---|
| `idade` | Idade do indivíduo |
| `sexo` | Sexo informado no cadastro |
| `glicose` | Valor de glicose do exame |
| `colesterol` | Valor de colesterol |
| `hemoglobina` | Valor de hemoglobina |
| `diagnostico` | Classificação do resultado |

Os dados iniciais estão armazenados em:

```text
dados/exames.csv
```

---

## 🤖 Classificação dos resultados

Para fins didáticos, o programa utiliza regras simplificadas para classificar os resultados.

Atualmente:

- **Glicose ≥ 100** → considerada alterada pelo programa;
- **Colesterol > 200** → considerado alterado pelo programa;
- Caso nenhum desses parâmetros esteja alterado → resultado **Normal**;
- Caso pelo menos um esteja alterado → resultado **Alterado**.

Quando uma alteração é encontrada, o programa informa qual parâmetro apresentou alteração.

### Exemplo

```text
Classificação: Alterado

Alterações encontradas:
- Glicose alterada
- Colesterol alterado
```

> Essas regras são simplificadas e servem apenas para demonstrar lógica de programação. Não representam critérios suficientes para diagnóstico clínico.

---

## 📊 Visualizações

O projeto também utiliza gráficos para facilitar a interpretação dos dados.

### Distribuição da glicose

O programa gera um histograma para visualizar como os valores de glicose estão distribuídos entre os exames.

### Idade × Colesterol

Também é gerado um gráfico de dispersão relacionando:

```text
Idade × Colesterol
```

Cada ponto representa um exame.

O programa também calcula a correlação entre essas duas variáveis.

---

## 📈 Estatísticas

O projeto utiliza a biblioteca `pandas` para calcular informações estatísticas, como:

- Média;
- Desvio padrão;
- Mínimo;
- Máximo;
- Quartis;
- Correlação.

Exemplo:

```text
Média de glicose: 114.40
Média de colesterol: 217.60
Média de hemoglobina: 13.76
```

Os valores acima são referentes aos dados fictícios utilizados no projeto.

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python**
- 🐼 **Pandas**
- 📊 **Matplotlib**
- 📄 **CSV**
- 💻 **Visual Studio Code**

---

## 📁 Estrutura do projeto

```text
analise-dados-biomedicos/
│
├── dados/
│   └── exames.csv
│
├── src/
│   └── analise.py
│
└── README.md
```

---

## 🚀 Como executar

### 1. Instale o Python

Certifique-se de que o Python está instalado no computador.

Verifique pelo terminal:

```bash
python --version
```

---

### 2. Instale as bibliotecas

No terminal:

```bash
pip install pandas matplotlib
```

---

### 3. Clone ou baixe o projeto

Depois, abra a pasta do projeto no Visual Studio Code.

---

### 4. Execute o programa

No terminal:

```bash
python src/analise.py
```

---

## 🧪 Exemplo de utilização

Ao executar o programa, o usuário pode cadastrar um novo exame:

```text
===================================
       NOVO EXAME BIOMÉDICO
===================================

Idade: 25
Sexo (F/M): F
Glicose: 90
Colesterol: 180
Hemoglobina: 13.5
```

O programa realiza a análise e apresenta:

```text
===================================
          RESULTADO DO EXAME
===================================

Idade: 25
Sexo: F
Glicose: 90.0
Colesterol: 180.0
Hemoglobina: 13.5

Classificação: Normal

Nenhuma alteração encontrada pelos critérios do programa.
```

Os dados também são armazenados no arquivo:

```text
dados/exames.csv
```

---

## 🎓 Objetivo acadêmico

Este projeto foi desenvolvido como uma forma de explorar a aplicação da programação na área da **Biomedicina**, especialmente em atividades relacionadas a:

- Análise de dados laboratoriais;
- Estatística;
- Visualização de informações;
- Automação de tarefas;
- Ciência de dados;
- Introdução ao Machine Learning.

A proposta é desenvolver conhecimentos que possam futuramente ser aplicados em áreas como **análises clínicas, pesquisa científica, bioinformática e ciência de dados aplicada à saúde**.

---

## 🔬 Possíveis melhorias futuras

Algumas funcionalidades que podem ser adicionadas futuramente:

- [ ] Adicionar valores de referência para hemoglobina;
- [ ] Melhorar a classificação dos exames;
- [ ] Criar gráficos separados para resultados normais e alterados;
- [ ] Criar uma interface gráfica;
- [ ] Adicionar filtros por idade e sexo;
- [ ] Criar um painel (*dashboard*) com os resultados;
- [ ] Adicionar mais exames laboratoriais;
- [ ] Implementar análise estatística mais avançada;
- [ ] Criar um modelo de Machine Learning utilizando um conjunto de dados adequado;
- [ ] Criar relatórios automáticos.

---

## ⚠️ Limitações

Este projeto é **educacional**.

Os dados são fictícios e as regras de classificação utilizadas são simplificadas. Portanto, os resultados apresentados pelo programa **não possuem finalidade diagnóstica** e não devem ser utilizados para avaliar a saúde de pessoas reais.

Em uma aplicação real seriam necessários dados adequados, valores de referência validados, controle de qualidade, tratamento de dados, análise estatística rigorosa, validação e supervisão de profissionais qualificados.

---

## 👩‍🔬 Sobre o projeto

Projeto desenvolvido por uma estudante de **Biomedicina**, com o objetivo de explorar a integração entre conhecimentos biomédicos e tecnologia.

**Biomedicina + Python + Dados 🧬💻📊**
