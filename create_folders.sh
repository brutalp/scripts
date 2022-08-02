#!/bin/bash
list_folders=("documents" "resources" "backups" "local_backups" "remote_backups" "ietm")
function check_folders {
    local folders
    folders=("$@")
    for folder in ${folders[@]}; do
        if ! [ -d /opt/seaproject/$folder ]; then
            echo "folder $folder doesnt exist"
            mkdir -p /opt/seaproject/$folder/0
            echo "folder $folder created"
            if [ "$folder" = "documents" -o "$folder" = "resources" -o "$folder" = "remote_backups" -o "$folder" = "local_backups" ]; then
                chmod 770 -Rv /opt/seaproject/$folder
                chown admin:users -Rv /opt/seaproject/$folder
                echo "for folder $folder rights are given"
            elif [ $folder = "ietm" ]; then
                chmod 750 -Rv /opt/seaproject/$folder
                chown admin:users -Rv /opt/seaproject/$folder
            fi
        else
            echo "$folder is exist!"
        fi
    done
}
check_folders ${list_folders[*]}
