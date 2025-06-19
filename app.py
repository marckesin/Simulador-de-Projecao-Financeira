import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import streamlit as st  # type: ignore
from io import BytesIO


# Função de simulação
def simular_projecao(valor_inicial, aporte_mensal, taxa_anual, anos, meta):
    """
    Simula em quanto tempo um determinado patrimônio será alcançado, com base
        nos parâmetros fornecidos.

    Args:
        valor_inicial (float): Valor inicial investido.
        aporte_mensal (float): Aporte mensal.
        taxa_anual (float): Taxa de rentabilidade anual.
        anos (int): Prazo em anos.
    """
    # Cálculos
    taxa_mensal = (1 + taxa_anual) ** (1 / 12) - 1
    meses = anos * 12
    dados = []
    valor = valor_inicial
    for mes in range(1, meses + 1):
        valor = valor * (1 + taxa_mensal) + aporte_mensal
        dados.append(
            {
                "Mês": mes,
                "Ano": mes // 12 + (1 if mes % 12 != 0 else 0),
                "Valor acumulado (R$)": round(valor, 2),
                "Meta atingida (%)": round(valor / meta * 100, 2),
            }
        )
    return pd.DataFrame(dados)


# Interface Streamlit
st.title("Simulador de Projeção Financeira com Cenários")

# Entradas do usuário
valor_inicial = st.number_input("Valor inicial investido (R$)", value=0.0, step=1000.0)
aporte_mensal = st.number_input("Aporte mensal (R$)", value=0.0, step=100.0)
taxa_base = (
    st.slider("Rentabilidade base anual (%)", min_value=0.1, max_value=30.0, value=10.0)
    / 100
)
anos = st.slider("Prazo (anos)", min_value=1, max_value=50, value=1)
meta = st.number_input(
    "Meta financeira (R$)", min_value=1.0, value=10000.0, step=5000.0
)

# Taxas para cenários
cenarios = {
    "Pessimista": taxa_base - 0.03,
    "Base": taxa_base,
    "Otimista": taxa_base + 0.03,
}

# Simulações
resultados = {}
for nome, taxa in cenarios.items():
    resultados[nome] = simular_projecao(valor_inicial, aporte_mensal, taxa, anos, meta)
    resultados[nome]["Cenário"] = nome

# Consolida dados para plotagem
df_total = pd.concat(resultados.values(), ignore_index=True)

# Gráfico interativo com Plotly
st.subheader("Gráfico Interativo por Cenário")
fig = px.line(
    df_total,
    x="Mês",
    y="Valor acumulado (R$)",
    color="Cenário",
    title="Projeção Financeira por Cenário",
)
fig.add_hline(
    y=meta,
    line_dash="dash",
    line_color="red",
    annotation_text="Meta",
    annotation_position="top left",
)
st.plotly_chart(fig, use_container_width=True)

# Tabela resumo
st.subheader("Resumo por Cenário")
df_resumo = pd.DataFrame(
    {"Cenário": [], "Valor Final (R$)": [], "Meta Atingida (%)": []}
)
for nome, df in resultados.items():
    final = df.iloc[-1]
    df_resumo.loc[len(df_resumo)] = [
        nome,
        final["Valor acumulado (R$)"],
        final["Meta atingida (%)"],
    ]

st.dataframe(df_resumo.set_index("Cenário"))

# Filtro de cenário para tabela detalhada
st.subheader("Evolução Mês a Mês por Cenário")
cenario_selecionado = st.selectbox(
    "Escolha o cenário para exibir a evolução:", list(resultados.keys())
)
st.dataframe(resultados[cenario_selecionado])

# Baixar em formato Excel
output = BytesIO()
with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
    for nome, df in resultados.items():
        df.to_excel(writer, sheet_name=nome, index=False)
        df_resumo.to_excel(writer, sheet_name="Resumo", index=False)
        output.seek(0)

st.download_button(
    label="📄 Baixar planilha Excel (.xlsx)",
    data=output,
    file_name="simulacao_financeira_cenarios.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)

# Exibe progresso apenas para cenário base
progresso = resultados["Base"].iloc[-1]["Meta atingida (%)"]
barra = min(progresso / 100, 1.0)
if progresso < 100:
    texto = f"{progresso:.2f}% da meta atingida"
else:
    texto = f"Meta ultrapassada em {progresso - 100:.2f}%!"

st.subheader("Progresso da Meta (Cenário Base)")
st.progress(barra, text=texto)
