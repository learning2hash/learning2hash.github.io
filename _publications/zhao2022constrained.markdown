---
layout: publication
title: Constrained Approximate Similarity Search On Proximity Graph
authors: Weijie Zhao, Shulong Tan, Ping Li
conference: Arxiv
year: 2022
bibkey: zhao2022constrained
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2210.14958'}]
tags: ["Evaluation", "Graph Based ANN", "Quantization", "Recommender Systems", "Similarity Search"]
short_authors: Weijie Zhao, Shulong Tan, Ping Li
---
Search engines and recommendation systems are built to efficiently display
relevant information from those massive amounts of candidates. Typically a
three-stage mechanism is employed in those systems: (i) a small collection of
items are first retrieved by (e.g.,) approximate near neighbor search
algorithms; (ii) then a collection of constraints are applied on the retrieved
items; (iii) a fine-grained ranking neural network is employed to determine the
final recommendation. We observe a major defect of the original three-stage
pipeline: Although we only target to retrieve \(k\) vectors in the final
recommendation, we have to preset a sufficiently large \(s\) (\(s > k\)) for each
query, and ``hope'' the number of survived vectors after the filtering is not
smaller than \(k\). That is, at least \(k\) vectors in the \(s\) similar candidates
satisfy the query constraints.
  In this paper, we investigate this constrained similarity search problem and
attempt to merge the similarity search stage and the filtering stage into one
single search operation. We introduce AIRSHIP, a system that integrates a
user-defined function filtering into the similarity search framework. The
proposed system does not need to build extra indices nor require prior
knowledge of the query constraints. We propose three optimization strategies:
(1) starting point selection, (2) multi-direction search, and (3) biased
priority queue selection. Experimental evaluations on both synthetic and real
data confirm the effectiveness of the proposed AIRSHIP algorithm. We focus on
constrained graph-based approximate near neighbor (ANN) search in this study,
in part because graph-based ANN is known to achieve excellent performance. We
believe it is also possible to develop constrained hashing-based ANN or
constrained quantization-based ANN.