---
layout: publication
title: 'Automated Video Labelling: Identifying Faces By Corroborative Evidence'
authors: Andrew Brown, Ernesto Coto, Andrew Zisserman
conference: 2021 IEEE 4th International Conference on Multimedia Information Processing
  and Retrieval (MIPR)
year: 2021
bibkey: brown2021automated
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.05645'}]
tags: []
short_authors: Andrew Brown, Ernesto Coto, Andrew Zisserman
---
We present a method for automatically labelling all faces in video archives,
such as TV broadcasts, by combining multiple evidence sources and multiple
modalities (visual and audio). We target the problem of ever-growing online
video archives, where an effective, scalable indexing solution cannot require a
user to provide manual annotation or supervision. To this end, we make three
key contributions: (1) We provide a novel, simple, method for determining if a
person is famous or not using image-search engines. In turn this enables a
face-identity model to be built reliably and robustly, and used for high
precision automatic labelling; (2) We show that even for less-famous people,
image-search engines can then be used for corroborative evidence to accurately
label faces that are named in the scene or the speech; (3) Finally, we
quantitatively demonstrate the benefits of our approach on different video
domains and test settings, such as TV shows and news broadcasts. Our method
works across three disparate datasets without any explicit domain adaptation,
and sets new state-of-the-art results on all the public benchmarks.