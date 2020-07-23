import time
from pynput.keyboard import Key, Listener

## Press 'space' to attempt a spray
## Press 'esc' to exit
## 5 Spray slots, a slot cannot be activated again until {spray_slot_wait_time} after it has been last activated
## no spray slots are checked until {universal_wait_time} after the last spray slot was activated

# Note for the future, dummy: (time.time() - start_time) gives you a readable cur_time

class Scent:
    def __init__(self, slot_length, u_wait_time, spray_wait_time):
        self.spray_slots = [0] * slot_length # initializes an array of size {slot_length} with a value of 0 at every index
        self.start_time = time.time()
        self.universal_wait = 0
        self.universal_wait_time = u_wait_time # seconds
        self.spray_slot_wait_time = spray_wait_time # seconds

    def spray(self): 
        # Universal wait prevents any sprays for {universal_wait_time} seconds after last spray    
        if time.time() - self.start_time > self.universal_wait:
            # Check through spray_slots to see if current time is greater than their current wait time
            for index, spray_slot in enumerate(self.spray_slots):
                if time.time() - self.start_time >= spray_slot:
                    # Update activated spray_slot wait time
                    self.spray_slots[index] = round( ( (time.time() - self.start_time) + self.spray_slot_wait_time),2 )
                    # Update universal_wait value
                    self.universal_wait = (time.time() - self.start_time) + self.universal_wait_time
                    # # Found and activated a spray slot so return out of function
                    print("Spray from slot {} activated".format(index)) 
                    return 
                else: # This spray slot unavailable
                    print("{:.2f} seconds away from slot {}".format(spray_slot - (time.time() - self.start_time),index))
            print("no available spray slot ")      
        else:
            print("Global wait prevented this spray - {:.2f} seconds until you can activate again".format( self.universal_wait - (time.time() - self.start_time) ) )

def on_release(key):
    if key == Key.space:
        scent.spray()
        print("{} Current Time: {:.2f}\n".format(scent.spray_slots, (time.time() - scent.start_time) ))
    if key == Key.esc:                
        # Stop listener
        return False

scent = Scent(5, 5, 60)
print( "Press 'space' to attempt a spray\n"
 "Press 'esc' to exit\n"
 "5 Spray slots, a slot cannot be activated again until {spray_slot_wait_time} after it has been last activated\n"
 "no spray slots are checked until {universal_wait_time} after the last spray slot was activated)\n")
 
with Listener(
        on_release=on_release) as listener:
    listener.join()
        