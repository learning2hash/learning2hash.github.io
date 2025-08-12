---
layout: publication
title: Learning Semantically Enhanced Feature For Fine-grained Image Classification
authors: Wei Luo, Hengmin Zhang, Jun Li, Xiu-Shen Wei
conference: IEEE Signal Processing Letters
year: 2020
bibkey: luo2020learning
citations: 74
additional_links: [{name: Code, url: 'https://github.com/cswluo/SEF'}, {name: Paper,
    url: 'https://arxiv.org/abs/2006.13457'}]
tags: []
short_authors: Luo et al.
---
We aim to provide a computationally cheap yet effective approach for
fine-grained image classification (FGIC) in this letter. Unlike previous
methods that rely on complex part localization modules, our approach learns
fine-grained features by enhancing the semantics of sub-features of a global
feature. Specifically, we first achieve the sub-feature semantic by arranging
feature channels of a CNN into different groups through channel permutation.
Meanwhile, to enhance the discriminability of sub-features, the groups are
guided to be activated on object parts with strong discriminability by a
weighted combination regularization. Our approach is parameter parsimonious and
can be easily integrated into the backbone model as a plug-and-play module for
end-to-end training with only image-level supervision. Experiments verified the
effectiveness of our approach and validated its comparable performance to the
state-of-the-art methods. Code is available at https://github.com/cswluo/SEF