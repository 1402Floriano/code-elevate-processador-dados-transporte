"""
Módulo para carregar dados CSV.
"""

import pandas as pd
from pathlib import Path

class Extrator:
    """Carrega dados do arquivo CSV."""

    def extrair_dado(self, file_path: str) -> pd.DataFrame:
        """
        Carrega dados do arquivo CSV.

        Args:
            file_path: Caminho para o arquivo CSV

        Returns:
            DataFrame com os dados carregados
        """
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        df = pd.read_csv(file_path, delimiter=';', encoding='utf-8')

        # Validar colunas obrigatórias
        required_columns = [
            'DATA_INICIO', 'DATA_FIM', 'CATEGORIA', 
            'LOCAL_INICIO', 'LOCAL_FIM', 'DISTANCIA', 'PROPOSITO'
        ]

        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Colunas obrigatórias ausentes: {missing_columns}")

        return df
