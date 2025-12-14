---
layout: publication
title: 'Sketching Without Worrying: Noise-tolerant Sketch-based Image Retrieval'
authors: Ayan Kumar Bhunia, Subhadeep Koley, Abdullah Faiz Ur Rahman Khilji, Aneeshan
  Sain, Pinaki Nath Chowdhury, Tao Xiang, Yi-Zhe Song
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: bhunia2022sketching
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.14817'}]
tags: [Evaluation, CVPR, Image Retrieval]
short_authors: Bhunia et al.
---
Sketching enables many exciting applications, notably, image retrieval. The
fear-to-sketch problem (i.e., "I can't sketch") has however proven to be fatal
for its widespread adoption. This paper tackles this "fear" head on, and for
the first time, proposes an auxiliary module for existing retrieval models that
predominantly lets the users sketch without having to worry. We first conducted
a pilot study that revealed the secret lies in the existence of noisy strokes,
but not so much of the "I can't sketch". We consequently design a stroke subset
selector that \{detects noisy strokes, leaving only those\} which make a positive
contribution towards successful retrieval. Our Reinforcement Learning based
formulation quantifies the importance of each stroke present in a given subset,
based on the extent to which that stroke contributes to retrieval. When
combined with pre-trained retrieval models as a pre-processing module, we
achieve a significant gain of 8%-10% over standard baselines and in turn report
new state-of-the-art performance. Last but not least, we demonstrate the
selector once trained, can also be used in a plug-and-play manner to empower
various sketch applications in ways that were not previously possible.