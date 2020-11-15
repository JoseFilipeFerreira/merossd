import asyncio 
from quart import Quart
from meross import MerossWrapper

app = Quart(__name__)
light = MerossWrapper()

@app.route('/bulb/')
async def status():
    return light.status()

@app.route('/bulb/on')
async def on():
    return await light.on()

@app.route('/bulb/off')
async def off():
    return await light.off()

@app.route('/bulb/toggle')
async def toggle():
    return await light.toggle()

loop = asyncio.get_event_loop()
loop.run_until_complete(light.connect())
app.run(host='0.0.0.0', port=4200, loop=loop)
