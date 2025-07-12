"""
Módulo para exportar dados processados.
"""

import pandas as pd
from pathlib import Path

class Carga:
    """Exporta dados processados para CSV."""

    def carregar_dado(self, df: pd.DataFrame, caminho_arq: str) -> None:
        """
        Exporta DataFrame para arquivo CSV.

        Args:
            df: DataFrame com dados processados
            file_path: Caminho para salvar o arquivo
        """

        # Criar diretório se não existir
        Path(caminho_arq).parent.mkdir(parents=True, exist_ok=True)

        # Salvar CSV
        df.to_csv(caminho_arq, index=False, encoding='utf-8', sep= ';')
