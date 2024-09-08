---
    layout: publication
    title: "Learning to embed semantic similarity for joint image-text retrieval"
    authors: Malali Noam, Keller Yosi
    conference: Arxiv
    year: 2022
    bibkey: malali2022learning
    additional_links:
       - {name: "DOI", url: "10.1109/TPAMI.2021.3132163"}
   - {name: "License", url: "http://creativecommons.org/licenses/by/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2210.03838"}
    tags: ['Arxiv', 'Deep Learning', 'Text Retrieval', 'Quantisation']
    ---
    {% raw %}
    We present a deep learning approach for learning the joint semantic embeddings of images and captions in a Euclidean space, such that the semantic similarity is approximated by the L2 distances in the embedding space. For that, we introduce a metric learning scheme that utilizes multitask learning to learn the embedding of identical semantic concepts using a center loss. By introducing a differentiable quantization scheme into the end-to-end trainable network, we derive a semantic embedding of semantically similar concepts in Euclidean space. We also propose a novel metric learning formulation using an adaptive margin hinge loss, that is refined during the training phase. The proposed scheme was applied to the MS-COCO, Flicke30K and Flickr8K datasets, and was shown to compare favorably with contemporary state-of-the-art approaches.
    {% endraw %}