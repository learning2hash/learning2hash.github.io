---
layout: publication
title: Augmented Transformers With Adaptive N-grams Embedding For Multilingual Scene
  Text Recognition
authors: Xueming Yan, Zhihang Fang, Yaochu Jin
conference: Arxiv
year: 2023
bibkey: yan2023augmented
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.14261'}]
tags: []
short_authors: Xueming Yan, Zhihang Fang, Yaochu Jin
---
While vision transformers have been highly successful in improving the
performance in image-based tasks, not much work has been reported on applying
transformers to multilingual scene text recognition due to the complexities in
the visual appearance of multilingual texts. To fill the gap, this paper
proposes an augmented transformer architecture with n-grams embedding and
cross-language rectification (TANGER). TANGER consists of a primary transformer
with single patch embeddings of visual images, and a supplementary transformer
with adaptive n-grams embeddings that aims to flexibly explore the potential
correlations between neighbouring visual patches, which is essential for
feature extraction from multilingual scene texts. Cross-language rectification
is achieved with a loss function that takes into account both language
identification and contextual coherence scoring. Extensive comparative studies
are conducted on four widely used benchmark datasets as well as a new
multilingual scene text dataset containing Indonesian, English, and Chinese
collected from tourism scenes in Indonesia. Our experimental results
demonstrate that TANGER is considerably better compared to the
state-of-the-art, especially in handling complex multilingual scene texts.