---
layout: publication
title: Levels Of Binary Equivalence For The Comparison Of Binaries From Alternative
  Builds
authors: Jens Dietrich, Tim White, Behnaz Hassanshahi, Paddy Krishnan
conference: Arxiv
year: 2024
bibkey: dietrich2024levels
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2410.08427'}]
tags: []
short_authors: Dietrich et al.
---
In response to challenges in software supply chain security, several
organisations have created infrastructures to independently build commodity
open source projects and release the resulting binaries. Build platform
variability can strengthen security as it facilitates the detection of
compromised build environments. Furthermore, by improving the security posture
of the build platform and collecting provenance information during the build,
the resulting artifacts can be used with greater trust. Such offerings are now
available from Google, Oracle and RedHat. The availability of multiple binaries
built from the same sources creates new challenges and opportunities, and
raises questions such as: 'Does build A confirm the integrity of build B?' or
'Can build A reveal a compromised build B?'. To answer such questions requires
a notion of equivalence between binaries. We demonstrate that the obvious
approach based on bitwise equality has significant shortcomings in practice,
and that there is value in opting for alternative notions. We conceptualise
this by introducing levels of equivalence, inspired by clone detection types.
  We demonstrate the value of these new levels through several experiments. We
construct a dataset consisting of Java binaries built from the same sources
independently by different providers, resulting in 14,156 pairs of binaries in
total. We then compare the compiled class files in those jar files and find
that for 3,750 pairs of jars (26.49%) there is at least one such file that is
different, also forcing the jar files and their cryptographic hashes to be
different. However, based on the new equivalence levels, we can still establish
that many of them are practically equivalent. We evaluate several candidate
equivalence relations on a semi-synthetic dataset that provides oracles
consisting of pairs of binaries that either should be, or must not be
equivalent.