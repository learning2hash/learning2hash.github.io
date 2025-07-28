---
layout: publication
title: Videostory Embeddings Recognize Events When Examples Are Scarce
authors: Amirhossein Habibian, Thomas Mensink, Cees G. M. Snoek
conference: Arxiv
year: 2015
bibkey: habibian2015videostory
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.02492'}]
tags: []
short_authors: Amirhossein Habibian, Thomas Mensink, Cees G. M. Snoek
---
This paper aims for event recognition when video examples are scarce or even
completely absent. The key in such a challenging setting is a semantic video
representation. Rather than building the representation from individual
attribute detectors and their annotations, we propose to learn the entire
representation from freely available web videos and their descriptions using an
embedding between video features and term vectors. In our proposed embedding,
which we call VideoStory, the correlations between the terms are utilized to
learn a more effective representation by optimizing a joint objective balancing
descriptiveness and predictability.We show how learning the VideoStory using a
multimodal predictability loss, including appearance, motion and audio
features, results in a better predictable representation. We also propose a
variant of VideoStory to recognize an event in video from just the important
terms in a text query by introducing a term sensitive descriptiveness loss. Our
experiments on three challenging collections of web videos from the NIST
TRECVID Multimedia Event Detection and Columbia Consumer Videos datasets
demonstrate: i) the advantages of VideoStory over representations using
attributes or alternative embeddings, ii) the benefit of fusing video
modalities by an embedding over common strategies, iii) the complementarity of
term sensitive descriptiveness and multimodal predictability for event
recognition without examples. By it abilities to improve predictability upon
any underlying video feature while at the same time maximizing semantic
descriptiveness, VideoStory leads to state-of-the-art accuracy for both few-
and zero-example recognition of events in video.