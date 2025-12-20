---
layout: publication
title: When Should Dense Retrievers Be Updated In Evolving Corpora? Detecting Out-of-distribution
  Corpora Using Gradnormir
authors: Dayoon Ko, Jinyoung Kim, Sohyeon Kim, Jinhyuk Kim, Jaehoon Lee, Seonghak
  Song, Minyoung Lee, Gunhee Kim
conference: 'Findings of the Association for Computational Linguistics: ACL 2025'
year: 2025
bibkey: ko2025when
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.01877'}]
tags: ["Efficiency", "Evaluation", "Robustness", "Supervised", "Unsupervised"]
short_authors: Ko et al.
---
Dense retrievers encode texts into embeddings to efficiently retrieve relevant documents from large databases in response to user queries. However, real-world corpora continually evolve, leading to a shift from the original training distribution of the retriever. Without timely updates or retraining, indexing newly emerging documents can degrade retrieval performance for future queries. Thus, identifying when a dense retriever requires an update is critical for maintaining robust retrieval systems. In this paper, we propose a novel task of predicting whether a corpus is out-of-distribution (OOD) relative to a dense retriever before indexing. Addressing this task allows us to proactively manage retriever updates, preventing potential retrieval failures. We introduce GradNormIR, an unsupervised approach that leverages gradient norms to detect OOD corpora effectively. Experiments on the BEIR benchmark demonstrate that GradNormIR enables timely updates of dense retrievers in evolving document collections, significantly enhancing retrieval robustness and efficiency.