@echo off
title CampusQuant AI Master Launcher
cls

echo =========================================================================
echo               CAMPUSQUANT AI - MASTER LAUNCHER
echo =========================================================================
echo.

cd /d "%~dp0"

echo [1/2] Launching FastAPI Backend Server...
start "CampusQuant Backend Server" cmd /k ".venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload"

echo [2/2] Launching Vite Frontend App...
start "CampusQuant Frontend Server" cmd /k "cd /d frontend && npm run dev"

echo.
echo =========================================================================
echo  [SUCCESS] CampusQuant AI Services Started!
echo  - Backend API:  http://127.0.0.1:8000
echo  - Frontend App: http://localhost:5173
echo.
echo  Opening web app in default browser...
echo =========================================================================
echo.

start http://localhost:5173
