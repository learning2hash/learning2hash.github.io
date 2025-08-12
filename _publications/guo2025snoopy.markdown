---
layout: publication
title: 'Snoopy: Effective And Efficient Semantic Join Discovery Via Proxy Columns'
authors: Yuxiang Guo, Yuren Mao, Zhonghao Hu, Lu Chen, Yunjun Gao
conference: IEEE Transactions on Knowledge and Data Engineering
year: 2025
bibkey: guo2025snoopy
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2502.16813'}]
tags: ["Efficiency"]
short_authors: Guo et al.
---
Semantic join discovery, which aims to find columns in a table repository
with high semantic joinabilities to a query column, is crucial for dataset
discovery. Existing methods can be divided into two categories: cell-level
methods and column-level methods. However, neither of them ensures both
effectiveness and efficiency simultaneously. Cell-level methods, which compute
the joinability by counting cell matches between columns, enjoy ideal
effectiveness but suffer poor efficiency. In contrast, column-level methods,
which determine joinability only by computing the similarity of column
embeddings, enjoy proper efficiency but suffer poor effectiveness due to the
issues occurring in their column embeddings: (i) semantics-joinability-gap,
(ii) size limit, and (iii) permutation sensitivity. To address these issues,
this paper proposes to compute column embeddings via proxy columns;
furthermore, a novel column-level semantic join discovery framework, Snoopy, is
presented, leveraging proxy-column-based embeddings to bridge effectiveness and
efficiency. Specifically, the proposed column embeddings are derived from the
implicit column-to-proxy-column relationships, which are captured by the
lightweight approximate-graph-matching-based column projection.To acquire good
proxy columns for guiding the column projection, we introduce a rank-aware
contrastive learning paradigm. Extensive experiments on four real-world
datasets demonstrate that Snoopy outperforms SOTA column-level methods by 16%
in Recall@25 and 10% in NDCG@25, and achieves superior efficiency--being at
least 5 orders of magnitude faster than cell-level solutions, and 3.5x faster
than existing column-level methods.