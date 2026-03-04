# RELATÓRIO PÓS-TRATAMENTO DE DADOS

Projeto: Análise de Base de Chamados de TI  
Base Original: base_chamados.csv  
Base Tratada Disponibilizada: nova_base.csv  
Data: 03/03/2026

## 1. Objetivo

Documentar a disponibilização de uma nova base estruturada para análise, após tratamento prévio de qualidade de dados.

#### Importante:
Não foram realizadas projeções, modelagens preditivas ou imputações estatísticas.
O trabalho consistiu exclusivamente na disponibilização de um novo CSV com dados já estruturados.

## 2. Estrutura da Nova Base

Formato: CSV
Separador: ;
Encoding esperado: UTF-8

### Colunas disponíveis

|Coluna	|Tipo esperado | Descrição
|--------|--------|:-----------------:|
|id_chamado|	int|	Identificador único
|data_abertura|	datetime|	Data de abertura
|data_fechamento|	datetime|	Data de encerramento
|setor|	string|	Área solicitante
|empresa|	string|	Empresa associada
|categoria|	string|	Tipo do chamado
|prioridade	|string|	Nível de prioridade
|status|	string|	Status do chamado
|tecnico_responsavel|	string|	Técnico designado
|tempo_atendimento_dias|	int|	Tempo total em dias
|sla_cumprido|	boolean|	Indicador de SLA

#### Exemplo de registro:

    0;2023-10-17 03:01:00;2023-10-20 10:01:00;operações;empresa_a;hardware;media;fechado;pedro;3;True

## 3. Alterações Observadas em Relação à Base Original
### 3.1 Nova Variável Derivada

`tempo_atendimento_dias`

* Representa o tempo total entre abertura e fechamento
* Já calculado previamente
* Elimina necessidade de recomputar tempo via diferença de datas

### 3.2 Inclusão de Variável de SLA

`sla_cumprido`

* Tipo booleano
* Permite análise direta de conformidade
* Facilita métricas de performance

### 3.3 Normalização Estrutural

#### Observa-se que:

* Colunas estão padronizadas em snake_case
* Categorias parecem previamente tratadas (ex: sistema_erp)
* Empresas seguem padrão empresa_x
* Setores estão consolidados

### 4. O que NÃO foi realizado

#### Para evitar interpretações equivocadas:

* Não houve modelagem estatística
* Não houve imputação de valores faltantes
* Não houve projeção de métricas
* Não houve remoção adicional de registros nesta etapa
* Não houve ajuste de outliers via técnicas estatísticas

#### A base apenas foi disponibilizada já tratada estruturalmente.

### 5. Conclusão Técnica

#### A nova base:

* Está estruturada para análise imediata
* Contém variável derivada de tempo
* Inclui indicador objetivo de SLA
* Apresenta padronização semântica

#### O dataset encontra-se apto para:

* Análises descritivas
* Construção de dashboards
* Cálculo de métricas operacionais
* Avaliação de performance por setor, empresa e técnico