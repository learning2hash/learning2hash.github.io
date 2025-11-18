---
layout: publication
title: 'OVIS: Open-vocabulary Visual Instance Search Via Visual-semantic Aligned Representation
  Learning'
authors: Sheng Liu, Kevin Lin, Lijuan Wang, Junsong Yuan, Zicheng Liu
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2021
bibkey: liu2021ovis
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2108.03704'}]
tags: ["AAAI", "Datasets", "Evaluation"]
short_authors: Liu et al.
---
We introduce the task of open-vocabulary visual instance search (OVIS). Given
an arbitrary textual search query, Open-vocabulary Visual Instance Search
(OVIS) aims to return a ranked list of visual instances, i.e., image patches,
that satisfies the search intent from an image database. The term "open
vocabulary" means that there are neither restrictions to the visual instance to
be searched nor restrictions to the word that can be used to compose the
textual search query. We propose to address such a search challenge via
visual-semantic aligned representation learning (ViSA). ViSA leverages massive
image-caption pairs as weak image-level (not instance-level) supervision to
learn a rich cross-modal semantic space where the representations of visual
instances (not images) and those of textual queries are aligned, thus allowing
us to measure the similarities between any visual instance and an arbitrary
textual query. To evaluate the performance of ViSA, we build two datasets named
OVIS40 and OVIS1600 and also introduce a pipeline for error analysis. Through
extensive experiments on the two datasets, we demonstrate ViSA's ability to
search for visual instances in images not available during training given a
wide range of textual queries including those composed of uncommon words.
Experimental results show that ViSA achieves an mAP@50 of 21.9% on OVIS40 under
the most challenging setting and achieves an mAP@6 of 14.9% on OVIS1600
dataset.