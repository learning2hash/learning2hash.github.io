---
layout: publication
title: 'Late Chunking: Contextual Chunk Embeddings Using Long-context Embedding Models'
authors: "Michael G\xFCnther, Isabelle Mohr, Daniel James Williams, Bo Wang, Han Xiao"
conference: Arxiv
year: 2024
bibkey: "g\xFCnther2024late"
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.04701'}]
tags: ["Similarity Search", "Text Retrieval", "Unsupervised"]
short_authors: "G\xFCnther et al."
---
Many use cases require retrieving smaller portions of text, and dense vector-based retrieval systems often perform better with shorter text segments, as the semantics are less likely to be over-compressed in the embeddings. Consequently, practitioners often split text documents into smaller chunks and encode them separately. However, chunk embeddings created in this way can lose contextual information from surrounding chunks, resulting in sub-optimal representations. In this paper, we introduce a novel method called late chunking, which leverages long context embedding models to first embed all tokens of the long text, with chunking applied after the transformer model and just before mean pooling - hence the term late in its naming. The resulting chunk embeddings capture the full contextual information, leading to superior results across various retrieval tasks. The method is generic enough to be applied to a wide range of long-context embedding models and works without additional training. To further increase the effectiveness of late chunking, we propose a dedicated fine-tuning approach for embedding models.