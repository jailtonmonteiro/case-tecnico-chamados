# Case Técnico de Estudos
Estudo realizado com base suja gerada por IA para complemento de estudos do curso de Pandas.

## Objetivo

#### Aplicar conceitos de:
* Manipulação de dados com Pandas
* Limpeza e padronização de dados
* Validação estrutural e lógica
* Criação de dataset tratado
* Documentação técnica de projeto

O projeto simula um cenário real de análise de chamados de TI, partindo de uma base com inconsistências até a disponibilização de um dataset estruturado para análise.

## Estrutura do Projeto

case-tecnico-estudos/  
│  
├── data/  
│ ├── raw/ # Dados originais (imutáveis)  
│ │ ├── base_chamados.csv  
│ │ └── exemplo.csv  
│ │  
│ └── processed/ # Dados tratados e prontos para análise  
│ ├── base_tratada.csv  
│ └── nova_base.csv  
│  
├── notebooks/ # Scripts de análise e processamento  
│ ├── 01_exploracao.py  
│ ├── 02_limpeza_tratamento.py  
│ └── 03_processamento.py  
│  
├── reports/ # Documentação analítica  
│ └── 01_diagnostico.md  
│  
├── README.md  
├── requirements.txt  
└── .gitignore  

## Contexto do Case

#### A base original foi propositalmente gerada com problemas como:

* Dados nulos
* Datas inconsistentes
* Falta de padronização
* Possíveis duplicidades
* Valores incoerentes

O objetivo foi identificar esses problemas, documentá-los e disponibilizar uma nova base tratada, pronta para consumo analítico.

## Etapas Realizadas
### 1. Análise Exploratória Inicial

* Verificação de estrutura
* Tipagem de dados
* Percentual de valores nulos
* Duplicidades

### 2. Validação de Regras de Negócio

* `data_fechamento >= data_abertura`
* `tempo_atendimento_dias >= 0`
* SLA consistente com tempo de atendimento
* Domínio válido para categorias, prioridades e status

### 3. Disponibilização de Nova Base

*data/processed/nova_base.csv*

#### Com:

* Estrutura padronizada
* Variável derivada tempo_atendimento_dias
* Indicador booleano sla_cumprido
* Colunas normalizadas (snake_case)

## Estrutura da Base Tratada

| Coluna                 | Descrição            |
| ---------------------- | -------------------- |
| id_chamado             | Identificador único  |
| data_abertura          | Data de abertura     |
| data_fechamento        | Data de encerramento |
| setor                  | Área solicitante     |
| empresa                | Empresa associada    |
| categoria              | Tipo do chamado      |
| prioridade             | Nível de prioridade  |
| status                 | Status atual         |
| tecnico_responsavel    | Técnico designado    |
| tempo_atendimento_dias | Tempo total em dias  |
| sla_cumprido           | Indicador de SLA     |

## Tecnologias Utilizadas

* Python 3.14.3
* Pandas 2.3.3
* Jupyter Notebook 1.1.1
* conda 26.1.0

#### Instalação:
* `pip install -r requirements.txt`

## Validações Implementadas

#### Exemplos de verificações realizadas:

* Unicidade de id_chamado
* Consistência entre datas
* Coerência entre tempo calculado e informado
* Domínio controlado de variáveis categóricas
* Verificação de valores nulos críticos

## Aprendizados Aplicados

* Data Cleaning em ambiente realista
* Estruturação de projeto de dados
* Documentação técnica
* Pensamento analítico orientado a regra de negócio
* Organização de repositório para portfólio

## Observação

Este projeto tem finalidade educacional e simula um cenário real de análise de dados para consolidação prática dos conteúdos estudados.