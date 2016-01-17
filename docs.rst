Documentation for greek-utils
=============================

* Convert BetaCode to Unicode
* Turn an iterable into a generator over trigrams
* A Trie datastructure
* MorphGNT BCV string to human-readable verse reference


Convert BetaCode to Unicode
---------------------------

>>> from greekutils.beta2unicode import convert
>>> convert('LO/GOS\n')
'λόγος'

Note that to properly handle final sigma, a ``\n`` should be appended to the
input string.


Turn an iterable into a generator over trigrams
-----------------------------------------------

>>> from greekutils.trigrams import trigrams
>>> list(trigrams('ABC'))
[(None, 'A', 'B'), ('A', 'B', 'C'), ('B', 'C', None)]

This is mostly intended for when you want to iterate over something while
being aware of what is before and after it.


A Trie datastructure
--------------------

Mostly used by ``beta2unicode`` but potentially useful for other applications.

A Trie is like a key-value dictionary but allows for lookup by prefix.

>>> from greekutils.trie import Trie
>>> t = Trie()
>>> t.add('foo', 'bar')
>>> t.find_prefix('food')
('foo', 'bar', 'd')

The tuple returned is the part of the key consumed, the value and the rest
of the key.


MorphGNT BCV string to human-readable verse reference
-----------------------------------------------------

e.g. '010101' to 'Matt 1:1'

Uses SBL short book names by default.

>>> from greekutils.verse_ref import bcv_to_verse_ref
>>> bcv_to_verse_ref('010101')
'Matt 1:1'

If the NT starts at something other than 1, you can provide a ``start``
parameter.

>>> bcv_to_verse_ref('610101', start=61)
'Matt 1:1'

If you want a separator other than a colon, such as a period, you can provide a
``separator`` parameter.

>>> bcv_to_verse_ref('010101', separator='.')
'Matt 1.1'
