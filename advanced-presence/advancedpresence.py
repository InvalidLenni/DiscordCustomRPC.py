from pypresence import Presence
import time

client_id = '850644889423446026'
RPC = Presence(client_id)
RPC.connect()

RPC.update(details="Hi there, i'm Lenni!",
           large_image='coding',
           large_text='invalidlenni.de',
           small_image='avatar',
           small_text='lenni',
           buttons=[{"label": "Github", "url": "https://github.com/InvalidLenni/", "Website", "https://invalidlenni.de/"}],
           start=time.time())
print('Online')

while True:
    time.sleep(600)
