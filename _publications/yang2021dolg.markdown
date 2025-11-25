---
layout: publication
title: 'DOLG: Single-stage Image Retrieval With Deep Orthogonal Fusion Of Local And
  Global Features'
authors: Min Yang, Dongliang He, Miao Fan, Baorong Shi, Xuetong Xue, Fu Li, Errui
  Ding, Jizhou Huang
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: yang2021dolg
citations: 125
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.02927'}]
tags: ["ICCV", "Image Retrieval", "Similarity Search"]
short_authors: Yang et al.
---
Image Retrieval is a fundamental task of obtaining images similar to the
query one from a database. A common image retrieval practice is to firstly
retrieve candidate images via similarity search using global image features and
then re-rank the candidates by leveraging their local features. Previous
learning-based studies mainly focus on either global or local image
representation learning to tackle the retrieval task. In this paper, we abandon
the two-stage paradigm and seek to design an effective single-stage solution by
integrating local and global information inside images into compact image
representations. Specifically, we propose a Deep Orthogonal Local and Global
(DOLG) information fusion framework for end-to-end image retrieval. It
attentively extracts representative local information with multi-atrous
convolutions and self-attention at first. Components orthogonal to the global
image representation are then extracted from the local information. At last,
the orthogonal components are concatenated with the global representation as a
complementary, and then aggregation is performed to generate the final
representation. The whole framework is end-to-end differentiable and can be
trained with image-level labels. Extensive experimental results validate the
effectiveness of our solution and show that our model achieves state-of-the-art
image retrieval performances on Revisited Oxford and Paris datasets.