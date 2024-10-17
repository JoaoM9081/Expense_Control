# Controle de Despesas

Este é um aplicativo simples de controle de despesas criado em Python. Ele permite que você registre suas receitas e gastos, além de visualizar gráficos para análise das suas finanças.

## Funcionalidades

- **Cadastro de Categorias**: Permite criar categorias personalizadas para organizar suas despesas (ex: Alimentação, Transporte, Lazer, etc.).
  
- **Registro de Receitas**: Insira e organize suas receitas financeiras.

- **Registro de Gastos**: Registre todas as despesas financeiras, associando-as às categorias apropriadas e data de retirada.

- **Visualização de Histórico**: Visualize todas as receitas e gastos em uma tabela, facilitando a análise.

- **Gráficos de Análise**:
  - **Gráfico de Barras**: Mostra a comparação entre receitas e gastos por categoria.
  - **Gráfico de Pizza**: Exibe a distribuição percentual das despesas entre diferentes categorias.

- **Interface Gráfica Intuitiva**: Uma interface gráfica amigável construída com `Tkinter`, permitindo fácil navegação e gerenciamento das finanças.

- **Integração com Banco de Dados**: O sistema possui integração com um Banco de Dados, permitindo que os dados fiquem de receitas e gastos fiquem salvos.


## Como usar

1. Clone este repositório para o seu computador local, com o comando: 
```sh
git clone https://github.com/JoaoM9081/Expense_Control.git
```

2. Navegue até o diretório `código`, onde os arquivos `view.py`, `main.py` e `createDB.py` estão localizados.

3. **Execute o arquivo `createDB.py` para criar o banco de dados**.

4. Depois de criar o banco de dados, execute o arquivo `main.py` usando Python 3:

## Dependências

Este projeto depende das seguintes bibliotecas Python:

* pillow
* matplotlib
* tkcalendar
* pandas

Você pode instalar essas dependências usando o pip:

```bash
    pip install pillow matplotlib tkcalendar pandas