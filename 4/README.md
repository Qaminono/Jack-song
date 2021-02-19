[#task]()

Однажды вечером, поправившийся на жирных бигмаках жирный Василий, теперь уже солидный и успешный самозанятый с ИП,
сидел и клепал очередную CRUD-форму на Реакте, когда в тележеньку ему постучал молчавший полтора года аккаунт тех самых курсов,
с работы на которых началась его карьера. "#%@#$. Только не @!%#$^& легаси, пусть и мой." -- подумал Василий,
но нелёгкая фрилансерская жизнь научила его, что вменяемого и щедрого заказчика надо беречь и облизывать.

    - Василий, помнишь, ты делал для нас апишку с английскими песнями? Ты не поверишь,
    но нас купил тот самый ИзиИелтс и мы теперь у них топовый отдел. Прости, что отвлекаю,
    но от нас требуют заменить твой API на стандартный из гайдлайнов, ну а кто с этим справится лучше,
    чем его автор? Выручишь?
    - Не вопрос, дружище, я тебе многим обязан. -- ответил Василий и погрузился в чтение присланного ТЗ.

ТЗ требует переделать публичный API модуля:

    - добавить в функцию song() два bool параметра-переключателя режимов
    формирования текста песни:

    def song(rnd: bool=False, double: bool=False) -> str:
        ...

Все комбинации параметров должны работать правильно:

    song(rnd=False, double=False) -> utf-8 строка с текстом песни в соответствии с ТЗ-1
    song(rnd=False, double=True) -> utf-8 строка текстом песни в соответствии с ТЗ-2
    song(rnd=True, double=False) -> utf-8 строка текстом песни в соответствии с ТЗ-3
    song(rnd=True, double=True) -> utf-8 строка с текстом песни, модифицированным согласно ТЗ-2 и ТЗ-3 одновременно

Пример для ситуации 4:

    This is the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked.

    This is the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked.

    This is the house that Jack built the house that Jack built the farmer sowing his corn,
    That kept the farmer sowing his corn,
    That kept the maiden all forlorn,
    That milked the maiden all forlorn,
    That milked.

Помогите Василию отрефакторить его говнокод.

Задача со звёздочкой:

Пометить функции random_song() и double_song() как устаревшие, для чего вывести стандартное оповещение при попытке их использовать:

        DeprecationWarning: '<имя_функции>' is deprecated, use parametrized 'song' instead

функции при этом должны выполнять свои контракты