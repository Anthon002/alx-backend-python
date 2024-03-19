#!/usr/bin/env python3
'''This modulle constains async_generator method
'''
import random
import asyncio


async def async_generator():
    '''This method generates 10 random numbers
    '''
    randarr = []
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
