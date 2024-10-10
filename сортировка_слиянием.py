from удобства import *


def слить_списки(первый_список: список,
                 второй_список: список,
                 ключ_сортировки: Вызываемый = тождественное_отображение) -> список:
    список_слияния = список()
    и = жы = 0

    while и < длина(первый_список) and жы < длина(второй_список):
        if ключ_сортировки(первый_список[и]) <= ключ_сортировки(второй_список[жы]):
            список_слияния.добавить(первый_список[и])
            и += 1
        else:
            список_слияния.добавить(второй_список[жы])
            жы += 1

    список_слияния.расширить(второй_список[жы:])
    список_слияния.расширить(первый_список[и:])

    return список_слияния


def сортировка_слиянием(список_для_сортировки: список,
                        ключ_сортировки: Вызываемый = тождественное_отображение,
                        на_месте: логический = Ложь) -> список | Ничего:
    if длина(список_для_сортировки) < 2:
        if not на_месте:  
            return список_для_сортировки
        return

    результат_слияния = слить_списки(
        сортировка_слиянием(список_для_сортировки[:длина(список_для_сортировки)//2], ключ_сортировки),
        сортировка_слиянием(список_для_сортировки[длина(список_для_сортировки)//2:], ключ_сортировки),
        ключ_сортировки
    )
    if not на_месте:
        return результат_слияния
    список_для_сортировки[:] = результат_слияния


мой_список = список([5, 4, -5, -1, 1, 3, 7])
печатать(
    *сортировка_слиянием(
        список_для_сортировки=мой_список,
        ключ_сортировки=модуль
    )
)

мой_список = список([5, 4, -5, -1, 1, 3, 7])
сортировка_слиянием(
    список_для_сортировки=мой_список,
    ключ_сортировки=модуль,
    на_месте=Правда
)
печатать(*мой_список)