---
layout: publication
title: Forensic Similarity For Digital Images
authors: Owen Mayer, Matthew C. Stamm
conference: IEEE Transactions on Information Forensics and Security
year: 2019
bibkey: mayer2019forensic
citations: 134
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.04684'}]
tags: ["Image Retrieval", "Privacy & Security", "Similarity Search"]
short_authors: Owen Mayer, Matthew C. Stamm
---
In this paper we introduce a new digital image forensics approach called
forensic similarity, which determines whether two image patches contain the
same forensic trace or different forensic traces. One benefit of this approach
is that prior knowledge, e.g. training samples, of a forensic trace are not
required to make a forensic similarity decision on it in the future. To do
this, we propose a two part deep-learning system composed of a CNN-based
feature extractor and a three-layer neural network, called the similarity
network. This system maps pairs of image patches to a score indicating whether
they contain the same or different forensic traces. We evaluated system
accuracy of determining whether two image patches were 1) captured by the same
or different camera model, 2) manipulated by the same or different editing
operation, and 3) manipulated by the same or different manipulation parameter,
given a particular editing operation. Experiments demonstrate applicability to
a variety of forensic traces, and importantly show efficacy on "unknown"
forensic traces that were not used to train the system. Experiments also show
that the proposed system significantly improves upon prior art, reducing error
rates by more than half. Furthermore, we demonstrated the utility of the
forensic similarity approach in two practical applications: forgery detection
and localization, and database consistency verification.