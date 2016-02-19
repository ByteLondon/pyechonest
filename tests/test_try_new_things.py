from pyechonest import artist, playlist
from . import util


ARTISTS = ['Arcade Fire', 'Feist', 'Vampire Weekend']


@util.skip_on_rate_limit_exceeded
def test_get_tracks_without_audio():
    seed_ids = [artist.Artist(a).id for a in ARTISTS]
    assert len(seed_ids) == len(ARTISTS)

    raw_plist = playlist.static(type='artist-radio', artist_id=seed_ids, variety=1)
    assert len(raw_plist) >= len(seed_ids)


@util.skip_on_rate_limit_exceeded
def test_get_tracks_with_audio():
    seed_ids = [artist.Artist(a).id for a in ARTISTS]
    assert len(seed_ids) == len(ARTISTS)

    raw_plist = playlist.static(type='artist-radio', artist_id=seed_ids, variety=1, buckets = ['id:7digital-US', 'tracks'], limit=True)
    assert len(raw_plist) >= len(seed_ids)

    tuple_plist = [s.get_tracks('7digital-US', [{}])[0].get('preview_url') for s in raw_plist]
    assert len(tuple_plist) == len(raw_plist)
