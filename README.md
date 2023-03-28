# Bluetooth Battery Monitor
Este é um script Python que monitora a bateria de dispositivos Bluetooth específicos e notifica o usuário sobre o nível de bateria desses dispositivos. O script usa a biblioteca Bleak para se conectar aos dispositivos Bluetooth e a biblioteca Plyer para notificar o usuário sobre o status da bateria dos dispositivos.

# Pré-requisitos
Python 3.7 ou superior
As bibliotecas Bleak e Plyer instaladas
Você pode instalar as bibliotecas usando o pip:
`pip install bleak plyer`

# Como usar
Abra o arquivo bluetooth_battery_monitor.py em um editor de texto.
Edite o dicionário devices para adicionar os dispositivos Bluetooth que você deseja monitorar. Cada entrada do dicionário deve ter o nome do dispositivo como a chave e o endereço MAC do dispositivo como o valor. Por exemplo:
`
 devices = {
    "Dispositivo 1": "12:34:56:78:90:AB",
    "Dispositivo 2": "AB:CD:EF:12:34:56"
}
`

Salve o arquivo e execute o script usando o seguinte comando: `python bluetooth_battery_monitor.py`

O script começará a monitorar a bateria dos dispositivos Bluetooth especificados e notificará o usuário sobre o status da bateria desses dispositivos a cada hora.

# Como funciona
O script usa uma função assíncrona get_battery_level() para se conectar a um dispositivo Bluetooth usando BleakClient e obter o nível de bateria do dispositivo. Se ocorrer um erro ao conectar-se ao dispositivo, a função retorna uma mensagem de erro.

O script usa outra função assíncrona scan_devices() para varrer todos os dispositivos Bluetooth especificados no dicionário devices e obter o nível de bateria de cada dispositivo usando a função get_battery_level(). Se houver um erro ao conectar-se a um dispositivo, uma notificação é exibida com a mensagem de erro. Caso contrário, os dados do dispositivo (nome e nível de bateria) são adicionados a uma lista devices_data que é retornada no final da função.

O script usa uma terceira função assíncrona send_notification() para criar uma mensagem com o nome e o nível de bateria de cada dispositivo e exibir a mensagem como uma notificação para o usuário usando a função notification.notify() da biblioteca Plyer.

Finalmente, o script usa a função assíncrona principal main() para executar continuamente as funções scan_devices() e send_notification() em um loop infinito a cada hora. O usuário é notificado sobre o status da bateria dos dispositivos Bluetooth a cada hora.
