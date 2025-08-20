---
layout: publication
title: Lexically-accelerated Dense Retrieval
authors: Hrishikesh Kulkarni, Sean MacAvaney, Nazli Goharian, Ophir Frieder
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: kulkarni2023lexically
citations: 19
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.16779'}]
tags: [SIGIR, Efficiency, Evaluation, Graph-based ANN]
short_authors: Kulkarni et al.
---
Retrieval approaches that score documents based on learned dense vectors
(i.e., dense retrieval) rather than lexical signals (i.e., conventional
retrieval) are increasingly popular. Their ability to identify related
documents that do not necessarily contain the same terms as those appearing in
the user's query (thereby improving recall) is one of their key advantages.
However, to actually achieve these gains, dense retrieval approaches typically
require an exhaustive search over the document collection, making them
considerably more expensive at query-time than conventional lexical approaches.
Several techniques aim to reduce this computational overhead by approximating
the results of a full dense retriever. Although these approaches reasonably
approximate the top results, they suffer in terms of recall -- one of the key
advantages of dense retrieval. We introduce 'LADR' (Lexically-Accelerated Dense
Retrieval), a simple-yet-effective approach that improves the efficiency of
existing dense retrieval models without compromising on retrieval
effectiveness. LADR uses lexical retrieval techniques to seed a dense retrieval
exploration that uses a document proximity graph. We explore two variants of
LADR: a proactive approach that expands the search space to the neighbors of
all seed documents, and an adaptive approach that selectively searches the
documents with the highest estimated relevance in an iterative fashion. Through
extensive experiments across a variety of dense retrieval models, we find that
LADR establishes a new dense retrieval effectiveness-efficiency Pareto frontier
among approximate k nearest neighbor techniques. Further, we find that when
tuned to take around 8ms per query in retrieval latency on our hardware, LADR
consistently achieves both precision and recall that are on par with an
exhaustive search on standard benchmarks.