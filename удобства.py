from typing import Callable


Ничего = None
Вызываемый = Callable
тождественное_отображение = lambda x: x
длина = len
печатать = print
модуль = abs
логический = bool
Правда = True
Ложь = False
целое = int
последовательно_применить = map


class список(list):
    def добавить(self, x):
        return self.append(x)

    def расширить(self, x):
        return self.extend(x)
