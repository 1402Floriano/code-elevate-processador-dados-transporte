import pytest
import pandas as pd

from utils.tratamento import Tratamento
from datetime import date

class TestDataProcessor:

#-----------------------------------------------------------------------------------#

    def teste_processamento_dados_sucesso(self):
        """
        Testa tratamento bem-sucedido de dados.
        
        """
        # Dados de teste
        data = {
            'DATA_INICIO':  ['01-01-2024 09:00', '01-01-2024 14:00', '02-01-2024 10:00'],
            'DATA_FIM':     ['01-01-2024 09:30', '01-01-2024 14:30', '02-01-2024 10:30'],
            'CATEGORIA':    ['Negocio', 'Pessoal', 'Negocio'],
            'LOCAL_INICIO': ['SP', 'SP', 'RJ'],
            'LOCAL_FIM':    ['SP', 'SP', 'RJ'],
            'DISTANCIA':    [15, 25, 30],
            'PROPOSITO':    ['Reunião', 'Alimentação', 'Entregas']
        }
        df = pd.DataFrame(data)

        trm = Tratamento()
        df = trm.tratar_dado(df)

        # Estrutura esperada de colunas
        estrutura_esperada = [
            'DT_REFE', 'QT_CORR','QT_CORR_NEG',      
            'QT_CORR_PESS', 'VL_MAX_DIST', 'VL_MIN_DIST',     
            'VL_AVG_DIST', 'QT_CORR_REUNI', 'QT_CORR_NAO_REUNI'
        ]

        # Base com o resultado refrente ao dia 01-01-2024
        df_dia_01 = df[df['DT_REFE'] == date(2024, 1, 1)].iloc[0]

        # Verifica conteudo do arquivo
        ## Colunas esperadas
        assert list(df.columns) == estrutura_esperada
        ## Numero de registros
        assert len(df) == 2
        ## Valida os resultados do dia 01-01-2024
        assert df_dia_01['QT_CORR'] == 2
        assert df_dia_01['QT_CORR_NEG'] == 1
        assert df_dia_01['QT_CORR_PESS'] == 1
        assert df_dia_01['VL_MAX_DIST'] == 25
        assert df_dia_01['VL_MIN_DIST'] == 15
        assert df_dia_01['VL_AVG_DIST'] == 20.0
        assert df_dia_01['QT_CORR_REUNI'] == 1
        assert df_dia_01['QT_CORR_NAO_REUNI'] == 1

#-----------------------------------------------------------------------------------#

    def teste_converter_string_para_data(self):
        """
        Testa conversão bem-sucedida de datas.
        
        """
        trm = Tratamento()

        datas = pd.Series(['01-01-2024 09:00', '02-01-2024 10:00'])
        sr = trm.converter_string_para_data(datas)

        # Verifica o formato da coluna
        assert pd.api.types.is_datetime64_any_dtype(sr)
        # Verifica os valores de dia, mes e ano
        assert sr.iloc[0].day == 1
        assert sr.iloc[0].month == 1
        assert sr.iloc[0].year == 2024

#-----------------------------------------------------------------------------------#

    def teste_falha_converter_string_para_data(self):
        """
        Testa erro na conversão de datas inválidas.
        
        """
        trm = Tratamento()

        datas = pd.Series(['data_invalida', 'outra_data_invalida'])

        # Teste erro
        with pytest.raises(ValueError, match="Não foi possível converter as datas"):
            trm.converter_string_para_data(datas)

#-----------------------------------------------------------------------------------#

    def teste_agregar_base_por_data(self):
        """
        Testa agregação por data.
        
        """
        data = {
            'DATA_INICIO': pd.to_datetime(['2024-01-01 09:00', '2024-01-01 14:00', '2024-01-02 10:00']),
            'DT_REFE': [date(2024, 1, 1), date(2024, 1, 1), date(2024, 1, 2)],
            'CATEGORIA': ['Negocio', 'Pessoal', 'Negocio'],
            'DISTANCIA': [10, 20, 30],
            'PROPOSITO': ['Reunião', 'Alimentação', 'Entregas']
        }
        df = pd.DataFrame(data)

        trm = Tratamento()
        df = trm.agregar_base_por_data(df)

        # Verifica numero de registros
        assert len(df) == 2
        # Valida o dado da primeira linha de registro do campo 'QT_CORR' (Dia 1)
        assert df.iloc[0]['QT_CORR'] == 2
        # Valida o dado da segunda linha de registro do campo 'QT_CORR' (Dia 2)
        assert df.iloc[1]['QT_CORR'] == 1

#-----------------------------------------------------------------------------------#