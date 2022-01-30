from pypresence import Presence
import time

client_id = '[VAR.clientid]'
RPC = Presence(client_id)
RPC.connect()

RPC.update(details="[VAR.details]",
           large_image='[VAR.largeImageKey]',
           large_text='[VAR.largeImageText]',
           small_image='[VAR.smallImageKey]',
           small_text='[VAR.smallImageText]',
           buttons=[{"label": "Github", "url": "https://github.com/InvalidLenni/", "Website", "https://invalidlenni.de/"}],
           start=time.time())
print('Online')

while True:
    time.sleep(600)
