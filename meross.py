import asyncio
import os

from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

class MerossWrapper():
    def __init__(self):
        self.EMAIL = os.environ.get('MEROSS_EMAIL')
        self.PASSWORD = os.environ.get('MEROSS_PASSWORD')

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

    def status(self):
        return "on" if self.light_on else "off"

    async def toggle(self):
        return await (self.off() if self.light_on else self.on())

    async def on(self):
        for plug in self.plugs:
            await plug.async_turn_on(channel=0)
        self.light_on = True
        return self.status()

    async def off(self):
        for plug in self.plugs:
            await plug.async_turn_off(channel=0)
        self.light_on = False
        return self.status()

    async def close(self):
        self.manager.close()
        await self.http_api_client.async_logout()
