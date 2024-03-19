#!/usr/bin/env python3
'''This module contains measure_runtime
'''
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
  '''This method uses gather method
  '''
  start = time.time()
  await asyncio.gather(*(async_comprehension() for _ in range(4)))
  t_s = time.time() - start
  return t_s
