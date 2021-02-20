[#task]()

Добавить в функцию song() ещё один флаг, управляющий выводом:

    def song(rnd: bool=False, double: bool=False, reverse: bool=False) -> str:

При установке флага reverse в True текст куплета доложен выводиться задом наперёд:

    .tliub kcaJ taht esuoh eht si sihT

    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht si sihT

    .tliub kcaJ taht esuoh eht ni yal tahT
    tlam eht eta tahT
    ,tar eht si sihT

Все остальные флаги должны выполнять свои функции как прежде. Две депрекатнутые функции также должны работать как прежде.