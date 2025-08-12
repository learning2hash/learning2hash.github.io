---
layout: publication
title: Constrained Mean Shift Using Distant Yet Related Neighbors For Representation
  Learning
authors: Kl Navaneet, Soroush Abbasi Koohpayegani, Ajinkya Tejankar, Kossar Pourahmadi,
  Akshayvarun Subramanya, Hamed Pirsiavash
conference: Lecture Notes in Computer Science
year: 2022
bibkey: navaneet2021constrained
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.04607'}]
tags: []
short_authors: Navaneet et al.
---
We are interested in representation learning in self-supervised, supervised,
and semi-supervised settings. Some recent self-supervised learning methods like
mean-shift (MSF) cluster images by pulling the embedding of a query image to be
closer to its nearest neighbors (NNs). Since most NNs are close to the query by
design, the averaging may not affect the embedding of the query much. On the
other hand, far away NNs may not be semantically related to the query. We
generalize the mean-shift idea by constraining the search space of NNs using
another source of knowledge so that NNs are far from the query while still
being semantically related. We show that our method (1) outperforms MSF in SSL
setting when the constraint utilizes a different augmentation of an image from
the previous epoch, and (2) outperforms PAWS in semi-supervised setting with
less training resources when the constraint ensures that the NNs have the same
pseudo-label as the query.