import asyncio
import aiohttp
import json
import time
import os

appName = "GGSPOTIFYINT" # name for event handling
displayName = "GG Spotify Integration" # name for display
authorName = "benjarojas" # name for display

subpath=r"SteelSeries\SteelSeries Engine 3\coreProps.json"
direction = os.path.join(os.getenv("PROGRAMDATA"), subpath)
endpoint_address = ""

while(1):
    print("Finding server address...")
    try:
        with open(direction) as json_file:
            json_file = json.load(json_file)
            print("Server address found: " + json_file['address'])
            endpoint_address = json_file['address']
            break
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        print("Error: coreProps.json not found")
        print("Is SteelSeries Engine 3 running?")
        time.sleep(5)

# metadata used for registering game
metadata = {
  "game": f"{appName}",
  "game_display_name": f"{displayName}",
  "developer": f"{authorName}",
}
metadata = json.dumps(metadata)

# headers used for POST requests (required, otherwise 400 error)
headers = {
    "Content-Type": "application/json"
}

# register game
async def register_game():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://" + endpoint_address + "/game_metadata", data=metadata, headers=headers) as response:
            if(response.status == 200):
                print("Game registered")
            else:
                print(f"Error: Game registration failed {response.status}")

async def keep_alive():
    async with aiohttp.ClientSession() as session:
        payload = json.dumps({'game': f'{appName}'})
        async with session.post("http://" + endpoint_address + "/game_heartbeat", data=payload, headers=headers) as response:
            if(response.status == 200):
                print("Game heartbeat sent")
            else:
                print(f"Error: Game heartbeat failed to send {response.status}")

async def main():
    await register_game()
    while True:
        await keep_alive()
        await asyncio.sleep(10)

asyncio.run(main())