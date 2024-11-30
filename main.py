import function as f
import os

for file in os.listdir('clients/'):
    f.rooms.append(int(file[4]))

while True:
    cmd = f.input_cmd() 
    if cmd == 0:
        exit()
    elif cmd == 1:
        f.set_client()
    elif cmd == 2:
        f.get_clients()
    elif cmd == 3:
        f.get_client()
    elif cmd == 4:
        f.remove_client()
    elif cmd == 5:
        f.edit_client()
    elif cmd == 6:
        f.to_build_diagram()
    else:
        print('Такой команды не существует!')