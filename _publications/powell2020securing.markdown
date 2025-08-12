---
layout: publication
title: Securing LSB Embedding Against Structural Steganalysis
authors: Brian A. Powell
conference: Arxiv
year: 2020
bibkey: powell2020securing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.03658'}]
tags: []
short_authors: Brian A. Powell
---
This work explores the extent to which LSB embedding can be made secure
against structural steganalysis through a modification of cover image
statistics prior to message embedding. Natural images possess symmetries that
are expressed through approximately equal cardinalities of certain sets of
\(k\)-tuples of consecutive pixels. LSB embedding disturbs this balance and a
\(k^\{\rm th\}\)-order structural attack infers the presence of a hidden message
with a length in proportion to the size of the imbalance amongst sets of
\(k\)-tuples. To protect against \(k^\{\rm th\}\)-order structural attacks, cover
modifications involve the redistribution of \(k\)-tuples among the different sets
so that symmetries of the cover image are broken, then repaired through the act
of LSB embedding so that the stego image bears the statistics of the original
cover. To protect against all orders up to some order \(k\), the statistics of
\(n\)-tuples must be preserved where \(n\) is the least common multiple of all
orders \(\leq k\). We find that this is only feasible for securing against up to
\(3^\{\rm rd\}\)-order attacks (Sample Pairs and Triples analyses) since
higher-order protections result in virtually zero embedding capacities.
Securing up to \(3^\{\rm rd\}\)-order requires redistribution of sextuplets: rather
than perform these \(6^\{\rm th\}\)-order cover modifications, which result in tiny
embedding capacities, we reduce the problem to the redistribution of triplets
in a manner that also preserves the statistics of pairs. This is done by
embedding into only certain pixels of each sextuplet, constraining the maximum
embedding rate to be \(\leq 2/3\) bits per channel. Testing on a variety of image
formats, we report best performance for JPEG-compressed images with a mean
maximum embedding rate undetectable by \(2^\{\rm nd\}\)- and \(3^\{\rm rd\}\)-order
attacks of 0.21 bits per channel.