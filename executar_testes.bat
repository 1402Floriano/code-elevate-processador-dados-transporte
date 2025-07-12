@echo off
echo Executando testes do Processador de Transporte
echo ================================================

echo.
echo Instalando dependencias...
python -m pip install -r requirements.txt

echo.
echo Executando testes com cobertura...
python -m pytest --cov=src --cov-report=term-missing

echo.
echo Testes concluidos!
pause
