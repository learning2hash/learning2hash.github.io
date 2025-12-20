---
layout: publication
title: 'Decoding Dense Embeddings: Sparse Autoencoders For Interpreting And Discretizing
  Dense Retrieval'
authors: Seongwan Park, Taeklim Kim, Youngjoong Ko
conference: Arxiv
year: 2025
bibkey: park2025decoding
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.00041'}]
tags: ["Efficiency", "Evaluation", "Tools & Libraries"]
short_authors: Seongwan Park, Taeklim Kim, Youngjoong Ko
---
Despite their strong performance, Dense Passage Retrieval (DPR) models suffer from a lack of interpretability. In this work, we propose a novel interpretability framework that leverages Sparse Autoencoders (SAEs) to decompose previously uninterpretable dense embeddings from DPR models into distinct, interpretable latent concepts. We generate natural language descriptions for each latent concept, enabling human interpretations of both the dense embeddings and the query-document similarity scores of DPR models. We further introduce Concept-Level Sparse Retrieval (CL-SR), a retrieval framework that directly utilizes the extracted latent concepts as indexing units. CL-SR effectively combines the semantic expressiveness of dense embeddings with the transparency and efficiency of sparse representations. We show that CL-SR achieves high index-space and computational efficiency while maintaining robust performance across vocabulary and semantic mismatches.