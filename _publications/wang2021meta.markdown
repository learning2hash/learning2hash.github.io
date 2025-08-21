---
layout: publication
title: Meta Cross-modal Hashing On Long-tailed Data
authors: Runmin Wang, Guoxian Yu, Carlotta Domeniconi, Xiangliang Zhang
conference: Arxiv
year: 2021
bibkey: wang2021meta
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2111.04086'}]
tags: ["Datasets", "Efficiency", "Hashing Methods"]
short_authors: Wang et al.
---
Due to the advantage of reducing storage while speeding up query time on big
heterogeneous data, cross-modal hashing has been extensively studied for
approximate nearest neighbor search of multi-modal data. Most hashing methods
assume that training data is class-balanced.However, in practice, real world
data often have a long-tailed distribution. In this paper, we introduce a
meta-learning based cross-modal hashing method (MetaCMH) to handle long-tailed
data. Due to the lack of training samples in the tail classes, MetaCMH first
learns direct features from data in different modalities, and then introduces
an associative memory module to learn the memory features of samples of the
tail classes. It then combines the direct and memory features to obtain meta
features for each sample. For samples of the head classes of the long tail
distribution, the weight of the direct features is larger, because there are
enough training data to learn them well; while for rare classes, the weight of
the memory features is larger. Finally, MetaCMH uses a likelihood loss function
to preserve the similarity in different modalities and learns hash functions in
an end-to-end fashion. Experiments on long-tailed datasets show that MetaCMH
performs significantly better than state-of-the-art methods, especially on the
tail classes.