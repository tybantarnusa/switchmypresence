from pypresence import Presence
from dotenv import load_dotenv
import time
import os

class Discord:
    def __init__(self, state, details, large_image):
        load_dotenv()

        self.client_id = os.environ.get("CLIENT_ID")
        self.RPC = Presence(self.client_id)

        self.state = state
        self.details = details
        self.large_image = large_image
        self.large_text = details

    def present(self):
        self.RPC.connect()
        
        start_time = int(time.time())
        
        self.RPC.update(state=self.state, details=self.details, large_image=self.large_image, large_text=self.large_text, start=start_time)
        while True:
            time.sleep(15)
    
    def stop(self):
        self.RPC.clear()