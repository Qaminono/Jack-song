import random
import warnings
from typing import Optional, List

verses = ['the house that Jack built ',
          'the malt\nThat lay in ',
          'the rat,\nThat ate ',
          'the cat,\nThat killed ',
          'the dog,\nThat worried ',
          'the cow with the crumpled horn,\nThat tossed ',
          'the maiden all forlorn,\nThat milked ',
          'the man all tattered and torn,\nThat kissed ',
          'the priest all shaven and shorn,\nThat married ',
          "the rooster that crow'd in the morn,\nThat waked ",
          'the farmer sowing his corn,\nThat kept ',
          'the horse and the hound and the horn,\nThat belong to ']


def _song_maker(data, reverse):
    all_song = list()
    for i in range(1, len(data) + 1):
        couplet = "This is " + "".join(data[:i][::-1]).strip() + '.'
        all_song.append(couplet[::-1] if reverse else couplet)
    return '\n\n'.join(all_song)


def song(rnd: bool = False, double: bool = False, reverse: bool = False, order: Optional[List[int]] = None) -> str:
    cases = {(False, False): lambda x: x,
             (False, True): lambda x: [verse * 2 for verse in x],
             (True, False): lambda x: random.sample(x, len(x)),
             (True, True): lambda x: [verse * 2 for verse in random.sample(x, len(x))]}
    data = cases[(rnd, double)](verses)
    data = [data[i] for i in order] if order else data
    return _song_maker(data, reverse)


def double_song():
    warnings.warn("'double_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(False, True)


def random_song():
    warnings.warn("'random_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(True, False)
