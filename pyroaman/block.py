from typing import List, Dict, Any, Iterator, Optional
import re
from dataclasses import dataclass
from cached_property import cached_property


@dataclass
class Block:
    string: str
    is_page: bool
    metadata: Dict[str, Any]

    parent: Optional['Block']
    children: List['Block']
    links: List['Block']
    backlinks: List['Block']

    @cached_property
    def text(self) -> str:
        return remove_formatting(self.string)

    def get_descendants(self) -> Iterator['Block']:
        yield from self.children
        for ch in self.children:
            yield from ch.get_descendants()

    def get_ancestors(self) -> Iterator['Block']:
        if self.parent:
            yield self.parent
            yield from self.parent.get_ancestors()

    def __hash__(self) -> int:
        return id(self)

    def __repr__(self, max_str_length: int = 35) -> str:
        string = self.string
        if len(string) > max_str_length:
            string = string[:max_str_length-3].rstrip(' ').rstrip('\n') + '...'

        return f'Block (string: "{string}", is_page: {self.is_page}, ' \
             + f'children: {len(self.children)}, links: {len(self.links)}, ' \
             + f'backlinks: {len(self.backlinks)})'


def remove_formatting(target: str) -> str:
    FORMATTING_REG = [
        r'^(.*)!\[.*\]\([^\)]*\)(.*)$',  # image
        r'^(.*)\[.*\]\([^\)]*\)(.*)$',   # links
        r'^(.*)\*\*([^\*]*)\*\*(.*)$',   # bold
        r'^(.*){{[^}]*}}(.*)$',          # command
        r'^(.*)\[\[(.*)$',               # reference start
        r'^(.*)\]\](.*)$',               # reference end
        r'^(.*)#(.*)$',                  # tag
    ]

    def _remove(target: str, reg: str) -> str:
        while True:
            matches = list(re.finditer(reg, target, re.MULTILINE))
            if not matches:
                return target
            match = matches[0]
            target = ''.join(match.groups())

    for reg in FORMATTING_REG:
        target = _remove(target, reg)
    return target
