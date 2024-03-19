#!/usr/bin/env python3
'''This module constains the async_comprehension method
'''
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''This method uses async list comprehension
    '''
    async_comp = [i async for i in async_generator()]
    return async_comp
