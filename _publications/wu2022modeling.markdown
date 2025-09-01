---
layout: publication
title: Modeling Fine-grained Information Via Knowledge-aware Hierarchical Graph For
  Zero-shot Entity Retrieval
authors: Taiqiang Wu, Xingyu Bai, Weigang Guo, Weijie Liu, Siheng Li, Yujiu Yang
conference: Proceedings of the Sixteenth ACM International Conference on Web Search
  and Data Mining
year: 2023
bibkey: wu2022modeling
citations: 9
additional_links: [{name: Code, url: 'https://github.com/wutaiqiang/GER-WSDM2023.'},
  {name: Paper, url: 'https://arxiv.org/abs/2211.10991'}]
tags: ["Few Shot & Zero Shot", "Tools & Libraries"]
short_authors: Wu et al.
---
Zero-shot entity retrieval, aiming to link mentions to candidate entities
under the zero-shot setting, is vital for many tasks in Natural Language
Processing. Most existing methods represent mentions/entities via the sentence
embeddings of corresponding context from the Pre-trained Language Model.
However, we argue that such coarse-grained sentence embeddings can not fully
model the mentions/entities, especially when the attention scores towards
mentions/entities are relatively low. In this work, we propose GER, a
\textbf\{G\}raph enhanced \textbf\{E\}ntity \textbf\{R\}etrieval framework, to
capture more fine-grained information as complementary to sentence embeddings.
We extract the knowledge units from the corresponding context and then
construct a mention/entity centralized graph. Hence, we can learn the
fine-grained information about mention/entity by aggregating information from
these knowledge units. To avoid the graph information bottleneck for the
central mention/entity node, we construct a hierarchical graph and design a
novel Hierarchical Graph Attention Network~(HGAN). Experimental results on
popular benchmarks demonstrate that our proposed GER framework performs better
than previous state-of-the-art models. The code has been available at
https://github.com/wutaiqiang/GER-WSDM2023.