@echo off
title Home Credit Dashboard - Project Creator

echo ========================================
echo     HOME CREDIT DASHBOARD
echo       NEW PROJECT CREATOR
echo ========================================
echo.

set /p PROJECT_NAME=Enter your project folder name: 

if "%PROJECT_NAME%"=="" (
    echo.
    echo ERROR: Project name cannot be empty.
    pause
    exit /b
)

cd /d "%USERPROFILE%\Documents"

if exist "%PROJECT_NAME%" (
    echo.
    echo ERROR: A folder named "%PROJECT_NAME%" already exists.
    echo.
    echo Your existing project was NOT changed.
    echo.
    pause
    exit /b
)

mkdir "%PROJECT_NAME%"
cd "%PROJECT_NAME%"

echo.
echo Creating project folders...
echo.

mkdir data
mkdir pages
mkdir utils
mkdir Screenshots

type nul > app.py

type nul > utils\data_loader.py
type nul > utils\preprocessing.py
type nul > utils\filters.py
type nul > utils\features.py
type nul > utils\kpis.py
type nul > utils\charts.py

type nul > pages\01_Executive_Overview.py
type nul > pages\02_Default_Analysis.py
type nul > pages\03_Demographic_Analysis.py
type nul > pages\04_Age_Analysis.py
type nul > pages\05_Gender_Analysis.py
type nul > pages\06_Income_Analysis.py
type nul > pages\07_Credit_Analysis.py
type nul > pages\08_Annuity_Analysis.py
type nul > pages\09_Income_vs_Credit.py
type nul > pages\10_Annuity_Burden.py
type nul > pages\11_Education_Analysis.py
type nul > pages\12_Employment_Analysis.py
type nul > pages\13_Family_Analysis.py
type nul > pages\14_Housing_Assets.py
type nul > pages\15_Contract_Analysis.py
type nul > pages\16_External_Score_Analysis.py
type nul > pages\17_Regional_Risk.py
type nul > pages\18_Missing_Value_Analysis.py
type nul > pages\19_Correlation_Risk_Factors.py
type nul > pages\20_Customer_Risk_Explorer.py

echo.
echo ========================================
echo   PROJECT CREATED SUCCESSFULLY!
echo ========================================
echo.
echo Location:
echo %CD%
echo.
echo Created:
echo - app.py
echo - data folder
echo - pages folder
echo - utils folder
echo - Screenshots folder
echo - 20 dashboard pages
echo - 6 utility files
echo.
echo Your existing projects were NOT changed.
echo.
pause