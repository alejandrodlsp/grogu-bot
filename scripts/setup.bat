@echo off
cd ..
mkdir log
echo.> log/discord.log
copy .env.example .env
pip install -r requirements.txt
echo Set up complete...
pause
