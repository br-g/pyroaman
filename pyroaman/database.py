from typing import List
from dataclasses import dataclass
from pyroaman.block import Block


@dataclass
class Database:
    blocks: List[Block]

    @property
    def pages(self) -> List[Block]:
        return [b for b in self.blocks if b.is_page]

    def lookup(self, target: str, strict: bool = False,
               case_sensitive: bool = False) -> List[Block]:
        """
        if `strict` is False (default):
            - returns blocks which contain the `target` string.
        if `strict` is True:
            - returns blocks whose content match the `target` string.
        """
        if not case_sensitive:
            target = target.lower()

        res = []
        for block in self.blocks:
            string = block.string if case_sensitive else block.string.lower()

            if strict and string == target:
                res.append(block)
            elif not strict and target in string:
                res.append(block)

        return res

    def __repr__(self) -> str:
        return f'Database ({len(self.pages)} pages, {len(self.blocks)} blocks)'
