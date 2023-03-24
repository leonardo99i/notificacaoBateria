import asyncio
from bleak import discover

# Tabela de classes de serviço Bluetooth
# Referência: https://www.bluetooth.com/specifications/assigned-numbers/service-discovery/
SERVICE_CLASSES = {
    0x0025: "Fone de Ouvido",
    0x0028: "Teclado",
    0x0029: "Mouse",
}

async def discover_devices():
    devices = await discover()
    for device in devices:
        print("Endereço MAC: ", device.address)
        print("Nome do dispositivo: ", device.name)
        print("")

        # Obter a classe de serviço do dispositivo
        services = device.metadata["uuids"]
        service_class = None
        for service in services:
            service_class = int(service.split("-")[0], 16)
            if service_class in SERVICE_CLASSES:
                break

        # Imprimir o tipo de dispositivo se a classe de serviço for reconhecida
        if service_class in SERVICE_CLASSES:
            print("Tipo de dispositivo: ", SERVICE_CLASSES[service_class])
        else:
            print("Tipo de dispositivo: Desconhecido")

loop = asyncio.get_event_loop()
loop.run_until_complete(discover_devices())
