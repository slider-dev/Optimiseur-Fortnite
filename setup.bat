::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFAhYVQCHAE+1EbsQ5+n//NaOr0waUd1tKN2Pl+XebbFF1RS9IMR+gCoPyYUFDxQ4
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSzk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
SETLOCAL

REM Vérifiez si Python est installé
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installé. Installation de Python...
    REM Téléchargement du programme d'installation de Python
    curl -o python_installer.exe https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Python a été installé avec succès.
) ELSE (
    echo Python est déjà installé.
)

REM Vérifiez si Git est installé
git --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Git n'est pas installé. Installation de Git...
    REM Téléchargement du programme d'installation de Git
    curl -o git_installer.exe https://github.com/git-for-windows/git/releases/latest/download/Git-2.40.0-64-bit.exe
    start /wait git_installer.exe /VERYSILENT /NORESTART
    echo Git a été installé avec succès.
) ELSE (
    echo Git est déjà installé.
)

REM Cloner le dépôt
echo Clonage du dépôt...
git clone https://github.com/slider-dev/Optimiseur-Fortnite.git

echo Installation et clonage terminés.
ENDLOCAL
pause
