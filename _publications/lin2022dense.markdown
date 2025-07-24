---
layout: publication
title: A Dense Representation Framework For Lexical And Semantic Matching
authors: Sheng-chieh Lin, Jimmy Lin
conference: ACM Transactions on Information Systems
year: 2023
bibkey: lin2022dense
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.09912'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Text Retrieval", "Tools & Libraries"]
short_authors: Sheng-chieh Lin, Jimmy Lin
---
Lexical and semantic matching capture different successful approaches to text
retrieval and the fusion of their results has proven to be more effective and
robust than either alone. Prior work performs hybrid retrieval by conducting
lexical and semantic matching using different systems (e.g., Lucene and Faiss,
respectively) and then fusing their model outputs. In contrast, our work
integrates lexical representations with dense semantic representations by
densifying high-dimensional lexical representations into what we call
low-dimensional dense lexical representations (DLRs). Our experiments show that
DLRs can effectively approximate the original lexical representations,
preserving effectiveness while improving query latency. Furthermore, we can
combine dense lexical and semantic representations to generate dense hybrid
representations (DHRs) that are more flexible and yield faster retrieval
compared to existing hybrid techniques. In addition, we explore it jointly
training lexical and semantic representations in a single model and empirically
show that the resulting DHRs are able to combine the advantages of the
individual components. Our best DHR model is competitive with state-of-the-art
single-vector and multi-vector dense retrievers in both in-domain and zero-shot
evaluation settings. Furthermore, our model is both faster and requires smaller
indexes, making our dense representation framework an attractive approach to
text retrieval. Our code is available at https://github.com/castorini/dhr.