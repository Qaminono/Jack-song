[#task]()

Через неделю тот же заказчик связался с фрилансером Василием и попросил внести доработку в выполненный заказ.
Заказчик просит добавить к существующему API написанного Василием модуля новую функцию,
которая будет возвращать текст песни, предварительно удвоив каждый из сюжетных ходов.
Удвоение выполняется простой конкатенацией строки через пробел:

    This is the house that Jack built the house that Jack built.

    This is the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    This is the rat,
    That ate the rat,
    That ate the malt
    That lay in the malt
    That lay in the house that Jack built the house that Jack built.

    ...

Функция должна иметь сигнатуру:

    def double_song() -> str
        ...

Василий подумал: "Ничего не понял и конкурс какой-то неинтересный", но выпендриваться не стал и согласился, вспомнив,
как всю неделю он вкусно жрал пюрешку Бигбон вместо своих обычных фриланс-пакетов.

Решения в виде Python-Модуля, содержащего обе функции, присылать в личку игреку.

UPDATE:
    
    the rat,
    That ate
    — "сюжет"
    the rat,
    That ate
    +
    the rat,
    That ate
    ==
    the rat,
    That ate the rat,
    That ate
    конкатенация

Запятые — см. решение первой части, удваиваются только там, где есть.

Продолжение следует...