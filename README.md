# Processador de Dados de Transporte

Sistema simples para processar dados de aplicativos de transporte e gerar relatórios agregados por data.

## 📋 Funcionalidades

- Processa arquivo CSV `info_transportes.csv`
- Gera tabela `info_corridas_do_dia` com dados agregados por data
- Calcula métricas: quantidade de corridas, média de distâncias percorrida, etc...

## 🚀 Como usar

### 🪟 **Windows (Mais Fácil)**

#### 1. Executar processamento
```cmd
executar_main.bat
```

#### 2. Executar testes
```cmd
executar_testes.bat
```

### 💻 **Linha de Comando (Qualquer SO)**

#### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

#### 2. Executar o processamento
```bash
python main.py
```

#### 3. Executar testes
```bash
python -m pytest --cov=src --cov-report=term-missing
```

## 📁 Estrutura do projeto

```
code-elevate-processador-dados-transporte/
├── main.py                    # Script principal
├── executar_main.bat          # Script Windows para main
├── executar_testes.bat        # Script Windows para testes
├── requirements.txt           # Dependências
├── utils/
│   ├── __init__.py
│   ├── carga.py               # Extração dos dados
│   ├── extrator.py            # Tratamento dos dados
│   └── tratamento.py          # Carregamento daos resultados
├── tests/
│   ├── __init__.py
│   ├── test_carga.py
│   ├── test_extrator.py
│   └── test_tratamento.py
├── data/
│   ├── in/                    # Coloque aqui o info_transportes.csv
│   └── out/                   # Arquivo de saída será gerado aqui
└── README.md
```

## 📊 Arquivo de entrada esperado

O arquivo `info_transportes.csv` deve estar em `data/in/` com as colunas:
- DATA_INICIO
- DATA_FIM  
- CATEGORIA
- LOCAL_INICIO
- LOCAL_FIM
- DISTANCIA
- PROPOSITO

## 📈 Arquivo de saída

Será gerado `data/out/info_corridas_do_dia.csv` com:
- DT_REFE
- QT_CORR
- QT_CORR_NEG
- QT_CORR_PESS
- VL_MAX_DIST
- VL_MIN_DIST
- VL_AVG_DIST
- QT_CORR_REUNI
- QT_CORR_NAO_REUNI

## 🔧 Solução de Problemas

### Erro "pytest não é reconhecido"
Use: `python -m pytest` ao invés de apenas `pytest`

### Erro de módulo não encontrado
Certifique-se de estar no diretório raiz do projeto e execute:
```bash
pip install -r requirements.txt
```
