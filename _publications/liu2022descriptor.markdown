---
layout: publication
title: 'Descriptor Distillation: A Teacher-student-regularized Framework For Learning
  Local Descriptors'
authors: Yuzhen Liu, Qiulei Dong
conference: Arxiv
year: 2022
bibkey: liu2022descriptor
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2209.11795'}]
tags: ["Datasets", "Distance Metric Learning", "Tools & Libraries"]
short_authors: Yuzhen Liu, Qiulei Dong
---
Learning a fast and discriminative patch descriptor is a challenging topic in
computer vision. Recently, many existing works focus on training various
descriptor learning networks by minimizing a triplet loss (or its variants),
which is expected to decrease the distance between each positive pair and
increase the distance between each negative pair. However, such an expectation
has to be lowered due to the non-perfect convergence of network optimizer to a
local solution. Addressing this problem and the open computational speed
problem, we propose a Descriptor Distillation framework for local descriptor
learning, called DesDis, where a student model gains knowledge from a
pre-trained teacher model, and it is further enhanced via a designed
teacher-student regularizer. This teacher-student regularizer is to constrain
the difference between the positive (also negative) pair similarity from the
teacher model and that from the student model, and we theoretically prove that
a more effective student model could be trained by minimizing a weighted
combination of the triplet loss and this regularizer, than its teacher which is
trained by minimizing the triplet loss singly. Under the proposed DesDis, many
existing descriptor networks could be embedded as the teacher model, and
accordingly, both equal-weight and light-weight student models could be
derived, which outperform their teacher in either accuracy or speed.
Experimental results on 3 public datasets demonstrate that the equal-weight
student models, derived from the proposed DesDis framework by utilizing three
typical descriptor learning networks as teacher models, could achieve
significantly better performances than their teachers and several other
comparative methods. In addition, the derived light-weight models could achieve
8 times or even faster speeds than the comparative methods under similar patch
verification performances