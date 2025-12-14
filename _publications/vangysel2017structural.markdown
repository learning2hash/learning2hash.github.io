---
layout: publication
title: Structural Regularities In Text-based Entity Vector Spaces
authors: Christophe van Gysel, Maarten de Rijke, Evangelos Kanoulas
conference: Proceedings of the ACM SIGIR International Conference on Theory of Information
  Retrieval
year: 2017
bibkey: vangysel2017structural
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.07930'}]
tags: [Supervised, Unsupervised, SIGIR]
short_authors: Christophe van Gysel, Maarten de Rijke, Evangelos Kanoulas
---
Entity retrieval is the task of finding entities such as people or products
in response to a query, based solely on the textual documents they are
associated with. Recent semantic entity retrieval algorithms represent queries
and experts in finite-dimensional vector spaces, where both are constructed
from text sequences.
  We investigate entity vector spaces and the degree to which they capture
structural regularities. Such vector spaces are constructed in an unsupervised
manner without explicit information about structural aspects. For concreteness,
we address these questions for a specific type of entity: experts in the
context of expert finding. We discover how clusterings of experts correspond to
committees in organizations, the ability of expert representations to encode
the co-author graph, and the degree to which they encode academic rank. We
compare latent, continuous representations created using methods based on
distributional semantics (LSI), topic models (LDA) and neural networks
(word2vec, doc2vec, SERT). Vector spaces created using neural methods, such as
doc2vec and SERT, systematically perform better at clustering than LSI, LDA and
word2vec. When it comes to encoding entity relations, SERT performs best.