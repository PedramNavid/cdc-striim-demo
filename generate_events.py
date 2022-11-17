import json
import os

import time
import psycopg
from fake_web_events import Simulation
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
if not DATABASE_URL:
    raise Exception("DATABASE_URL is not set. Please specify it in the .env file")
simulation = Simulation(user_pool_size=1000, sessions_per_day=100000)

while True:
    events = simulation.run(duration_seconds=5)

    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            for payload in events:
                cur.execute(
                    "INSERT INTO public.web_events(event_id, event_time, payload) "
                    "VALUES (%s, %s, %s);",
                    [
                        payload["event_id"],
                        payload["event_timestamp"],
                        json.dumps(payload),
                    ],
                )

    print("Batch complete, taking a breather...")
    time.sleep(5)
