---
layout: publication
title: Continual Learning In Cross-modal Retrieval
authors: Kai Wang, Luis Herranz, Joost van de Weijer
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2021
bibkey: wang2021continual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.06806'}]
tags: ["CVPR", "Multimodal Retrieval"]
short_authors: Kai Wang, Luis Herranz, Joost van de Weijer
---
Multimodal representations and continual learning are two areas closely
related to human intelligence. The former considers the learning of shared
representation spaces where information from different modalities can be
compared and integrated (we focus on cross-modal retrieval between language and
visual representations). The latter studies how to prevent forgetting a
previously learned task when learning a new one. While humans excel in these
two aspects, deep neural networks are still quite limited. In this paper, we
propose a combination of both problems into a continual cross-modal retrieval
setting, where we study how the catastrophic interference caused by new tasks
impacts the embedding spaces and their cross-modal alignment required for
effective retrieval. We propose a general framework that decouples the
training, indexing and querying stages. We also identify and study different
factors that may lead to forgetting, and propose tools to alleviate it. We
found that the indexing stage pays an important role and that simply avoiding
reindexing the database with updated embedding networks can lead to significant
gains. We evaluated our methods in two image-text retrieval datasets, obtaining
significant gains with respect to the fine tuning baseline.