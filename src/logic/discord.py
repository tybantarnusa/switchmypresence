from pypresence import Presence
import time
import os

class Discord:
    def __init__(self, state, large_image):
        self.client_id = 848100876773621771 
        self.RPC = Presence(self.client_id)

        self.state = state
        self.large_image = large_image
        self.large_text = state

    def present(self):
        self.RPC.connect()
        start_time = int(time.time())
        self.RPC.update(state=self.state, large_image=self.large_image, large_text=self.large_text, start=start_time)
    
    def stop(self):
        self.RPC.clear()