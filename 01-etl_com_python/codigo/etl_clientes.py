import pandas as pd

# =========================
# EXTRAÇÃO
# =========================

clientes_csv = pd.read_csv(
    "dados/brutos/clientes_csv.csv",
    dtype={
        "cpf": str,
        "cartao": str
    }
)

clientes_xml = pd.read_xml(
    "dados/brutos/clientes_xml.xml",
    dtype={
        "cpf": str,
        "cartao": str
    },
    parser="etree"
)

clientes_csv["origem_dados"] = "CSV"
clientes_xml["origem_dados"] = "XML"

clientes = pd.concat([clientes_csv, clientes_xml], ignore_index=True)

# =========================
# TRANSFORMAÇÃO
# =========================

# Remover registros com campos obrigatórios nulos
clientes = clientes.dropna(subset=["nome", "cpf", "cartao"])

# Remover nomes vazios
clientes = clientes[clientes["nome"].str.strip() != ""]

# Limpar CPF e cartão (remover espaços)
clientes["cpf"] = clientes["cpf"].str.strip()
clientes["cartao"] = clientes["cartao"].str.strip()

# Validar CPF (11 dígitos)
clientes = clientes[clientes["cpf"].str.len() == 11]

# Validar cartão (16 dígitos)
clientes = clientes[clientes["cartao"].str.len() == 16]

# Converter datas
clientes["data_nascimento"] = pd.to_datetime(
    clientes["data_nascimento"], errors="coerce"
)

clientes["data_abertura"] = pd.to_datetime(
    clientes["data_abertura"], errors="coerce"
)

clientes = clientes.dropna(
    subset=["data_nascimento", "data_abertura"]
)

# Converter saldo
clientes["saldo"] = pd.to_numeric(
    clientes["saldo"], errors="coerce"
)

clientes = clientes[clientes["saldo"] >= 0]

# =========================
# CARREGAMENTO
# =========================

clientes.to_csv(
    "dados/processados/clientes_tratados.csv",
    index=False
)

print("ETL finalizado com sucesso.")
print(f"Total de clientes válidos: {len(clientes)}")
