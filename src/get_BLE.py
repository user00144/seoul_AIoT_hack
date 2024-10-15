import asyncio
import requests
from bleak import BleakClient
import datetime
import json

address = "BE29D9DB-34CA-1856-881A-736BC0E021F3"
read_write_charcteristic_uuid = "bb5cb03b-9a27-48c9-8a6b-b7ddff9a4e87"
url = 'http://localhost:8000/acc'
headers = {'Content-Type': 'application/json'}


def notify_callback(sender: int, data: bytearray):
    print('sender: ', sender, 'data: ', data)

async def run(address):    
    async with BleakClient(address) as client:
        is_zero = True
        print('connected')
        while(True) :
            await asyncio.sleep(0.5)
            read_data = await client.read_gatt_char(read_write_charcteristic_uuid)
            integer_data = int(read_data.decode('utf-8'))
            if integer_data == 1 and is_zero :
                cur_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                data = {
                    "id" : "ids_000001",
                    "category" : "Fence_Damage",
                    "date" : cur_time # Stirng
                }
                response = requests.post(url, data=json.dumps(data), headers=headers)
                print(response)
            is_zero = (integer_data == 0)
    print('disconnect')

asyncio.run(run(address))
