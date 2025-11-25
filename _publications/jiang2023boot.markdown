---
layout: publication
title: 'Boot And Switch: Alternating Distillation For Zero-shot Dense Retrieval'
authors: Fan Jiang, Qiongkai Xu, Tom Drummond, Trevor Cohn
conference: 'Findings of the Association for Computational Linguistics: EMNLP 2023'
year: 2023
bibkey: jiang2023boot
citations: 0
additional_links: [{name: Code, url: 'https://github.com/Fantabulous-J/BootSwitch.\'},
  {name: Paper, url: 'https://arxiv.org/abs/2311.15564'}]
tags: ["EMNLP", "Few Shot & Zero Shot", "Re-Ranking", "Unsupervised"]
short_authors: Jiang et al.
---
Neural 'dense' retrieval models are state of the art for many datasets,
however these models often exhibit limited domain transfer ability. Existing
approaches to adaptation are unwieldy, such as requiring explicit supervision,
complex model architectures, or massive external models. We present
\(\texttt\{ABEL\}\), a simple but effective unsupervised method to enhance passage
retrieval in zero-shot settings. Our technique follows a straightforward loop:
a dense retriever learns from supervision signals provided by a reranker, and
subsequently, the reranker is updated based on feedback from the improved
retriever. By iterating this loop, the two components mutually enhance one
another's performance. Experimental results demonstrate that our unsupervised
\(\texttt\{ABEL\}\) model outperforms both leading supervised and unsupervised
retrievers on the BEIR benchmark. Meanwhile, it exhibits strong adaptation
abilities to tasks and domains that were unseen during training. By either
fine-tuning \(\texttt\{ABEL\}\) on labelled data or integrating it with existing
supervised dense retrievers, we achieve state-of-the-art
results.\footnote\{Source code is available at
https://github.com/Fantabulous-J/BootSwitch.\}