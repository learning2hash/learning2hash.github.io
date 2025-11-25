---
layout: publication
title: Robust And Decomposable Average Precision For Image Retrieval
authors: "Elias Ramzi, Nicolas Thome, Cl\xE9ment Rambour, Nicolas Audebert, Xavier\
  \ Bitot"
conference: Thirty-fifth Conference on Neural Information Processing Systems (NeurIPS
  2021) Dec 2021 Sydney Australia
year: 2021
bibkey: ramzi2021robust
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2110.01445'}]
tags: ["Evaluation", "Image Retrieval", "NEURIPS"]
short_authors: Ramzi et al.
---
In image retrieval, standard evaluation metrics rely on score ranking, e.g.
average precision (AP). In this paper, we introduce a method for robust and
decomposable average precision (ROADMAP) addressing two major challenges for
end-to-end training of deep neural networks with AP: non-differentiability and
non-decomposability. Firstly, we propose a new differentiable approximation of
the rank function, which provides an upper bound of the AP loss and ensures
robust training. Secondly, we design a simple yet effective loss function to
reduce the decomposability gap between the AP in the whole training set and its
averaged batch approximation, for which we provide theoretical guarantees.
Extensive experiments conducted on three image retrieval datasets show that
ROADMAP outperforms several recent AP approximation methods and highlight the
importance of our two contributions. Finally, using ROADMAP for training deep
models yields very good performances, outperforming state-of-the-art results on
the three datasets.