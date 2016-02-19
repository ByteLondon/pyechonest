from pyechonest import song
from . import util


# just a list I got of the interwebs - don't judge me!
# keep the list short to avoid blowing out rate limits
PLAYLIST = [
  ('Lose Yourself', 'Eminem'),
  ('Dark Horse', 'Katy Perry'),
  ('Bangarang (feat. Sirah)', 'Skrillex')
]


@util.skip_on_rate_limit_exceeded
def test_get_tempo():
    buckets = ['audio_summary']
    for p in PLAYLIST:
        data = song.search(artist=p[1], title=p[0], results=1, buckets=buckets)
        assert data[0].audio_summary['tempo']
