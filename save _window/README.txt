Script de sauvegarde complète d'OpenERP/Odoo WINDOWS                                        
Par Richmond FIKO :                                               
http://www.africaperformances-ci.com/                                     
création : 2013                                                        
derniere MAJ: 09-01-2016  

* IMPORTANT: Ce programme est distribué dans l'objectif d'etre utile mais sans aucune garantie
                                             		 	
Ces scripts ont été testés avec succes sur OpenERP V7
Pour exécuter ces scripts:
- copiez les dans un repertoire du C:\
- definir et/ou creez le repertoire de sauvegarde
- dans "save.bat", verifiez le chemin du server OpenERP/Odoo
- dans "save.bat", verifiez le chemin du /bin PostgreSQL (repertoire ou se trouve l'exécutable "pg_dump.exe" par defaut)
- dans "save.bat", modifiez le nom de la base à sauvegarder
- pour l'exécuter, vous faites un clic droit sur "save_log.bat" puis exécutez le en temps qu'administrateur
- un ficher de log (dbsave_log.txt) est crée au lancement de la premiere sauvegarde
- si vous souhaitez programmer les heures de backup, vous pouvez utiliser le planificateur de taches windows pour lancer le script "save_log.bat"
Tuto: http://windows.microsoft.com/fr-fr/windows/schedule-task
