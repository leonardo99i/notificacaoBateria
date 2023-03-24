import asyncio
from bleak import BleakScanner

async def print_connected_devices():
    # Escanear por dispositivos Bluetooth usando BleakScanner
    devices = await BleakScanner.discover()

    # Imprimir endereço MAC dos dispositivos conectados
    for device in devices:
        if device.address_type != 0: # ignorar endereços "aleatórios"
            continue

        connected = False
        for s in device.metadata["uuids"]:
            if s.startswith("00001101"): # o UUID de porta serial é 00001101-0000-1000-8000-00805F9B34FB
                connected = True
                break

        if connected:
            print("Endereço MAC:", device.address, "(Conectado)")
        else:
            print("Endereço MAC:", device.address)

asyncio.run(print_connected_devices())
