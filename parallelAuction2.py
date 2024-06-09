import threading
import queue
from collections import defaultdict
import numpy as np

# Parameters
n_agents = 5  # Number of agents
items = list(range(5))  # List of items being auctioned

# Global structures
bids = [queue.Queue() for _ in range(n_agents)]
winning_items = [set() for _ in range(n_agents)]
received_bids = defaultdict(lambda: (None, -float('inf')))  # Maps item to (agent_id, bid_amount)

# Helper functions
def valuation_function(agent_id, item):
    # Example valuation function, you might want to customize this
    # np.random.seed(0)
    return np.random.rand()  # Each agent values items differently

def agent_thread(agent_id):
    # Step 2: Agent computes bids
    for item in items:
        bid_amount = valuation_function(agent_id, item)
        print("bid amout: ",bid_amount)
        bids[agent_id].put((item, bid_amount))

def auctioneer_thread():
    # Step 6: Receive bids
    for agent_id in range(n_agents):
        while not bids[agent_id].empty():
            item, bid_amount = bids[agent_id].get()
            if bid_amount > received_bids[item][1]:
                received_bids[item] = (agent_id, bid_amount)
    
    # Step 9: Determine and broadcast winners
    for item, (agent_id, bid_amount) in received_bids.items():
        winning_items[agent_id].add(item)

    # Step 12: Wait for acknowledgments (simulated here)
    for agent_id in range(n_agents):
        print(f"Agent {agent_id} won items: {sorted(list(winning_items[agent_id]))}")

# Running the threads
agent_threads = [threading.Thread(target=agent_thread, args=(i,)) for i in range(n_agents)]
auctioneer_thread = threading.Thread(target=auctioneer_thread)

# Start all threads
for thread in agent_threads:
    thread.start()
auctioneer_thread.start()

# Wait for all threads to complete
for thread in agent_threads:
    thread.join()
auctioneer_thread.join()
