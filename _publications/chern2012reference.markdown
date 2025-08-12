---
layout: publication
title: Reference Based Genome Compression
authors: Bobbie Chern, Idoia Ochoa, Alexandros Manolakos, Albert No, Kartik Venkat,
  Tsachy Weissman
conference: 2012 IEEE Information Theory Workshop
year: 2012
bibkey: chern2012reference
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1204.1912'}]
tags: ["Evaluation"]
short_authors: Chern et al.
---
DNA sequencing technology has advanced to a point where storage is becoming
the central bottleneck in the acquisition and mining of more data. Large
amounts of data are vital for genomics research, and generic compression tools,
while viable, cannot offer the same savings as approaches tuned to inherent
biological properties. We propose an algorithm to compress a target genome
given a known reference genome. The proposed algorithm first generates a
mapping from the reference to the target genome, and then compresses this
mapping with an entropy coder. As an illustration of the performance: applying
our algorithm to James Watson's genome with hg18 as a reference, we are able to
reduce the 2991 megabyte (MB) genome down to 6.99 MB, while Gzip compresses it
to 834.8 MB.