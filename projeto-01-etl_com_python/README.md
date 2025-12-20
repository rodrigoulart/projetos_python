# Projeto 01 - Pipeline de ETL com Python

## Descrição
Projeto baseado em dados fictícios de clientes bancários.  
O objetivo foi construir um **pipeline ETL** completo utilizando Python e Pandas, extraindo dados de arquivos CSV e XML, realizando limpeza e validação, e carregando em um arquivo CSV final.

## Principais Implementações
- Leitura de múltiplas fontes de dados (CSV e XML).  
- Identificação e remoção de registros com dados inconsistentes (CPFs inválidos, cartões incompletos, nomes vazios, datas incorretas, saldos negativos).  
- Padronização de tipos de dados (datas, saldos, strings).  
- Consolidação dos dados em um único arquivo CSV pronto para análise.  
- Estrutura de pastas organizada (`dados/brutos` e `dados/processados`).  

## Arquivos
- `dados/brutos/clientes_csv.csv` - Dados de clientes em CSV.  
- `dados/brutos/clientes_xml.xml` - Dados de clientes em XML.  
- `dados/processados/clientes_tratados.csv` - Arquivo final com os clientes válidos após ETL.  
- `codigo/etl_clientes.py` - Script Python implementando o pipeline ETL.  
- `requirements.txt` - Dependências do projeto.

