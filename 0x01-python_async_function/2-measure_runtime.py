#!/usr/bin/env python3
'''This module contains the implementation for measure_time
'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''returns average time
    '''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
