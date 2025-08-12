---
layout: publication
title: Toward Real-time Image Annotation Using Marginalized Coupled Dictionary Learning
authors: Seyed Mahdi Roostaiyan, Mohammad Mehdi Hosseini, Mahya Mohammadi Kashani,
  S. Hamid Amiri
conference: Journal of Real-Time Image Processing
year: 2022
bibkey: roostaiyan2022toward
citations: 4
additional_links: [{name: Code, url: 'https://github.com/hamid-amiri/MCDL-Image-Annotation'},
  {name: Paper, url: 'https://arxiv.org/abs/2304.06907'}]
tags: []
short_authors: Roostaiyan et al.
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
updating. Meanwhile, we have introduced \(\{\ell\}_1\) regularization on semantic
prototypes to preserve the sparse and imbalanced nature of labels in learned
semantic prototypes. Finally, comprehensive experimental results on various
datasets demonstrate the efficiency of the proposed method for image annotation
tasks in terms of accuracy and time. The reference implementation is publicly
available on https://github.com/hamid-amiri/MCDL-Image-Annotation.