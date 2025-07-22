---
layout: publication
title: Text and Code Embeddings by Contrastive Pre-Training
authors: Neelakantan Arvind, Xu Tao, Puri Raul, Radford Alec, Han Jesse Michael, Tworek
  Jerry, Yuan Qiming, Tezak Nikolas, Kim Jong Wook, Hallacy Chris, Heidecke Johannes,
  Shyam Pranav, Power Boris, Nekoul Tyna Eloundou, Sastry Girish, Krueger Gretchen,
  Schnurr David, Such Felipe Petroski, Hsu Kenny, Thompson Madeleine, Khan Tabarak,
  Sherbakov Toki, Jang Joanne, Welinder Peter, Weng Lilian
conference: Arxiv
year: 2022
bibkey: neelakantan2022text
citations: 110
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2201.10005'}]
tags: ["Unsupervised", "Scalability", "Supervised", "Datasets"]
short_authors: Neelakantan et al.
---
Text embeddings are useful features in many applications such as semantic
search and computing text similarity. Previous work typically trains models
customized for different use cases, varying in dataset choice, training
objective and model architecture. In this work, we show that contrastive
pre-training on unsupervised data at scale leads to high quality vector
representations of text and code. The same unsupervised text embeddings that
achieve new state-of-the-art results in linear-probe classification also
display impressive semantic search capabilities and sometimes even perform
competitively with fine-tuned models. On linear-probe classification accuracy
averaging over 7 tasks, our best unsupervised model achieves a relative
improvement of 4% and 1.8% over previous best unsupervised and supervised text
embedding models respectively. The same text embeddings when evaluated on
large-scale semantic search attains a relative improvement of 23.4%, 14.7%, and
10.6% over previous best unsupervised methods on MSMARCO, Natural Questions and
TriviaQA benchmarks, respectively. Similarly to text embeddings, we train code
embedding models on (text, code) pairs, obtaining a 20.8% relative improvement
over prior best work on code search.