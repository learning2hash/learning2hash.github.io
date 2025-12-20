---
layout: publication
title: Weakly-supervised Scientific Document Classification Via Retrieval-augmented
  Multi-stage Training
authors: Ran Xu, Yue Yu, Joyce C. Ho, Carl Yang
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: xu2023weakly
citations: 12
additional_links: [{name: Code, url: 'https://github.com/ritaranx/wander'}, {name: Paper,
    url: 'https://arxiv.org/abs/2306.07193'}]
tags: ["Datasets", "SIGIR", "Supervised"]
short_authors: Xu et al.
---
Scientific document classification is a critical task for a wide range of
applications, but the cost of obtaining massive amounts of human-labeled data
can be prohibitive. To address this challenge, we propose a weakly-supervised
approach for scientific document classification using label names only. In
scientific domains, label names often include domain-specific concepts that may
not appear in the document corpus, making it difficult to match labels and
documents precisely. To tackle this issue, we propose WANDER, which leverages
dense retrieval to perform matching in the embedding space to capture the
semantics of label names. We further design the label name expansion module to
enrich the label name representations. Lastly, a self-training step is used to
refine the predictions. The experiments on three datasets show that WANDER
outperforms the best baseline by 11.9% on average. Our code will be published
at https://github.com/ritaranx/wander.