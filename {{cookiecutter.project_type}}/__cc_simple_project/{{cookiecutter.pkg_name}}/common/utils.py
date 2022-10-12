"""
Define here all utility functions that are general purpose and can be used
across the wole program.
"""
from typing import List, Dict


def pick_by_id(llist: List[object], id_value: str) -> Dict[object, object]:
    """
    Returns an element of a list, which is supposed to be adictionary with an "id" field.

    Args:
        llist (List[object]): list to iterate on.
        id_value (str): value of the id.

    Returns:
        Dict[object, object]: found element
    """
    return [ll for ll in llist if ll["id"] == id_value][0]
