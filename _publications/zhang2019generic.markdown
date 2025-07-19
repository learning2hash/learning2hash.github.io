---
layout: publication
title: Generic Intent Representation in Web Search
authors: Zhang et al.
conference: Proceedings of the 42nd International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2019
bibkey: zhang2019generic
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.10710'}]
tags: [SIGIR]
---
This paper presents GEneric iNtent Encoder (GEN Encoder) which learns a
distributed representation space for user intent in search. Leveraging large
scale user clicks from Bing search logs as weak supervision of user intent, GEN
Encoder learns to map queries with shared clicks into similar embeddings
end-to-end and then finetunes on multiple paraphrase tasks. Experimental
results on an intrinsic evaluation task - query intent similarity modeling -
demonstrate GEN Encoder's robust and significant advantages over previous
representation methods. Ablation studies reveal the crucial role of learning
from implicit user feedback in representing user intent and the contributions
of multi-task learning in representation generality. We also demonstrate that
GEN Encoder alleviates the sparsity of tail search traffic and cuts down half
of the unseen queries by using an efficient approximate nearest neighbor search
to effectively identify previous queries with the same search intent. Finally,
we demonstrate distances between GEN encodings reflect certain information
seeking behaviors in search sessions.