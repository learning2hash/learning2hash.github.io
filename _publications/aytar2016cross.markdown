---
layout: publication
title: Cross-modal Scene Networks
authors: Yusuf Aytar, Lluis Castrejon, Carl Vondrick, Hamed Pirsiavash, Antonio Torralba
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2017
bibkey: aytar2016cross
citations: 127
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.09003'}]
tags: []
short_authors: Aytar et al.
---
People can recognize scenes across many different modalities beyond natural
images. In this paper, we investigate how to learn cross-modal scene
representations that transfer across modalities. To study this problem, we
introduce a new cross-modal scene dataset. While convolutional neural networks
can categorize scenes well, they also learn an intermediate representation not
aligned across modalities, which is undesirable for cross-modal transfer
applications. We present methods to regularize cross-modal convolutional neural
networks so that they have a shared representation that is agnostic of the
modality. Our experiments suggest that our scene representation can help
transfer representations across modalities for retrieval. Moreover, our
visualizations suggest that units emerge in the shared representation that tend
to activate on consistent concepts independently of the modality.