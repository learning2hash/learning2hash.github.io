---
layout: publication
title: Multi-queue Momentum Contrast For Microvideo-product Retrieval
authors: Yali Du, Yinwei Wei, Wei Ji, Fan Liu, Xin Luo, Liqiang Nie
conference: Proceedings of the Sixteenth ACM International Conference on Web Search
  and Data Mining
year: 2022
bibkey: du2022multi
citations: 16
additional_links: [{name: Code, url: 'https://github.com/duyali2000/MQMC'}, {name: Paper,
    url: 'https://arxiv.org/abs/2212.11471'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Du et al.
---
The booming development and huge market of micro-videos bring new e-commerce
channels for merchants. Currently, more micro-video publishers prefer to embed
relevant ads into their micro-videos, which not only provides them with
business income but helps the audiences to discover their interesting products.
However, due to the micro-video recording by unprofessional equipment,
involving various topics and including multiple modalities, it is challenging
to locate the products related to micro-videos efficiently, appropriately, and
accurately. We formulate the microvideo-product retrieval task, which is the
first attempt to explore the retrieval between the multi-modal and multi-modal
instances.
  A novel approach named Multi-Queue Momentum Contrast (MQMC) network is
proposed for bidirectional retrieval, consisting of the uni-modal feature and
multi-modal instance representation learning. Moreover, a discriminative
selection strategy with a multi-queue is used to distinguish the importance of
different negatives based on their categories. We collect two large-scale
microvideo-product datasets (MVS and MVS-large) for evaluation and manually
construct the hierarchical category ontology, which covers sundry products in
daily life. Extensive experiments show that MQMC outperforms the
state-of-the-art baselines. Our replication package (including code, dataset,
etc.) is publicly available at https://github.com/duyali2000/MQMC.