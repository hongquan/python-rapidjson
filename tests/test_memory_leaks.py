# -*- coding: utf-8 -*-
# :Project:   python-rapidjson -- Tracemalloc-based leaks tests
# :Created:   dom 10 feb 2019 13:47:32 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   MIT License
# :Copyright: © 2019 Lele Gaifax
#

import io
import datetime
import gc
import tracemalloc

import pytest
import rapidjson as rj


def object_hook(td):
    if '__td__' in td:
        return datetime.timedelta(td['__td__'])
    else:
        return td


def default(obj):
    if isinstance(obj, datetime.timedelta):
        return {"__td__": obj.total_seconds()}
    else:
        return obj


def test_object_hook_and_default():
    tracemalloc.start()

    data = []
    for i in range(1, 100):
        data.append({"name": "a%d" % i, "timestamp": datetime.timedelta(seconds=i)})

    snapshot1 = tracemalloc.take_snapshot().filter_traces((
        tracemalloc.Filter(True, __file__),))

    for _ in range(1000):
        a = rj.dumps(data, default=default)
        rj.loads(a, object_hook=object_hook)

    gc.collect()

    snapshot2 = tracemalloc.take_snapshot().filter_traces((
        tracemalloc.Filter(True, __file__),))

    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    tracemalloc.stop()

    for stat in top_stats[:10]:
        assert stat.count_diff < 3


def test_load():
    tracemalloc.start()

    snapshot1 = tracemalloc.take_snapshot().filter_traces((
        tracemalloc.Filter(True, __file__),))

    for _ in range(10):
        dct = '{' + ','.join('"foo%d":"bar%d"' % (i, i) for i in range(100)) + '}'
        content = io.StringIO('[' + ','.join(dct for _ in range(100)) + ']')
        rj.load(content, chunk_size=50)

    del content
    del _
    gc.collect()

    snapshot2 = tracemalloc.take_snapshot().filter_traces((
        tracemalloc.Filter(True, __file__),))

    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    tracemalloc.stop()

    for stat in top_stats[:10]:
        assert stat.count_diff < 3
