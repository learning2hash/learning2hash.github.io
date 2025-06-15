---
layout: publication
title: 'IMAGINATOR: Pre-trained Image+text Joint Embeddings Using Word-level Grounding Of Images'
authors: Varuna Krishna et al.
conference: "Arxiv"
year: 2023
citations: 0
bibkey: krishna2023pre
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2305.10438'}
  - {name: "Code", url: 'https://github.com/varunakk/IMAGINATOR'}
tags: ['Cross-Modal', 'Deep', 'Retrieval Models', 'Has Code', 'Supervised', 'Training Strategy', 'Multi-Modal Hashing', 'Applications']
---
Word embeddings, i.e., semantically meaningful vector representation of
words, are largely influenced by the distributional hypothesis "You shall know
a word by the company it keeps" (Harris, 1954), whereas modern prediction-based
neural network embeddings rely on design choices and hyperparameter
optimization. Word embeddings like Word2Vec, GloVe etc. well capture the
contextuality and real-world analogies but contemporary convolution-based image
embeddings such as VGGNet, AlexNet, etc. do not capture contextual knowledge.
The popular king-queen analogy does not hold true for most commonly used vision
embeddings.
  In this paper, we introduce a pre-trained joint embedding (JE), named
IMAGINATOR, trained on 21K distinct image objects level from 1M image+text
pairs. JE is a way to encode multimodal data into a vector space where the text
modality serves as the ground-ing key, which the complementary modality (in
this case, the image) is anchored with. IMAGINATOR encapsulates three
individual representations: (i) object-object co-location, (ii) word-object
co-location, and (iii) word-object correlation. These three ways capture
complementary aspects of the two modalities which are further combined to
obtain the final JEs.
  Generated JEs are intrinsically evaluated to assess how well they capture the
contextuality and real-world analogies. We also evaluate pre-trained IMAGINATOR
JEs on three downstream tasks: (i) image captioning, (ii) Image2Tweet, and
(iii) text-based image retrieval. IMAGINATOR establishes a new standard on the
aforementioned down-stream tasks by outperforming the current SoTA on all the
selected tasks. IMAGINATOR will be made publicly available. The codes are
available at https://github.com/varunakk/IMAGINATOR
