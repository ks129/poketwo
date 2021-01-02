import os

token = os.environ["TOKEN"]
prefix = os.environ["PREFIX"]
cogs = [x.strip() for x in os.getenv("COGS", "").split(",")]
amqp_url = os.environ["AMQP_URL"]
redis_url = os.environ["REDIS_URL"]
db_url = os.environ["DB_URL"]
