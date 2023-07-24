import asyncio
from bleak import BleakClient

address = "f1:bf:ba:4a:9b:ec"

async def main(address):
	print("Connecting ...")
	client = BleakClient(address)
	try:
		await client.connect()
		print("Connected");
	except Exception as e:
		print(e)
	finally:
		print("finally");
		await client.disconnect()

asyncio.run(main(address))
