#!/usr/bin/env python3
'''This module's function.
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''This will retrieve the first item from a sequence.
    '''
    if lst:
        item_ = lst[0]
        return item
    return None
