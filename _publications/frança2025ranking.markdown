---
layout: publication
title: Ranking-based Fusion Algorithms For Extreme Multi-label Text Classification
  (XMTC)
authors: "Celso Fran\xE7a, Gestefane Rabbi, Thiago Salles, Washington Cunha, Leonardo\
  \ Rocha, Marcos Andr\xE9 Gon\xE7alves"
conference: Arxiv
year: 2025
bibkey: "fran\xE7a2025ranking"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2507.03761'}]
tags: [Uncategorized]
short_authors: "Fran\xE7a et al."
---
In the context of Extreme Multi-label Text Classification (XMTC), where labels are assigned to text instances from a large label space, the long-tail distribution of labels presents a significant challenge. Labels can be broadly categorized into frequent, high-coverage \textbf\{head labels\} and infrequent, low-coverage \textbf\{tail labels\}, complicating the task of balancing effectiveness across all labels. To address this, combining predictions from multiple retrieval methods, such as sparse retrievers (e.g., BM25) and dense retrievers (e.g., fine-tuned BERT), offers a promising solution. The fusion of \textit\{sparse\} and \textit\{dense\} retrievers is motivated by the complementary ranking characteristics of these methods. Sparse retrievers compute relevance scores based on high-dimensional, bag-of-words representations, while dense retrievers utilize approximate nearest neighbor (ANN) algorithms on dense text and label embeddings within a shared embedding space. Rank-based fusion algorithms leverage these differences by combining the precise matching capabilities of sparse retrievers with the semantic richness of dense retrievers, thereby producing a final ranking that improves the effectiveness across both head and tail labels.