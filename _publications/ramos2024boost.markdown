---
layout: publication
title: "BlockBoost: Scalable and Efficient Blocking through Boosting"
authors: Thiago Ramos, Rodrigo Loro Schuller, Alex Akira Okuno, Lucas Nissenbaum, Roberto I Oliveira, Paulo Orenstein
conference: AISTATS
year: 2024
bibkey: ramos2024boost
additional_links:
   - {name: "PDF", url: "https://proceedings.mlr.press/v238/ramos24a/ramos24a.pdf"}
   - {name: "Code", url: "https://github.com/thiagorr162/blockboost"}
tags: ["AISTATS]
---
As datasets grow larger, matching and merging entries from different databases has become a costly task in modern data pipelines. To avoid expensive comparisons between entries, blocking similar items is a popular preprocessing step. In this paper, we introduce BlockBoost, a novel boosting-based method that generates compact binary hash codes for database entries, through which blocking can be performed efficiently. The algorithm is fast and scalable, resulting in computational costs that are orders of magnitude lower than current benchmarks. Unlike existing alternatives, BlockBoost comes with associated feature importance measures for interpretability, and possesses strong theoretical guarantees, including lower bounds on critical performance metrics like recall and reduction ratio. Finally, we show that BlockBoost delivers great empirical results, outperforming state-of-the-art blocking benchmarks in terms of both performance metrics and computational cost.
