import paramiko
import pprint
FOLDERS = ('documents', 'exchange', 'ietm', 'local_backups', 'reports', 'resources', 'update')


def run_sh(string):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.131.2.11', username='admin', password='qwertyuiop')
    stdin, stdout, stderr = ssh.exec_command(string)
    output = stdout.read().decode()
    ssh.close()
    output = cut_string(output)
    return output


def cut_string(list_of_properties):
    properties_of_folder = {}
    list_of_properties = list_of_properties.split('\n')
    for string in list_of_properties:
        string = str(string).split(' ')
        string = [i for i in string if i]  # удаляем пустые элементы списка
        if len(string) > 3:
            properties_of_folder.setdefault(string[-1], []).append(string[0])
            own = string[2] + ':' + string[3]
            properties_of_folder.setdefault(string[-1], []).append(own)
    return properties_of_folder


def check_sub_folders():
    pass


def check_mod():
    pass


def check_own():
    pass


def main():
    list_of_folders = run_sh('ls -l /opt/seaproject')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(list_of_folders)
    # for folder in list_of_folders:
    #     print(folder)
    #     print(list_of_folders[folder])
    for folder in FOLDERS:
        print(folder + ':')
        # print(run_sh('ls -l /opt/seaproject/' + folder))
        pp.pprint(run_sh('ls -l /opt/seaproject/' + folder))
    # check_mod()
    # check_own()


if __name__ == '__main__':
    main()


