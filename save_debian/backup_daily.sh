#! /bin/bash

#////////////////////////////////////////////////////////////////////////////////////#
# Script de sauvegarde complète d'Odoo DEBIAN                                        #
# Par Richmond FIKO 			                                                     #
# http://www.africaperformances-ci.com/                                              #
# création : 2015-11                                                                 #
# derniere MAJ: 09-01-2016                                                           #
#                                                                                    #
# TO DO: Mettre en oeuvre la restauration du daily sur le serveur                    #
#                                                                                    #
# Le script effectue une sauvegarde complète de la base de données au format dump    #
# A exécuter en 'root'                                                               #
# This program is distributed in the hope that it will be useful,					 #
# but WITHOUT ANY WARRANTY                                                		 	 #
#                                                                                    #
#   Utilisation :                                                                    #
#   -------------                                                                    #
#   Pour exécuter le fichier sous Debian                                             #
#   Placer le fichier dans le répertoire /root                                       #
#   Ouvrir une invite de commande et entrer                                          #
#       cd /root                                                                     #
#       bash ./backup_daily.sh                                                       #
#                                                                                    # 
#////////////////////////////////////////////////////////////////////////////////////#

# ---------------------------------------------------------------------------------- #
# !!!                                IMPORTANT                                     !!!
# ---------------------------------------------------------------------------------- #
#                                                                                    #
# Modifier le fichier pg_hba.conf de PostgreSQL pour autoriser la connexion          #
# sans mot de passe en local comme suit                                              #
#                                                                                    #
# Emplacement du fichier = /etc/postgresql/9.1/main/pg_hba.conf :                    #
# Rajouter ou modifier la ligne ci-dessous :                                         #
#                                                                                    #
# TYPE  DATABASE        USER            ADDRESS                 METHOD               #
# local   all          openerp                                  trust                #
#                                                                                    #
# Pour programmer son exécution automatique créez des taches avec le cron, exple:    #
# https://fr.wikipedia.org/wiki/Cron                                                 #
# ---------------------------------------------------------------------------------- #

# Fichier de LOG
LOG_FILE='/var/log/odoo_backup_daily.log'

# Création du fichier de log
if [ ! -e ${LOG_FILE} ]; then
    echo 'Creation du fichier de log :'${LOG_FILE}
    touch ${LOG_FILE}
fi

######################################################################################
#                               SAUVEGARDE DE LA DB                                  #
######################################################################################

# Nom du répertoire qui contient la sauvegarde à creer s'il n'existe pas (a modifier si necessaire)
SAVE_DIR='/zenfolder/datas/backup'
SAVE_PATH=${SAVE_DIR}'/'

# Nom du sous-répertoire de sauvegarde de la DB
DB_DIR='daily'

# Utilisateur (a modifier si necessaire)
DB_USER='odoo'

# Rôle (a modifier si necessaire)
DB_ROLE='odoo'

# Nom de la base de données (a modifier si necessaire)
DB_NAME='prod'

# Nom du fichier de sauvegarde
FILE_NAME=${DB_NAME}'_DBSAVE_'

# Date de la sauvegarde
DATE_SAVE=`date +%Y-%m-%d`

# Extension du fichier de sauvegarde
FILE_EXT='.backup'

# Le nom complet du fichier de sauvegarde ressemblera à ça:
#    FILE_NAME + DATE_SAVE + FILE_EXT
#    Exemple : MaDbOpenErp_DBSAVE_ + 2013-06-24 + .backup = MaDbOpenErp_DB_2013-06-24.backup

# Chemin du Fichier de sauvegarde
DB_SAVE_PATH=${SAVE_PATH}${DB_DIR}'/'${FILE_NAME}${DATE_SAVE}${FILE_EXT}

#Chemin de recherche Housekeeping
HKP=${SAVE_PATH}${DB_DIR}'/'

echo `date +%Y-%m-%d_%H:%M:%S`'  - Lancement de la Sauvegarde Daily' >> ${LOG_FILE} 2>&1
echo `date +%Y-%m-%d_%H:%M:%S`'  - Lancement de la Sauvegarde Daily'


