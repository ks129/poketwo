from dataclasses import dataclass
from typing import List


@dataclass
class Config:
    token: str
    prefix: str
    cogs: List[str]
    amqp_url: str
    redis_url: str
    db_url: str
