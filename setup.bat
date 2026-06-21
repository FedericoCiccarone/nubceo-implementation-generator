@echo off

echo Instalando dependencias Nubceo Assistant...

python -m venv venv

call venv\Scripts\activate

pip install -r requirements.txt

playwright install

echo.
echo Instalacion completa
pause