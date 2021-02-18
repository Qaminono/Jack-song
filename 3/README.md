[#task]()

Двумя неделями позже фрилансер Василий увидел уведомление в телеге, и, подавив в себе нехорошее предчувствие,
открыл мессенджер. Заказчик опять просит доработать API, на этот раз добавив новую функцию с сигнатурой:

    def random_song() -> str
        ...

Функция должна возвращать текст песни со случайным образом перемешанной последовательностью сюжетов,
сохраняя при этом и последовательность событий между куплетами, например:

    This is the cow with the crumpled horn,
    That tossed.

    This is the malt
    That lay in the cow with the crumpled horn,
    That tossed.

    This is the priest all shaven and shorn,
    That married the malt
    That lay in the cow with the crumpled horn,
    That tossed.

"Что за бред? Ведь получится бессвязная ахинея!" -- бабахнул задом об стул Василий, но вспомнил на зубах вкус куриных наггетсов,
которые он смог наконец-то попробовать, согласился.

Помогите Василию справиться с очередными доработками в ТЗ.

UPDATE: действие участников в сюжете должно оставаться сответствеющим исходной песне, смысловая нагрузка неважна:

    the rooster that crow'd in the morn,
    That waked
    +
    the cat,
    That killed
    =
    the cat,
    That killed the rooster that crow'd in the morn,
    That waked