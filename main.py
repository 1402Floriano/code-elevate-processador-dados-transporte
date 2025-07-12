#!/usr/bin/env python3
"""
Script principal para processar dados de transporte.
"""

import sys
import os
from pathlib import Path

from utils.extrator import Extrator
from utils.tratamento import Tratamento
from utils.carga import Carga

def main():
    """Função principal."""

    print("🚀 Processador de Dados de Transporte")
    print("=" * 40)

    try:
        
        str_arq_entrada = "data/in/info_transportes.csv"
        str_arq_saida = "data/out/info_corridas_do_dia.csv"

        # Verificar se arquivo de entrada existe
        str_arq_entrada = "data/in/info_transportes.csv"
        if not os.path.exists(str_arq_entrada):
            print(f"❌ Arquivo não encontrado: {str_arq_entrada}")
            print("💡 Coloque o arquivo info_transportes.csv em data/in/")
            return

        # Extrair dados
        print(f"\n 📂 Extraindo dados: {str_arq_entrada}")
        ext = Extrator()
        df = ext.extrair_dado(str_arq_entrada)
        print(f" ✅ {len(df)} registros carregados")

        # Tratar dados
        print("\n ⚙️ Tratando dados...")
        trm = Tratamento()
        df = trm.tratar_dado(df)
        print(f" ✅ {len(df)} registros processados")

        # Carregar dados
        print("\n 💾 Carregando Dados...")
        crg = Carga()
        crg.carregar_dado(df, str_arq_saida)
        print(f" ✅ Arquivo salvo: {str_arq_saida}")


        print("\n 🎉 Processamento concluído com sucesso!")
        print("=" * 40)

    except Exception as e:
        print(f"❌ Erro: {e}")
        return 1

if __name__ == "__main__":
    main()