# Valor3D

**Sistema Web para Gestão de Custos e Formação de Preços para Impressões 3D**

Sistema web desenvolvido como projeto de estágio obrigatório do curso de Engenharia de Computação da Universidade Virtual do Estado de São Paulo (UNIVESP), com o objetivo de auxiliar profissionais e empreendedores da área de impressão 3D no gerenciamento de custos e na formação de preços de peças produzidas.

---

## Sobre o Projeto

O Valor3D foi desenvolvido para automatizar o processo de cálculo de custos e formação de preços de peças produzidas por impressão 3D.

O sistema permite cadastrar materiais, impressoras e parâmetros de custos, além de criar orçamentos e calcular automaticamente os principais componentes envolvidos na formação do preço de venda.

A aplicação foi desenvolvida buscando proporcionar maior organização, padronização e praticidade no processo de elaboração de orçamentos.

---

## Objetivo

Auxiliar profissionais e empreendedores da área de impressão 3D na definição de preços, considerando os principais custos envolvidos no processo produtivo:

- Custo do material;
- Consumo de energia elétrica;
- Custo da máquina;
- Mão de obra de preparação;
- Acabamento;
- Margem de lucro;
- Quantidade de peças.

---

## Funcionalidades

### Gestão de Materiais

- Cadastro de materiais;
- Edição de materiais;
- Exclusão de materiais;
- Registro de marca, tipo, peso do rolo e valor.

### Gestão de Impressoras

- Cadastro de impressoras;
- Edição e exclusão;
- Registro de marca e modelo;
- Potência do equipamento;
- Valor do equipamento;
- Vida útil estimada;
- Upload de imagem;
- Controle de status da impressora.

### Configuração de Custos

- Valor do kWh;
- Custo de mão de obra por hora;
- Parâmetros relacionados à preparação e acabamento;
- Margem de lucro.

### Gestão de Orçamentos

- Cadastro de orçamentos;
- Edição de orçamentos;
- Exclusão de orçamentos;
- Seleção de material;
- Seleção de impressora;
- Peso da peça;
- Tempo de impressão;
- Tempo de preparação;
- Tempo de acabamento;
- Quantidade de peças;
- Status do orçamento.

### Cálculos

O sistema realiza automaticamente os cálculos relacionados a:

- Custo do material;
- Custo da máquina;
- Custo de energia elétrica;
- Custo de mão de obra;
- Custo de acabamento;
- Custo total;
- Margem de lucro;
- Preço de venda;
- Lucro previsto.

### Dashboard

O sistema possui um dashboard para apresentação dos principais indicadores e informações relacionadas aos cadastros e orçamentos.

### Autenticação

- Login de usuários;
- Logout;
- Proteção das páginas com autenticação;
- Usuário administrador;
- Recuperação de senha;
- Backend de e-mail para recuperação de senha.

---

## Tecnologias Utilizadas

- **Python 3**
- **Django**
- **MySQL**
- **HTML5**
- **CSS3**
- **Bootstrap 5**
- **Bootstrap Icons**
- **Git**
- **GitHub**
- **Visual Studio Code**

---

## Arquitetura

O projeto utiliza o padrão arquitetural **MVT (Model-View-Template)** adotado pelo framework Django.

A aplicação foi organizada de forma a separar:

- **Models:** representação e persistência dos dados;
- **Views:** regras de negócio e processamento das requisições;
- **Templates:** apresentação e interface do sistema;
- **Forms:** tratamento e validação dos dados dos formulários;
- **URLs:** definição das rotas da aplicação.

O banco de dados utilizado é o **MySQL**.

---

## Estrutura do Projeto

A estrutura principal da aplicação está organizada da seguinte forma:

```text
Valor3D/
│
├── sistema/
│   ├── core/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── manage.py
│   └── ...
│
├── media/
├── .gitignore
└── README.md
Cálculo de Custos

O processo de formação do preço segue, de forma geral, o seguinte fluxo:

Dados do Orçamento
        │
        ▼
Custo do Material
        │
        ▼
Custo da Máquina
        │
        ▼
Custo de Energia
        │
        ▼
Custo de Preparação
        │
        ▼
Custo de Acabamento
        │
        ▼
Custo Total
        │
        ▼
Aplicação da Margem de Lucro
        │
        ▼
Preço de Venda

O resultado é apresentado ao usuário na tela de resumo do orçamento, permitindo visualizar o custo total, o preço de venda e o lucro previsto.

Desenvolvimento

O desenvolvimento do Valor3D foi organizado utilizando uma abordagem baseada em sprints, combinando princípios de Scrum e Kanban para planejamento e acompanhamento das atividades.

Sprint 1 — Estrutura Inicial
Definição do projeto;
Configuração do ambiente;
Criação da aplicação Django;
Configuração inicial do banco de dados.
Sprint 2 — Materiais
Modelagem de materiais;
CRUD de materiais;
Integração com o banco de dados.
Sprint 3 — Impressoras
Modelagem de impressoras;
CRUD de impressoras;
Upload de imagens;
Informações técnicas dos equipamentos.
Sprint 4 — Orçamentos
Modelagem de orçamentos;
CRUD de orçamentos;
Relacionamento entre materiais, impressoras e orçamentos.
Sprint 5 — Cálculos
Cálculo do custo do material;
Cálculo da máquina;
Cálculo de energia;
Cálculo de mão de obra;
Cálculo de acabamento;
Custo total;
Margem de lucro;
Preço de venda.
Sprint 6 — Dashboard e Integração
Dashboard;
Integração das funcionalidades;
Organização das regras de negócio;
Melhorias na apresentação das informações.
Sprint 7 — Autenticação e Qualidade
Sistema de login;
Logout;
Proteção das páginas;
Recuperação de senha;
Mensagens do sistema;
Revisão geral;
Atualização do GitHub.
Sprint 8 — UX/UI e Identidade Visual
Nova identidade visual;
Logotipo oficial;
Menu lateral;
Dashboard;
Bootstrap Icons;
Padronização dos componentes;
Refinamento dos cards;
Ajustes de espaçamento e alinhamento;
Tela de resumo do orçamento;
Melhorias de experiência do usuário;
Acabamento visual do sistema.
Controle de Versão

O desenvolvimento do projeto foi acompanhado utilizando Git para controle de versões e GitHub para armazenamento e acompanhamento do código-fonte.

O repositório permite registrar a evolução do projeto durante as etapas de desenvolvimento e manter o histórico das alterações realizadas.


**Status do Projeto**

**Concluído — versão 1.0**

**Data de conclusão:** 05/08/2026

O projeto foi desenvolvido como parte das atividades do Estágio Supervisionado Obrigatório do curso de Engenharia de Computação da UNIVESP.

---

## Autora

**Adriane Cristina de Souza**

Estudante de Engenharia de Computação
Universidade Virtual do Estado de São Paulo — UNIVESP

2026

---

## Licença

Este projeto foi desenvolvido para fins acadêmicos como parte das atividades do Estágio Supervisionado Obrigatório da UNIVESP.