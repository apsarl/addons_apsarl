REM FR Fichier execute par save_log

@echo off
echo -
echo -
echo -
echo -
echo -

REM FR Definition des dates et heures de la sauvegarde

echo ----------------------------sauvegarde %date%-----------------------------
echo Date du jour : %date%
echo Heure debut : %time%
echo -----------------------------------------------------------------------------

REM FR chemin du serveur OpenERP_Odoo et arret du serveur a modifier si necessaire

PATH=%WINDIR%\system32;%WINDIR%;%WINDIR%\System32\Wbem;.
net stop openerp-server

REM FR chemin du serveur PostgreSQL et lancement du backup
REM FR precisez le chemin de la sauvegarde et le nom de la base de donnees 

cd C:/Program Files (x86)/OpenERP 7.0-20131213-002437/PostgreSQL/bin
pg_dump.exe --host localhost --port 5432 --username "openpg" --role "openpg" --no-password  --format tar --blobs --verbose --file "C:\chemin_de_la_sauvegarde" "nom_bd_a_sauvegarder"
IF errorlevel 0 echo sauvegarde 1 reussie
IF errorlevel 1 echo Erreur de sauvegarde
echo heure fin save 1: %time%
echo -

REM FR chemin du serveur OpenERP_Odoo et arret du serveur a modifier si necessaire

PATH=%WINDIR%\system32;%WINDIR%;%WINDIR%\System32\Wbem;.
net start openerp-server
