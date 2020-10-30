import asyncio
import os

from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager


class MerossWrapper():
    def __init__(self, fifo_name):
        self.EMAIL = os.environ.get('MEROSS_EMAIL')
        self.PASSWORD = os.environ.get('MEROSS_PASSWORD')
        self.FIFO_NAME = fifo_name

        os.mkfifo(self.FIFO_NAME, 0o600)
        print(f"FIFO named '{self.FIFO_NAME}' is created successfully.")

    async def connect(self):
        self.http_api_client = await MerossHttpClient.async_from_user_password(
                email=self.EMAIL,
                password=self.PASSWORD)

        self.manager = MerossManager(http_client=self.http_api_client, auto_reconnect=True)
        await self.manager.async_init()

        await self.manager.async_device_discovery()
        self.plugs = self.manager.find_devices()

        for plug in self.plugs:
            await plug.async_update()
            self.light_on = plug.is_on()
    
    async def toggle(self):
        if self.light_on:
            await self.off()
        else:
            await self.on()

    async def on(self):
        for plug in self.plugs:
            await plug.async_turn_on(channel=0)
        self.light_on = True

    async def off(self):
        for plug in self.plugs:
            await plug.async_turn_off(channel=0)
        self.light_on = False

    async def listen_fifo(self):
        self.fifo = open(self.FIFO_NAME, "r")

        while True:
            for line in self.fifo:
                if line == "toggle":
                    await self.toggle()
                    print("toggle:", "on" if self.light_on else "off")
                elif line == "on":
                    await self.on()
                    print("on")
                elif line == "off":
                    await self.off()
                    print("off")
                elif line == "close":
                    return
                else:
                    print("ERROR:", line)


    async def close(self):
        # Close the manager and logout from http_api
        self.fifo.close()
        self.manager.close()
        await self.http_api_client.async_logout()

        os.remove(self.FIFO_NAME)

async def main():
    FIFO_NAME = "/tmp/meross.daemon"
    light = MerossWrapper(FIFO_NAME)
    await light.connect()
    await light.listen_fifo()
    await light.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
