---
layout: publication
title: Self-supervised Ranking For Representation Learning
authors: Ali Varamesh, Ali Diba, Tinne Tuytelaars, Luc van Gool
conference: Arxiv
year: 2020
bibkey: varamesh2020self
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2010.07258'}]
tags: ["Image Retrieval", "Self-Supervised"]
short_authors: Varamesh et al.
---
We present a new framework for self-supervised representation learning by
formulating it as a ranking problem in an image retrieval context on a large
number of random views (augmentations) obtained from images. Our work is based
on two intuitions: first, a good representation of images must yield a
high-quality image ranking in a retrieval task; second, we would expect random
views of an image to be ranked closer to a reference view of that image than
random views of other images. Hence, we model representation learning as a
learning to rank problem for image retrieval. We train a representation encoder
by maximizing average precision (AP) for ranking, where random views of an
image are considered positively related, and that of the other images
considered negatives. The new framework, dubbed S2R2, enables computing a
global objective on multiple views, compared to the local objective in the
popular contrastive learning framework, which is calculated on pairs of views.
In principle, by using a ranking criterion, we eliminate reliance on
object-centric curated datasets. When trained on STL10 and MS-COCO, S2R2
outperforms SimCLR and the clustering-based contrastive learning model, SwAV,
while being much simpler both conceptually and at implementation. On MS-COCO,
S2R2 outperforms both SwAV and SimCLR with a larger margin than on STl10. This
indicates that S2R2 is more effective on diverse scenes and could eliminate the
need for an object-centric large training dataset for self-supervised
representation learning.