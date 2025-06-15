---
layout: publication
title: 'User-curated Image Collections: Modeling And Recommendation'
authors: Yuncheng Li, Yang Cong, Tao Mei, Jiebo Luo
conference: "Arxiv"
year: 2015
citations: 7
bibkey: li2015user
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1509.05671'}
tags: ['RecSys', 'Tools and Libraries', 'Applications']
---
Most state-of-the-art image retrieval and recommendation systems
predominantly focus on individual images. In contrast, socially curated image
collections, condensing distinctive yet coherent images into one set, are
largely overlooked by the research communities. In this paper, we aim to design
a novel recommendation system that can provide users with image collections
relevant to individual personal preferences and interests. To this end, two key
issues need to be addressed, i.e., image collection modeling and similarity
measurement. For image collection modeling, we consider each image collection
as a whole in a group sparse reconstruction framework and extract concise
collection descriptors given the pretrained dictionaries. We then consider
image collection recommendation as a dynamic similarity measurement problem in
response to user's clicked image set, and employ a metric learner to measure
the similarity between the image collection and the clicked image set. As there
is no previous work directly comparable to this study, we implement several
competitive baselines and related methods for comparison. The evaluations on a
large scale Pinterest data set have validated the effectiveness of our proposed
methods for modeling and recommending image collections.
