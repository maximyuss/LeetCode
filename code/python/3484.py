# https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet:
    def __init__(self, rows: int):
        self.store = {}
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        self.store[cell] = value

    def resetCell(self, cell: str) -> None:
        self.store.pop(cell, None)

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+', 1)
        val_a = int(a) if a.isdigit() else self.store.get(a, 0)
        val_b = int(b) if b.isdigit() else self.store.get(b, 0)
        return val_a + val_b
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
