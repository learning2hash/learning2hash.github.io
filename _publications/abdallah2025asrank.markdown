---
layout: publication
title: 'Asrank: Zero-shot Re-ranking With Answer Scent For Document Retrieval'
authors: Abdelrahman Abdallah, Jamshid Mozafari, Bhawna Piryani, Adam Jatowt
conference: 'Findings of the Association for Computational Linguistics: NAACL 2025'
year: 2025
bibkey: abdallah2025asrank
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.15245'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot", "Hybrid ANN Methods", "NAACL", "Re-Ranking", "Text Retrieval"]
short_authors: Abdallah et al.
---
Retrieval-Augmented Generation (RAG) models have drawn considerable attention
in modern open-domain question answering. The effectiveness of RAG depends on
the quality of the top retrieved documents. However, conventional retrieval
methods sometimes fail to rank the most relevant documents at the top. In this
paper, we introduce ASRank, a new re-ranking method based on scoring retrieved
documents using zero-shot answer scent which relies on a pre-trained large
language model to compute the likelihood of the document-derived answers
aligning with the answer scent. Our approach demonstrates marked improvements
across several datasets, including NQ, TriviaQA, WebQA, ArchivalQA, HotpotQA,
and Entity Questions. Notably, ASRank increases Top-1 retrieval accuracy on NQ
from \(19.2%\) to \(46.5%\) for MSS and \(22.1%\) to \(47.3%\) for BM25. It also
shows strong retrieval performance on several datasets compared to
state-of-the-art methods (47.3 Top-1 by ASRank vs 35.4 by UPR by BM25).