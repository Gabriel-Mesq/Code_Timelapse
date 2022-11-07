# Transcrever, letra por letra, o código de um arquivo para outro.
# Efetivamente, simulando uma timelapse da criação de um código.

import time

#Insira aqui o código já escrito
origem = ''

#Insira aqui o nome do arquivo onde irá ocorrer a timelapse
destino = ''

with open(f'{origem}', 'r') as code:
    for line in code:
        for i in range(len(line)):
            with open(f'{destino}', 'a') as tl_code:
                tl_code.write(line[i])
                if line[i] != ' ':
                    time.sleep(0.05)
