import pytest
import tempfile

from utils.extrator import Extrator
from pathlib import Path

class TesteExtrator:

#-----------------------------------------------------------------------------------#

    def teste_extracao_dados_sucesso(self):
        """
        Testa extração bem-sucedido de dados.
        
        """
        # Criar arquivo CSV temporário
        arq_csv = """DATA_INICIO;DATA_FIM;CATEGORIA;LOCAL_INICIO;LOCAL_FIM;DISTANCIA;PROPOSITO
                    01-01-2024 09:00;01-01-2024 09:30;Negocio;São Paulo;São Paulo;15;Reunião
                    02-01-2024 10:00;02-01-2024 10:15;Pessoal;Rio de Janeiro;Rio de Janeiro;8;Alimentação
        """

        # Arquivo temporario
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as a:
            a.write(arq_csv)
            arq_temp = a.name

        try:
            ext = Extrator()
            df = ext.extrair_dado(arq_temp)

            # Verifica conteudo do arquivo
            ## Numero de registros
            assert len(df) == 2
            ## Existencia de coluna especificas
            assert 'DATA_INICIO' in df.columns
            assert 'CATEGORIA' in df.columns
            ## Valida o dado da primeira linha de registro do campo 'CATEGORIA'
            assert df.iloc[0]['CATEGORIA'] == 'Negocio'
        
        finally:
            Path(arq_temp).unlink()

#-----------------------------------------------------------------------------------#

    def teste_arquivo_in_nao_existe(self):
        """
        Testa erro quando arquivo não existe.
        
        """
        ext = Extrator()

        # Teste de erro
        with pytest.raises(FileNotFoundError):
            ext.extrair_dado('arquivo_inexistente.csv')

#-----------------------------------------------------------------------------------#

    def teste_coluna_nao_existe(self):
        """
        Testa erro quando colunas obrigatórias estão ausentes.
        
        """
        # CSV sem coluna PROPOSITO
        arq_csv = """DATA_INICIO;DATA_FIM;CATEGORIA;LOCAL_INICIO;LOCAL_FIM;DISTANCIA
                    01-01-2024 09:00;01-01-2024 09:30;Negocio;São Paulo;São Paulo;15
        """
        
        # Arquivo temporario
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, encoding='utf-8') as a:
            a.write(arq_csv)
            arq_temp = a.name

        try:
            ext = Extrator()

            # Teste de erro
            with pytest.raises(ValueError, match="Colunas obrigatórias ausentes"):
                ext.extrair_dado(arq_temp)
        
        finally:
            Path(arq_temp).unlink()

#-----------------------------------------------------------------------------------#