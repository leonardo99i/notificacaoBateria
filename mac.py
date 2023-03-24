import asyncio
from bleak import discover

async def discover_devices():
    devices = await discover()
    for device in devices:
        print("Endereço MAC: ", device.address)
        print("Nome do dispositivo: ", device.name)

loop = asyncio.get_event_loop()
loop.run_until_complete(discover_devices())
