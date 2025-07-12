"""
Módulo para processar e agregar dados.
"""

import pandas as pd
from datetime import datetime

class Tratamento:
    """Trata e agrega dados por data."""

    def tratar_dado(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Trata dados e agrega por data de referência.

        Args:
            df: DataFrame com dados brutos

        Returns:
            DataFrame com dados agregados por data

        """

        # Converter data de início
        df['DATA_INICIO'] = self.converter_string_para_data(df['DATA_INICIO'])

        # Criar DT_REFE (apenas a data, sem hora)
        df['DT_REFE'] = df['DATA_INICIO'].dt.date

        # Agregar dados por DT_REFE
        df = self.agregar_base_por_data(df)

        return df


    def converter_string_para_data(self, col: pd.Series) -> pd.Series:
        """
        Converte série de datas para datetime.
        
        """
        # Tentar diferentes formatos de data
        formatos_datas = [
            '%d-%m-%Y %H:%M',
            '%Y-%m-%d %H:%M:%S',
            '%d/%m/%Y %H:%M',
            '%Y-%m-%d %H:%M',
            '%m-%d-%Y %H:%M'
        ]

        for data_formato in formatos_datas:
            try:
                return pd.to_datetime(col, format=data_formato)
            except:
                continue

        # Se nenhum formato funcionou, tentar conversão automática
        try:
            return pd.to_datetime(col)
        except:
            raise ValueError("Não foi possível converter as datas")

    
    def agregar_base_por_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Agrega dados por data de referência.

        """
        # Agrupar por DT_REFE
        df = df.groupby('DT_REFE')

        # Calcular agregações
        df = pd.DataFrame({
            'DT_REFE':              list(df.groups.keys()),
            'QT_CORR':              df.size().values,
            'QT_CORR_NEG':          df.apply(lambda x: (x['CATEGORIA'] == 'Negocio').sum()).values,
            'QT_CORR_PESS':         df.apply(lambda x: (x['CATEGORIA'] == 'Pessoal').sum()).values,
            'VL_MAX_DIST':          df['DISTANCIA'].max().values,
            'VL_MIN_DIST':          df['DISTANCIA'].min().values,
            'VL_AVG_DIST':          df['DISTANCIA'].mean().values,
            'QT_CORR_REUNI':        df.apply(lambda x: (x['PROPOSITO'] == 'Reunião').sum()).values,
            'QT_CORR_NAO_REUNI':    df.apply(lambda x: ((x['PROPOSITO'] != 'Reunião') & (x['PROPOSITO'].notna()) & (x['PROPOSITO'] != '')).sum()).values,
        })

        # Ordenar por data
        df = df.sort_values('DT_REFE').reset_index(drop=True)

        # Arredondar valores decimais
        df['VL_AVG_DIST'] = df['VL_AVG_DIST'].round(2)

        return df