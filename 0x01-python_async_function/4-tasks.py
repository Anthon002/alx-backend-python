#!/usr/bin/env python3
'''This module contains the implementation for task_wait_n
'''
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
  '''this method will execute the task_wait_random n number of times.
  '''
  delays = await asyncio.gather(
    *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
  )
  sorted_delays = sorted(delays)
  return sorted(delays)
