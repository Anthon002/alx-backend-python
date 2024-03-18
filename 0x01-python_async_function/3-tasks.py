#!/usr/bin/env python3
'''This module contains the implementaion for task_wait_random
'''
import asyncio as asy


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asy.Task:
  '''This method create asynchronous task for the wait_random.
  '''
  task_ = asy.create_task(wait_random(max_delay))
  return task_
