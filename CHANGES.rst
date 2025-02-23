Changes
-------

0.8.0 (2019-08-09)
~~~~~~~~~~~~~~~~~~

* New serialization option ``bytes_mode`` to control how bytes instances gets encoded
  (`issue #122`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/122


0.7.2 (2019-06-09)
~~~~~~~~~~~~~~~~~~

* Hopefully fix the memory leak when loading from a stream (`issue #117`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/117


0.7.1 (2019-05-11)
~~~~~~~~~~~~~~~~~~

* Raise a more specific exception on loading errors, ``JSONDecodeError``, instead of
  generic ``ValueError`` (`issue #118`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/118

* Fix optimization path when using ``OrderedDict``\ s (`issue #119`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/119

* Fix serialization of ``IntEnum``\ s (`issue #121`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/121

* I spent *quite a lot* of time investigating on the memory leak when loading from a
  stream (`issue #117`__): as I was not able to fully replicate the problem, I cannot be
  sure I solved the problem... sorry!

  __ https://github.com/python-rapidjson/python-rapidjson/issues/117


0.7.0 (2019-02-11)
~~~~~~~~~~~~~~~~~~

* Raise correct exception in code samples (`PR #109`__), thanks to Thomas Dähling

  __ https://github.com/python-rapidjson/python-rapidjson/pull/109

* Fix compilation with system-wide install of rapidjson (`issue #110`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/110

* Use current master version of rapidjson, that includes a `fix`__ for its `issue #1368`__
  and `issue #1336`__, and cures several compilation warnings as well (`issue #112`__ and
  `issue #107`__)

  __ https://github.com/Tencent/rapidjson/commit/f5e5d47fac0f654749c4d6267015005b74643dff
  __ https://github.com/Tencent/rapidjson/issues/1368
  __ https://github.com/Tencent/rapidjson/issues/1336
  __ https://github.com/python-rapidjson/python-rapidjson/issues/112
  __ https://github.com/python-rapidjson/python-rapidjson/issues/107

* Fix memory leak when using ``object_hook`` (`issue #115`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/115


0.6.3 (2018-07-11)
~~~~~~~~~~~~~~~~~~

* No visible changes, but now PyPI carries binary wheels for Python 3.7.


0.6.2 (2018-06-08)
~~~~~~~~~~~~~~~~~~

* Use a more specific ValidationError, to differentiate from invalid JSON


0.6.1 (2018-06-06)
~~~~~~~~~~~~~~~~~~

* Nothing new, attempt to build Python 3.6 binary wheels on Travis CI


0.6.0 (2018-06-06)
~~~~~~~~~~~~~~~~~~

* Add a new comparison table involving ``ensure_ascii`` (`issue #98`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/98

* Use Python's ``repr()`` to emit float values instead of rapidjson's ``dtoa()`` (`issue
  #101`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/101

* Use a newer (although unreleased) version of rapidjson to fix an `issue`__ with
  JSONSchema validation (`PR #103`__), thanks to Anthony Miyaguchi

  __ https://github.com/Tencent/rapidjson/issues/825
  __ https://github.com/python-rapidjson/python-rapidjson/pull/103


0.5.2 (2018-03-31)
~~~~~~~~~~~~~~~~~~

* Tiny tweak to restore macOS build on Travis CI


0.5.1 (2018-03-31)
~~~~~~~~~~~~~~~~~~

* Minor tweaks to CI and PyPI deploy configuration


0.5.0 (2018-03-31)
~~~~~~~~~~~~~~~~~~

* New ``RawJSON`` class, allowing inclusion of *pre-serialized* content (`PR #95`__ and
  `PR #96`__), thanks to Silvio Tomatis

  __ https://github.com/python-rapidjson/python-rapidjson/pull/95
  __ https://github.com/python-rapidjson/python-rapidjson/pull/96


0.4.3 (2018-01-14)
~~~~~~~~~~~~~~~~~~

* Deserialize from ``bytes`` and ``bytearray`` instances, ensuring they
  contain valid UTF-8 data

* Speed up parsing of floating point numbers, avoiding intermediary conversion
  to a Python string (`PR #94`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/94


0.4.2 (2018-01-09)
~~~~~~~~~~~~~~~~~~

* Fix precision handling of DM_UNIX_TIME timestamps


0.4.1 (2018-01-08)
~~~~~~~~~~~~~~~~~~

* Fix memory leaks in ``Decoder()`` and ``Encoder()`` classes, related to
  bad handling of ``PyObject_GetAttr()`` result value

* Fix compatibility with Python 3.7a


0.4.0 (2018-01-05)
~~~~~~~~~~~~~~~~~~

* Implemented the streaming interface, see `load()`__ and `dump()`__ (`issue #80`__)

  __ http://python-rapidjson.readthedocs.io/en/latest/load.html
  __ http://python-rapidjson.readthedocs.io/en/latest/dump.html
  __ https://github.com/python-rapidjson/python-rapidjson/issues/80

  **Backward incompatibility**: now the *flags* arguments on all the functions are
  *keyword only*, to mimic stdlib's ``json`` style


0.3.2 (2017-12-21)
~~~~~~~~~~~~~~~~~~

* Reduce compiler warnings (`issue #87`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/87


0.3.1 (2017-12-20)
~~~~~~~~~~~~~~~~~~

* Fix Travis CI recipe to accomodate MacOS


0.3.0 (2017-12-20)
~~~~~~~~~~~~~~~~~~

* Fix compilation on MacOS (`issue #78`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/78

* Handle generic iterables (`PR #89`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/89

  **Backward incompatibility**: the ``dumps()`` function and the ``Encoder()``
  constructor used to accept a ``max_recursion_depth`` argument, to control
  the maximum allowed nesting of Python structures; since the underlying
  function is now effectively recursive, it has been replaced by the generic
  `sys.setrecursionlimit()`__ mechanism

  __ https://docs.python.org/3.6/library/sys.html#sys.setrecursionlimit


0.2.7 (2017-12-08)
~~~~~~~~~~~~~~~~~~

* Restore compatibility with Python < 3.6


0.2.6 (2017-12-08)
~~~~~~~~~~~~~~~~~~

* Fix memory leaks when using object_hook/start_object/end_object


0.2.5 (2017-09-30)
~~~~~~~~~~~~~~~~~~

* Fix bug where error handling code could raise an exception causing a
  confusing exception to be returned (`PR #82`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/82

* Fix bug where loads's ``object_hook`` and dumps's ``default`` arguments
  could not be passed ``None`` explicitly (`PR #83`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/83

* Fix crash when dealing with surrogate pairs (`issue #81`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/81


0.2.4 (2017-09-17)
~~~~~~~~~~~~~~~~~~

* Fix compatibility with MacOS/clang


0.2.3 (2017-08-24)
~~~~~~~~~~~~~~~~~~

* Limit the precision of DM_UNIX_TIME timestamps to six decimal digits


0.2.2 (2017-08-24)
~~~~~~~~~~~~~~~~~~

* Nothing new, attempt to fix production of Python 3.6 binary wheels


0.2.1 (2017-08-24)
~~~~~~~~~~~~~~~~~~

* Nothing new, attempt to fix production of Python 3.6 binary wheels


0.2.0 (2017-08-24)
~~~~~~~~~~~~~~~~~~

* New ``parse_mode`` option, implementing relaxed JSON syntax (`issue #73`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/73

* New ``Encoder`` and ``Decoder``, implementing a class-based interface

* New ``Validator``, exposing the underlying *JSON schema* validation (`issue #71`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/71


0.1.0 (2017-08-16)
~~~~~~~~~~~~~~~~~~

* Remove beta status


0.1.0b4 (2017-08-14)
~~~~~~~~~~~~~~~~~~~~

* Make execution of the test suite on Appveyor actually happen


0.1.0b3 (2017-08-12)
~~~~~~~~~~~~~~~~~~~~

* Exclude CI configurations from the source distribution


0.1.0b2 (2017-08-12)
~~~~~~~~~~~~~~~~~~~~

* Fix Powershell wheel upload script in appveyor configuration


0.1.0b1 (2017-08-12)
~~~~~~~~~~~~~~~~~~~~

* Compilable with somewhat old g++ (`issue #69`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/69

* **Backward incompatibilities**:

  - all ``DATETIME_MODE_XXX`` constants have been shortened to ``DM_XXX``
    ``DATETIME_MODE_ISO8601_UTC`` has been renamed to ``DM_SHIFT_TO_UTC``

  - all ``UUID_MODE_XXX`` constants have been shortened to ``UM_XXX``

* New option ``DM_UNIX_TIME`` to serialize date, datetime and time values as
  `UNIX timestamps`__ targeting `issue #61`__

  __ https://en.wikipedia.org/wiki/Unix_time
  __ https://github.com/python-rapidjson/python-rapidjson/issues/61

* New option ``DM_NAIVE_IS_UTC`` to treat naïve datetime and time values as if
  they were in the UTC timezone (also for issue #61)

* New keyword argument ``number_mode`` to use underlying C library numbers

* Binary wheels for GNU/Linux and Windows on PyPI (one would hope: this is the
  reason for the beta1 release)


0.0.11 (2017-03-05)
~~~~~~~~~~~~~~~~~~~

* Fix a couple of refcount handling glitches, hopefully targeting `issue
  #48`__.

  __ https://github.com/python-rapidjson/python-rapidjson/issues/48


0.0.10 (2017-03-02)
~~~~~~~~~~~~~~~~~~~

* Fix source distribution to contain all required stuff (`PR #64`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/64


0.0.9 (2017-03-02)
~~~~~~~~~~~~~~~~~~

* CI testing on GitHub

* Allow using locally installed RapidJSON library (`issue #60`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/60

* Bug fixes (`issue #37`__, `issue #51`__, `issue #57`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/37
  __ https://github.com/python-rapidjson/python-rapidjson/issues/51
  __ https://github.com/python-rapidjson/python-rapidjson/issues/57


0.0.8 (2016-12-09)
~~~~~~~~~~~~~~~~~~

* Use unpatched RapidJSON 1.1 (`PR #46`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/46

* Handle serialization and deserialization of datetime, date and time
  instances (`PR #35`__) and of UUID instances (`PR #40`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/35
  __ https://github.com/python-rapidjson/python-rapidjson/pull/40

* Sphinx based documentation (`PR #44`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/44

* Refresh benchmarks (`PR #45`__)

  __ https://github.com/python-rapidjson/python-rapidjson/pull/45

* Bug fixes (`issue #25`__, `issue #38`__, `PR #43`__)

  __ https://github.com/python-rapidjson/python-rapidjson/issues/25
  __ https://github.com/python-rapidjson/python-rapidjson/issues/38
  __ https://github.com/python-rapidjson/python-rapidjson/pull/43
