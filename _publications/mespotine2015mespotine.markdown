---
layout: publication
title: Mespotine-rle-basic V0.9 - An Overhead-reduced And Improved Run-length-encoding
  Method
authors: Meo Mespotine
conference: Arxiv
year: 2015
bibkey: mespotine2015mespotine
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1501.05542'}]
tags: []
short_authors: Meo Mespotine
---
Run Length Encoding(RLE) is one of the oldest algorithms for data-compression
available, a method used for compression of large data into smaller and
therefore more compact data. It compresses by looking at the data for
repetitions of the same character in a row and storing the amount(called run)
and the respective character(called run_value) as target-data. Unfortunately it
only compresses within strict and special cases. Outside of these cases, it
increases the data-size, even doubles the size in worst cases compared to the
original, unprocessed data. In this paper, we will discuss modifications to
RLE, with which we will only store the run for characters, that are actually
compressible, getting rid of a lot of useless data like the runs of the
characters, that are uncompressible in the first place. This will be achieved
by storing the character first and the run second. Additionally we create a
bit-list of 256 positions(one for every possible ASCII-character), in which we
will store, if a specific (ASCII-)character is compressible(1) or not(0). Using
this list, we can now say, if a character is compressible (store [the
character]+[it's run]) or if it is not compressible (store [the character] only
and the next character is NOT a run, but the following character instead).
Using this list, we can also successfully decode the data(if the character is
compressible, the next character is a run, if not compressible, the next
character is a normal character). With that, we store runs only for characters,
that are compressible in the first place. In fact, in the worst case scenario,
the encoded data will create always just an overhead of the size of the
bit-list itself. With an alphabet of 256 different characters(i.e. ASCII) it
would be only a maximum of 32 bytes, no matter how big the original data was.
[...]