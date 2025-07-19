---
layout: publication
title: 'Moving Towards Centers: Re-ranking With Attention And Memory For Re-identification'
authors: Zhou Yunhao, Wang Yi, Chau Lap-pui
conference: IEEE Transactions on Multimedia
year: 2022
bibkey: zhou2022moving
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.01447'}]
tags: [Hybrid ANN Methods, Re RANKING]
---
Re-ranking utilizes contextual information to optimize the initial ranking
list of person or vehicle re-identification (re-ID), which boosts the retrieval
performance at post-processing steps. This paper proposes a re-ranking network
to predict the correlations between the probe and top-ranked neighbor samples.
Specifically, all the feature embeddings of query and gallery images are
expanded and enhanced by a linear combination of their neighbors, with the
correlation prediction serving as discriminative combination weights. The
combination process is equivalent to moving independent embeddings toward the
identity centers, improving cluster compactness. For correlation prediction, we
first aggregate the contextual information for probe's k-nearest neighbors via
the Transformer encoder. Then, we distill and refine the probe-related features
into the Contextual Memory cell via attention mechanism. Like humans that
retrieve images by not only considering probe images but also memorizing the
retrieved ones, the Contextual Memory produces multi-view descriptions for each
instance. Finally, the neighbors are reconstructed with features fetched from
the Contextual Memory, and a binary classifier predicts their correlations with
the probe. Experiments on six widely-used person and vehicle re-ID benchmarks
demonstrate the effectiveness of the proposed method. Especially, our method
surpasses the state-of-the-art re-ranking approaches on large-scale datasets by
a significant margin, i.e., with an average 4.83% CMC@1 and 14.83% mAP
improvements on VERI-Wild, MSMT17, and VehicleID datasets.