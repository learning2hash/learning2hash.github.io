---
layout: publication
title: 'Toward Real-time Image Annotation Using Marginalized Coupled Dictionary Learning'
authors: Seyed Mahdi Roostaiyan, Mohammad Mehdi Hosseini, Mahya Mohammadi Kashani, S. Hamid Amiri
conference: "Journal of Real-Time Image Processing. 2022 Jun;19(3)623-38"
year: 2023
citations: 3
bibkey: roostaiyan2023toward
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/2304.06907'}
  - {name: "Code", url: 'https://github.com/hamid-amiri/MCDL-Image-Annotation'}
tags: ['Cross-Modal', 'Independent', 'Efficiency', 'Retrieval Models', 'Shallow', 'Datasets', 'Vector Indexing', 'Has Code', 'Training Strategy', 'Applications']
---
In most image retrieval systems, images include various high-level semantics,
called tags or annotations. Virtually all the state-of-the-art image annotation
methods that handle imbalanced labeling are search-based techniques which are
time-consuming. In this paper, a novel coupled dictionary learning approach is
proposed to learn a limited number of visual prototypes and their corresponding
semantics simultaneously. This approach leads to a real-time image annotation
procedure. Another contribution of this paper is that utilizes a marginalized
loss function instead of the squared loss function that is inappropriate for
image annotation with imbalanced labels. We have employed a marginalized loss
function in our method to leverage a simple and effective method of prototype
updating. Meanwhile, we have introduced \\(\{\ell\}_1\\) regularization on semantic
prototypes to preserve the sparse and imbalanced nature of labels in learned
semantic prototypes. Finally, comprehensive experimental results on various
datasets demonstrate the efficiency of the proposed method for image annotation
tasks in terms of accuracy and time. The reference implementation is publicly
available on https://github.com/hamid-amiri/MCDL-Image-Annotation.
