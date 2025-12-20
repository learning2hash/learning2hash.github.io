---
layout: publication
title: Emotion Embedding Spaces For Matching Music To Stories
authors: Minz Won, Justin Salamon, Nicholas J. Bryan, Gautham J. Mysore, Xavier Serra
conference: Arxiv
year: 2021
bibkey: won2021emotion
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.13468'}]
tags: ["Datasets", "Distance Metric Learning", "Multimodal Retrieval"]
short_authors: Won et al.
---
Content creators often use music to enhance their stories, as it can be a
powerful tool to convey emotion. In this paper, our goal is to help creators
find music to match the emotion of their story. We focus on text-based stories
that can be auralized (e.g., books), use multiple sentences as input queries,
and automatically retrieve matching music. We formalize this task as a
cross-modal text-to-music retrieval problem. Both the music and text domains
have existing datasets with emotion labels, but mismatched emotion vocabularies
prevent us from using mood or emotion annotations directly for matching. To
address this challenge, we propose and investigate several emotion embedding
spaces, both manually defined (e.g., valence/arousal) and data-driven (e.g.,
Word2Vec and metric learning) to bridge this gap. Our experiments show that by
leveraging these embedding spaces, we are able to successfully bridge the gap
between modalities to facilitate cross modal retrieval. We show that our method
can leverage the well established valence-arousal space, but that it can also
achieve our goal via data-driven embedding spaces. By leveraging data-driven
embeddings, our approach has the potential of being generalized to other
retrieval tasks that require broader or completely different vocabularies.