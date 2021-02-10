from typing import Iterator, List, Dict
import re
from copy import deepcopy
from tqdm import tqdm
from loguru import logger
from pyroaman.block import Block
from pyroaman.database import Database


def parse_block(raw: Dict) -> Block:
    children = [parse_block(e) for e in raw['children']] \
                if 'children' in raw else []

    metadata = deepcopy(raw)
    if 'children' in metadata:
        del metadata['children']
    if 'string' in metadata:
        del metadata['string']
    if 'title' in metadata:
        del metadata['title']

    if 'string' in raw:
        string = raw['string']
    elif 'title' in raw:
        string = raw['title']
    else:
        string = ''

    return Block(
        string=string,
        is_page='title' in raw,
        metadata=metadata,
        parent=None,
        children=children,
        links=[],
        backlinks=[])


def parse_database(raw: List[Dict]) -> Database:
    def _add_parents(blocks: List[Block]) -> None:
        for parent in blocks:
            for child in parent.children:
                child.parent = parent

    def _add_links(blocks: List[Block]) -> None:
        index = {e.string: e for e in blocks if e.is_page}

        for block in tqdm(blocks):
            references = sorted(set(get_references(block.string)))
            block.links = [index[e] for e in references if e in index]

            for ref in references:
                if ref in index:
                    index[ref].backlinks.append(block)

    logger.info('Parsing blocks')
    blocks = []
    for e in tqdm(raw):
        page = parse_block(e)
        blocks.append(page)
        blocks += list(page.get_descendants())
    _add_parents(blocks)

    logger.info('Creating links')
    _add_links(blocks)

    return Database(blocks)


def get_references(target: str) -> Iterator[str]:
    """Yields all the references ([[example]], #example).
       Supports nested references."""
    stack = []
    i = 0
    while i < len(target)-1:
        if target[i:i+2] == '[[':
            stack.append(i)
            i += 2
        elif stack and target[i:i+2] == ']]':
            start = stack.pop(-1)
            yield target[start+2:i]
            i += 2
        else:
            i += 1

    reg = r"#([a-zA-Z0-9]+)"
    yield from re.findall(reg, target)
