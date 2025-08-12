---
layout: publication
title: Towards Micro-video Thumbnail Selection Via A Multi-label Visual-semantic Embedding
  Model
authors: Liu Bo
conference: Arxiv
year: 2022
bibkey: bo2022towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.02930'}]
tags: ["Datasets"]
short_authors: Liu Bo
---
The thumbnail, as the first sight of a micro-video, plays a pivotal role in
attracting users to click and watch. While in the real scenario, the more the
thumbnails satisfy the users, the more likely the micro-videos will be clicked.
In this paper, we aim to select the thumbnail of a given micro-video that meets
most users` interests. Towards this end, we present a multi-label
visual-semantic embedding model to estimate the similarity between the pair of
each frame and the popular topics that users are interested in. In this model,
the visual and textual information is embedded into a shared semantic space,
whereby the similarity can be measured directly, even the unseen words.
Moreover, to compare the frame to all words from the popular topics, we devise
an attention embedding space associated with the semantic-attention projection.
With the help of these two embedding spaces, the popularity score of a frame,
which is defined by the sum of similarity scores over the corresponding visual
information and popular topic pairs, is achieved. Ultimately, we fuse the
visual representation score and the popularity score of each frame to select
the attractive thumbnail for the given micro-video. Extensive experiments
conducted on a real-world dataset have well-verified that our model
significantly outperforms several state-of-the-art baselines.