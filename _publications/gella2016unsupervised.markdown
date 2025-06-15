---
layout: publication
title: 'Unsupervised Visual Sense Disambiguation For Verbs Using Multimodal Embeddings'
authors: Spandana Gella, Mirella Lapata, Frank Keller
conference: "Arxiv"
year: 2016
citations: 11
bibkey: gella2016unsupervised
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1603.09188'}
  - {name: "Code", url: 'https://github.com/spandanagella/verse'}
tags: ['Cross-Modal', 'Retrieval Models', 'Shallow', 'Datasets', 'Vector Indexing', 'Has Code', 'Supervised', 'Applications']
---
We introduce a new task, visual sense disambiguation for verbs: given an
image and a verb, assign the correct sense of the verb, i.e., the one that
describes the action depicted in the image. Just as textual word sense
disambiguation is useful for a wide range of NLP tasks, visual sense
disambiguation can be useful for multimodal tasks such as image retrieval,
image description, and text illustration. We introduce VerSe, a new dataset
that augments existing multimodal datasets (COCO and TUHOI) with sense labels.
We propose an unsupervised algorithm based on Lesk which performs visual sense
disambiguation using textual, visual, or multimodal embeddings. We find that
textual embeddings perform well when gold-standard textual annotations (object
labels and image descriptions) are available, while multimodal embeddings
perform well on unannotated images. We also verify our findings by using the
textual and multimodal embeddings as features in a supervised setting and
analyse the performance of visual sense disambiguation task. VerSe is made
publicly available and can be downloaded at:
https://github.com/spandanagella/verse.
