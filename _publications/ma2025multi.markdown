---
layout: publication
title: Multi-modal Reference Learning For Fine-grained Text-to-image Retrieval
authors: Ma Zehong, Chen Hao, Zeng Wei, Su Limin, Zhang Shiliang
conference: IEEE Transactions on Multimedia
year: 2025
bibkey: ma2025multi
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.07718'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Ma et al.
---
Fine-grained text-to-image retrieval aims to retrieve a fine-grained target
image with a given text query. Existing methods typically assume that each
training image is accurately depicted by its textual descriptions. However,
textual descriptions can be ambiguous and fail to depict discriminative visual
details in images, leading to inaccurate representation learning. To alleviate
the effects of text ambiguity, we propose a Multi-Modal Reference learning
framework to learn robust representations. We first propose a multi-modal
reference construction module to aggregate all visual and textual details of
the same object into a comprehensive multi-modal reference. The multi-modal
reference hence facilitates the subsequent representation learning and
retrieval similarity computation. Specifically, a reference-guided
representation learning module is proposed to use multi-modal references to
learn more accurate visual and textual representations. Additionally, we
introduce a reference-based refinement method that employs the object
references to compute a reference-based similarity that refines the initial
retrieval results. Extensive experiments are conducted on five fine-grained
text-to-image retrieval datasets for different text-to-image retrieval tasks.
The proposed method has achieved superior performance over state-of-the-art
methods. For instance, on the text-to-person image retrieval dataset RSTPReid,
our method achieves the Rank1 accuracy of 56.2%, surpassing the recent CFine
by 5.6%.