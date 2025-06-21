# Simulador de Projeção Financeira Interativo

Uma aplicação web interativa construída com o framework [Streamlit](https://streamlit.io/) para simular projeções financeiras. Permite aos usuários visualizar o crescimento de seus investimentos ao longo do tempo, considerando diferentes cenários de rentabilidade (pessimista, base e otimista) e acompanhar o progresso em direção a uma meta financeira.

## Funcionalidades Principais

*   **Entrada de Dados Personalizada:** Defina o valor inicial, aportes mensais, taxa de rentabilidade base anual, prazo em anos e sua meta financeira.
*   **Análise de Cenários:** Simulações automáticas para cenários pessimista (taxa base - 3%), base e otimista (taxa base + 3%).
*   **Visualização Gráfica:** Gráfico interativo (Plotly) mostrando a evolução do patrimônio acumulado para cada cenário ao longo dos meses, com a meta financeira destacada.
*   **Resumo por Cenário:** Tabela concisa exibindo o valor final acumulado e o percentual da meta atingida para cada um dos três cenários.
*   **Evolução Mensal Detalhada:** Tabela com a progressão do investimento mês a mês para um cenário selecionado pelo usuário.
*   **Acompanhamento da Meta (Cenário Base):** Barra de progresso visualizando o quão perto você está de atingir sua meta no cenário base, com uma mensagem indicativa.
*   **Exportação de Dados:** Faça o download dos resultados da simulação (dados de cada cenário e o resumo) em formato Excel (.xlsx) para análise offline ou compartilhamento.

## Como Usar

### Pré-requisitos

*   Python 3.6 ou superior
*   As seguintes bibliotecas Python:
    *   `streamlit`
    *   `pandas`
    *   `plotly`
    *   `xlsxwriter`

### Instalação das Dependências

Você pode instalar as bibliotecas necessárias usando pip:

```bash
pip install streamlit pandas plotly xlsxwriter
```

### Executando a Aplicação

1.  Navegue até o diretório onde o arquivo `app.py` está localizado.
2.  Execute o seguinte comando no seu terminal:

    ```bash
    streamlit run app.py
    ```
3.  Abra o navegador no endereço fornecido pelo Streamlit (geralmente `http://localhost:8501`).
4.  Interaja com a Aplicação:
    *   Insira os valores desejados nos campos de entrada no painel lateral.
    *   Observe os gráficos e tabelas serem atualizados dinamicamente.
    *   Selecione diferentes cenários para visualização detalhada.
    *   Utilize o botão de download para obter a planilha Excel com os dados da simulação.

## Tecnologias Utilizadas

*   **Streamlit:** Para a criação da interface web interativa.
*   **Plotly Express:** Para a geração dos gráficos interativos.

---