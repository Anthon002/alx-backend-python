#!/usr/bin/env python3
'''This module's function element_length.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''This function will calc the length of the list of sequences.
    '''
    length = [(j, len(j)) for j in lst]
    return length
