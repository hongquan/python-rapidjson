.. -*- coding: utf-8 -*-
.. :Project:   python-rapidjson -- Encoder class documentation
.. :Author:    Lele Gaifax <lele@metapensiero.it>
.. :License:   MIT License
.. :Copyright: © 2017, 2018, 2019 Lele Gaifax
..

===============
 Encoder class
===============

.. module:: rapidjson

.. testsetup::

   from rapidjson import (Decoder, Encoder, BM_NONE, BM_UTF8, DM_NONE, DM_ISO8601,
                          DM_UNIX_TIME, DM_ONLY_SECONDS, DM_IGNORE_TZ, DM_NAIVE_IS_UTC,
                          DM_SHIFT_TO_UTC, UM_NONE, UM_CANONICAL, UM_HEX, NM_NATIVE,
                          NM_DECIMAL, NM_NAN, PM_NONE, PM_COMMENTS, PM_TRAILING_COMMAS)

.. class:: Encoder(skip_invalid_keys=False, ensure_ascii=True, indent=None, \
                   sort_keys=False, number_mode=None, datetime_mode=None, \
                   uuid_mode=None, bytes_mode=BM_UTF8)

   Class-based :func:`dumps`\ -like functionality.

   :param bool skip_invalid_keys: whether invalid :class:`dict` keys :ref:`will be skipped
                                  <skip-invalid-keys>`
   :param bool ensure_ascii: whether the output should contain :ref:`only ASCII
                             characters <ensure-ascii>`
   :param int indent: indentation width to produce :ref:`pretty printed JSON
                      <pretty-print>`
   :param bool sort_keys: whether dictionary keys should be :ref:`sorted
                          alphabetically <sort-keys>`
   :param int number_mode: enable particular :ref:`behaviors in handling numbers
                           <dumps-number-mode>`
   :param int datetime_mode: how should :ref:`datetime, time and date instances be handled
                             <dumps-datetime-mode>`
   :param int uuid_mode: how should :ref:`UUID instances be handled <dumps-uuid-mode>`
   :param int bytes_mode: how should :ref:`bytes instances be handled <dumps-bytes-mode>`


   .. method:: __call__(obj, stream=None, *, chunk_size=65536)

      :param obj: the value to be encoded
      :param stream: a *file-like* instance
      :param int chunk_size: write the stream in chunks of this size at a time
      :returns: a string with the ``JSON`` encoded `value`, when `stream` is ``None``

      When `stream` is specified, the encoded result will be written there, possibly in
      chunks of `chunk_size` bytes at a time, and the return value will be ``None``.

   .. method:: default(value)

      :param value: the Python value to be encoded
      :returns: a *JSON-serializable* value

      If implemented, this method is called whenever the serialization machinery finds a
      Python object that it does not recognize: if possible, the method should returns a
      *JSON encodable* version of the `value`, otherwise raise a :exc:`TypeError`:

      .. doctest::

         >>> class Point:
         ...   def __init__(self, x, y):
         ...     self.x = x
         ...     self.y = y
         ...
         >>> point = Point(1,2)
         >>> Encoder()(point)
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
         TypeError: <__main__.Point object at …> is not JSON serializable
         >>> class PointEncoder(Encoder):
         ...   def default(self, obj):
         ...     if isinstance(obj, Point):
         ...       return {'x': obj.x, 'y': obj.y}
         ...     else:
         ...       raise TypeError('%r is not JSON serializable' % obj)
         ...
         >>> pe = PointEncoder(sort_keys=True)
         >>> pe(point)
         '{"x":1,"y":2}'

      When you want to treat your :class:`bytes` instances in a special way, you can use
      :data:`BM_NONE` together with this method:

      .. doctest::

         >>> class HexifyBytes(Encoder):
         ...   def default(self, obj):
         ...     if isinstance(obj, bytes):
         ...       return obj.hex()
         ...     else:
         ...       return obj
         ...
         >>> small_numbers = bytes([1, 2, 3])
         >>> hb = HexifyBytes(bytes_mode=BM_NONE)
         >>> hb(small_numbers)
         '"010203"'
