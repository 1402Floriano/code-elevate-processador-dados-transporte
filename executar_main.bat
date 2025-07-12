@echo off

echo.
echo Instalando dependencias...
python -m pip install -r requirements.txt

echo.
echo.
echo.
echo Executando processamento...
python main.py

echo.
echo Processamento concluido!
pause