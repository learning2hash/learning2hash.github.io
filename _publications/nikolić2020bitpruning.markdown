---
layout: publication
title: 'Bitpruning: Learning Bitlengths For Aggressive And Accurate Quantization'
authors: "Milo\u0161 Nikoli\u0107, Ghouthi Boukli Hacene, Ciaran Bannon, Alberto Delmas\
  \ Lascorz, Matthieu Courbariaux, Yoshua Bengio, Vincent Gripon, Andreas Moshovos"
conference: Arxiv
year: 2020
bibkey: "nikoli\u01072020bitpruning"
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2002.03090'}]
tags: [Quantization, Memory Efficiency]
short_authors: "Nikoli\u0107 et al."
---
Neural networks have demonstrably achieved state-of-the art accuracy using
low-bitlength integer quantization, yielding both execution time and energy
benefits on existing hardware designs that support short bitlengths. However,
the question of finding the minimum bitlength for a desired accuracy remains
open. We introduce a training method for minimizing inference bitlength at any
granularity while maintaining accuracy. Namely, we propose a regularizer that
penalizes large bitlength representations throughout the architecture and show
how it can be modified to minimize other quantifiable criteria, such as number
of operations or memory footprint. We demonstrate that our method learns
thrifty representations while maintaining accuracy. With ImageNet, the method
produces an average per layer bitlength of 4.13, 3.76 and 4.36 bits on AlexNet,
ResNet18 and MobileNet V2 respectively, remaining within 2.0%, 0.5% and 0.5% of
the base TOP-1 accuracy.