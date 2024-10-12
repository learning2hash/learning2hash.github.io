---
layout: publication
title: Beyond Pairwise Provably Fast Algorithms For Approximate k-way Similarity Search
authors: Anshumali Shrivastava, Ping Li
conference: "Neural Information Processing Systems"
year: 2013
bibkey: shrivastava2013beyond
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2013/hash/f1b6f2857fb6d44dd73c7041e0aa0f19-Abstract.html"}
tags: ['Independent', 'LSH', 'NEURIPS']
---
We go beyond the notion of pairwise similarity and look into search problems with \\(k\\)-way similarity functions. In this paper, we focus on problems related to \emph{3-way Jaccard} similarity: \\(\mathcal&#123;R&#125;^&#123;3way&#125;= \frac&#123;|S_1 \cap S_2 \cap S_3|&#125;&#123;|S_1 \cup S_2 \cup S_3|&#125;\\), \\(S_1, S_2, S_3 \in \mathcal&#123;C&#125;\\), where \\(\mathcal&#123;C&#125;\\) is a size \\(n\\) collection of sets (or binary vectors). We show that approximate \\(\mathcal&#123;R&#125;^&#123;3way&#125;\\) similarity search problems admit fast algorithms with provable guarantees, analogous to the pairwise case. Our analysis and speedup guarantees naturally extend to \\(k\\)-way resemblance. In the process, we extend traditional framework of \emph{locality sensitive hashing (LSH)} to handle higher order similarities, which could be of independent theoretical interest. The applicability of \\(\mathcal&#123;R&#125;^&#123;3way&#125;\\) search is shown on the Google sets application. In addition, we demonstrate the advantage of \\(\mathcal&#123;R&#125;^&#123;3way&#125;\\) resemblance over the pairwise case in improving retrieval quality.
