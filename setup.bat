set OSGEO4W_ROOT=C:\OSGeo4W
set GDAL_DATA=%OSGEO4W_ROOT%\apps\gdal\share\gdal
set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
set PATH=%PATH%;%OSGEO4W_ROOT%\bin
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%"


eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEyNDI5ODE0LCJpYXQiOjE3MTExMzM4MTQsImp0aSI6IjEwNWIxNmNjNGIwOTRjNzU5YjY2ZjM4Y2U1ZDJhNzQzIiwidXNlcl9pZCI6Mn0.KuADVw0RwnHTEsAARcfWGg2wpdNR31xt53yS-7cDbWA


RJwdCVAoYEeg1Mcvzb2pS/pjYn7EzIEzLljN1ICT key to aws