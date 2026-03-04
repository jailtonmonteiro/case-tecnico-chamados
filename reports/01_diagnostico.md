# RELATÓRIO PRELIMINAR DE ANÁLISE DE DADOS

**Projeto:** Análise de Base de Chamados de TI  
**Base:** base_chamados.csv  
**Volume:** 50.500 registros  #### 
**Data da análise:** 02/03/2026

## 1. Objetivo

#### Realizar uma análise exploratória inicial da base de chamados de TI, identificando:

* Problemas estruturais
* Inconsistências
* Dados nulos ou faltantes
* Problemas de padronização
* Possíveis impactos analíticos
* Recomendações de tratamento

## 2. Visão Geral da Base

#### A base contém 50.500 registros de chamados técnicos com as seguintes colunas:

| Coluna               | Descrição                  |
| -------------------- |:--------------------------:|
| id_chamado           | Identificador único        |
| data_abertura        | Data de abertura do chamado|
| data_fechamento      | Data de encerramento       |
| setor                | Setor atendido             |
| empresa              | Empresa atendida           |
| categoria            | Categoria do chamado       |
| prioridade           | Nível de prioridade        |
| status               | Status atual               |
| tecnico_responsavel  | Técnico designado          |

## 3. Problemas Encontrados
### 3.1 Dados Nulos / Faltantes

| Coluna                |  Linhas Na | Observação           |
| --------------------- | ----- | ------------------------- |
| data_abertura         | 0     | Coluna em formato string  |
| data_fechamento       | 2545  | Coluna em formato string  |
| tecnico_responsavel   | 8270  | Falta de atribuição       |

### 3.2 Inconsistência de Datas

* Registros possuem `data_fechamento` anterior à `data_abertura`.
* Registros sem datas de fechamento.

### 3.3 Inconsistência em atribuição 

* Registros possuem `tecnico_responsavel` como valor nulo

### 3.4 Padronização de campos

* Registros sem padrão de letras.
* Registros com espaços em brancos.