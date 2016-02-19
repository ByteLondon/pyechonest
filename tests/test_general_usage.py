from pyechonest import artist, song
from . import util


@util.skip_on_rate_limit_exceeded
def test_find_artists_similar_to():
    bk = artist.Artist('Bikini Kill')
    assert len(bk.similar) != 0
    for a in bk.similar:
        assert a.name


@util.skip_on_rate_limit_exceeded
def test_search_for_artist():
    results = artist.search(name='Weezer')
    weezer = results[0]
    assert weezer.name == 'Weezer'
    assert len(weezer.blogs) != 0
    for b in weezer.blogs:
        assert b.get('url')


@util.skip_on_rate_limit_exceeded
def test_get_artist_by_name():
    a = artist.Artist('Lady Gaga')
    assert a.id == 'ARX6TAQ11C8A415850'
    assert a.name == 'Lady Gaga'


@util.skip_on_rate_limit_exceeded
def test_get_artist_by_musicbrainz_id():
    a = artist.Artist('musicbrainz:artist:a74b1b7f-71a5-4011-9441-d0b5e4122711')
    assert a.id == 'ARH6W4X1187B99274F'
    assert a.name == 'Radiohead'


@util.skip_on_rate_limit_exceeded
def test_get_hottest_artists():
    hot = artist.top_hottt()
    assert len(hot) > 0


@util.skip_on_rate_limit_exceeded
def test_get_song_audio_and_analysis():
    buckets = ['id:7digital-US', 'tracks']
    the_songs = song.search(artist='The National', title='Slow Show', buckets=buckets, limit=True)
    assert len(the_songs) > 0 # at least 1 matching song
    the_song = the_songs[0]
    assert the_song.title == 'Slow Show'
    tracks = the_song.get_tracks('7digital-US')
    assert len(tracks) > 0 # at least 1 track for the song
    assert tracks[0]['album_name'] == 'Boxer'
