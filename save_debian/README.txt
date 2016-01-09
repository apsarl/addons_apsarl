POUR UTILISER LES SCRIPTS EFFICACEMENT

# TO DO: Mettre en oeuvre la restauration du daily sur le serveur                    #
#                                                                                    #
# Le script effectue une sauvegarde complète de la base de données au format dump    #
# A exécuter en 'root'                                                               #
#                                                                                    #
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
######################################################################################