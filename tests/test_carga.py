import pandas as pd
import tempfile

from utils.carga import Carga
from pathlib import Path


class TesteCarga:

#-----------------------------------------------------------------------------------#

    def teste_carga_dados_sucesso(self):
        """
        Testa exportação bem-sucedida de dados.
        
        """
        # Dados de teste
        data = {
            'DT_REFE':           ['2024-01-01', '2024-01-02'],
            'QT_CORR':           [2, 1],
            'QT_CORR_NEG':       [1, 1],
            'QT_CORR_PESS':      [1, 0],
            'VL_MAX_DIST':       [25, 30],
            'VL_MIN_DIST':       [15, 30],
            'VL_AVG_DIST':       [20.0, 30.0],
            'QT_CORR_REUNI':     [1, 0],
            'QT_CORR_NAO_REUNI': [0, 1]
        }
        df = pd.DataFrame(data)

        # Criar arquivo temporário
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as a:
            arq_temp = a.name

        try:
            crg = Carga()
            crg.carregar_dado(df, arq_temp)

            # Leitura do arquivo caregado
            df_out = pd.read_csv(arq_temp, sep=';')

            # Verificar se arquivo foi criado
            assert Path(arq_temp).exists()
            # Verifica conteudo do arquivo
            ## Numero de registros
            assert len(df_out) == 2
            ## Compara colunas do antes e depois da carga do arquivo
            assert list(df_out.columns) == list(df.columns)
            ## Valida o dado da primeira linha de registro do campo 'QT_CORR'
            assert df_out.iloc[0]['QT_CORR'] == 2

        finally:
            if Path(arq_temp).exists():
                Path(arq_temp).unlink()

#-----------------------------------------------------------------------------------#

    def teste_criar_diretorio(self):
        """
        Testa se o carregamento cria diretórios necessários.
        
        """
        # Dados de teste
        data = {'coluna': [1, 2, 3]}
        df = pd.DataFrame(data)

        # Caminho com diretório que não existe
        with tempfile.TemporaryDirectory() as temp_dir:
            caminho_arq = Path(temp_dir) / 'novo_diretorio' / 'arquivo.csv'

        crg = Carga()
        crg.carregar_dado(df, caminho_arq)

        # Verificar se o arquivo foi criado
        assert caminho_arq.exists()
        # Verificar se o diretório foi criado
        assert caminho_arq.parent.exists()

#-----------------------------------------------------------------------------------#

    def teste_carga_arquivo_vazio(self):
        """
        Testa carregamento de DataFrame vazio.
        
        """
        df = pd.DataFrame()

        # Criar arquivo temporário
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as a:
            arq_temp = a.name

        try:
            crg = Carga()
            crg.carregar_dado(df, arq_temp)

            # Verificar se arquivo foi criado (mesmo vazio)
            assert Path(arq_temp).exists()

        finally:
            if Path(arq_temp).exists():
                Path(arq_temp).unlink()

#-----------------------------------------------------------------------------------#