# Création du répertoire DB si existe pas
if [ ! -d ${SAVE_PATH}${DB_DIR} ]; then
    echo '  - Creation du repertoire :'${SAVE_PATH}${DB_DIR} >> ${LOG_FILE} 2>&1
    echo '  - Creation du repertoire :'${SAVE_PATH}${DB_DIR}
    mkdir ${SAVE_PATH}${DB_DIR}
fi

# Création du répertoire temp si existe pas (necessaire à la restauration du daily - voir TO DO)
#if [ ! -d ${SAVE_PATH}${DB_DIR}/temp ]; then
#    echo '  - Creation du repertoire :'${SAVE_PATH}${DB_DIR}/temp >> ${LOG_FILE} 2>&1
#    echo '  - Creation du repertoire :'${SAVE_PATH}${DB_DIR}/temp
#    mkdir ${SAVE_PATH}${DB_DIR}/temp
#fi

# Stopper serveur Odoo
echo '  - Arret du serveur Odoo' >> ${LOG_FILE} 2>&1
echo '  - Arret du serveur Odoo'
service odoo stop
echo '  - Arret du serveur Odoo OK' >> ${LOG_FILE} 2>&1
echo '  - Arret du serveur Odoo OK'

# Housekeeping(effacer les backups de plus de 15 jours)
#effacer la precedente daily de odoo
echo '  - Housekeeping + 15 jours' >> ${LOG_FILE} 2>&1
echo '  - Housekeeping + 15 jours'

for file in `find ${HKP} -mtime +15 -type f -name *.${FILE_EXT}`
do
  echo "deleting: " $file >> ${LOG_FILE}
  rm $file
done
echo '  - Housekeeping OK' >> ${LOG_FILE} 2>&1
echo '  - Housekeeping OK'

# Sauvegarde de la base de donnée
echo '  - Sauvegarde de la base de donnees OpenERP '${DB_NAME}'. Veuillez patienter...'

psql -U ${DB_USER}
pg_dump --verbose --username ${DB_USER} --role ${DB_ROLE} --no-password --format t --blobs --file ${DB_SAVE_PATH} ${DB_NAME}

echo '  - Sauvegarde de la base de donnees OpenERP terminee' >> ${LOG_FILE} 2>&1
echo '  - Sauvegarde de la base de donnees OpenERP terminee' 

# Attribution des droits à l'utilisateur odoo/odoo : 0755 commande à verifier
echo '  - Mise a jour des permissions' >> ${LOG_FILE} 2>&1
echo '  - Mise a jour des permissions'
chown odoo:odoo ${SAVE_DIR} -R
chmod 777 ${SAVE_DIR} -R

echo '  - Sauvegarde complete OpenERP terminee' >> ${LOG_FILE} 2>&1
echo '  - Sauvegarde complete OpenERP terminee'

# Copie du daily - renommage
#echo '  - Copie du daily - renommage de la derniere save' >> ${LOG_FILE} 2>&1
#echo '  - Copie du daily - renommage de la derniere save'

#cp ${DB_SAVE_PATH} ${SAVE_PATH}${DB_DIR}/temp/daily${FILE_EXT}

#echo '  - Copie renommer OK' >> ${LOG_FILE} 2>&1
#echo '  - Copie renommer OK'

# Restaurer la daily (Uniquement pour le backup daily)
#echo '  - Restauration daily' >> ${LOG_FILE} 2>&1
#echo '  - Restauration daily'

#pg_restore -C ${SAVE_PATH}${DB_DIR}/temp/daily${FILE_EXT}

#echo '  - Restauration daily OK' >> ${LOG_FILE} 2>&1
#echo '  - Restauration daily OK'


# Redemarrer Serveur Odoo
echo '  - Redemarrage du serveur Odoo' >> ${LOG_FILE} 2>&1
echo '  - Redemarrage du serveur Odoo'

service odoo start

echo '  - Redemarrage du serveur Odoo OK' >> ${LOG_FILE} 2>&1
echo '  - Redemarrage du serveur Odoo OK'

echo `date +%Y-%m-%d_%H:%M:%S`'  - Backup Termine smile ;-)' >> ${LOG_FILE} 2>&1
echo `date +%Y-%m-%d_%H:%M:%S`'  - Backup Termine smile ;-)'

echo '------------------------------------' >> ${LOG_FILE} 2>&1

exit 0