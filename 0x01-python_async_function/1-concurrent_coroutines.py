#!/usr/bin/env python3
'''This module contains the implementation of wait_n
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay: int) -> List[float]:
  '''This method calls the wait_n multiple times
  '''
  asynclist = []
  for i in range(n):
    asynclist.append(await wait_random(max_delay))
  return asynclist
