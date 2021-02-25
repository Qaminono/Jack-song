import random
import warnings

verses = ['the horse and the hound and the horn,\nThat belong to ',
          'the farmer sowing his corn,\nThat kept ',
          'the rooster that crow\'d in the morn,\nThat waked ',
          'the priest all shaven and shorn,\nThat married ',
          'the man all tattered and torn,\nThat kissed ',
          'the maiden all forlorn,\nThat milked ',
          'the cow with the crumpled horn,\nThat tossed ',
          'the dog,\nThat worried ',
          'the cat,\nThat killed ',
          'the rat,\nThat ate ',
          'the malt\nThat lay in ',
          'the house that Jack built ']


def _song_maker(data, reverse):
    all_song = list()
    for i in range(1, len(data) + 1):
        couplet = "This is " + "".join(data[-i:]).strip() + '.'
        all_song.append(couplet[::-1] if reverse else couplet)
    return '\n\n'.join(all_song)


def song(rnd: bool = False, double: bool = False, reverse: bool = False) -> str:
    cases = {(False, False): lambda x: x,
             (False, True): lambda x: [verse * 2 for verse in x],
             (True, False): lambda x: random.sample(x, len(x)),
             (True, True): lambda x: [verse * 2 for verse in random.sample(x, len(x))]}
    data = cases[(rnd, double)](verses)
    return _song_maker(data, reverse)


def double_song():
    warnings.warn("'double_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(False, True)


def random_song():
    warnings.warn("'random_song' is deprecated, use parametrized 'song' instead", DeprecationWarning)
    return song(True, False)
