---
layout: publication
title: Locality Constraint Dictionary Learning With Support Vector For Pattern Classification
authors: He-Feng Yin, Xiao-Jun Wu, Su-Gen Chen
conference: IEEE Access
year: 2019
bibkey: yin2019locality
citations: 11
additional_links: [{name: Code, url: 'https://github.com/yinhefeng/LCDL-SV'}, {name: Paper,
    url: 'https://arxiv.org/abs/1911.10003'}]
tags: ["Evaluation"]
short_authors: He-Feng Yin, Xiao-Jun Wu, Su-Gen Chen
---
Discriminative dictionary learning (DDL) has recently gained significant
attention due to its impressive performance in various pattern classification
tasks. However, the locality of atoms is not fully explored in conventional DDL
approaches which hampers their classification performance. In this paper, we
propose a locality constraint dictionary learning with support vector
discriminative term (LCDL-SV), in which the locality information is preserved
by employing the graph Laplacian matrix of the learned dictionary. To jointly
learn a classifier during the training phase, a support vector discriminative
term is incorporated into the proposed objective function. Moreover, in the
classification stage, the identity of test data is jointly determined by the
regularized residual and the learned multi-class support vector machine.
Finally, the resulting optimization problem is solved by utilizing the
alternative strategy. Experimental results on benchmark databases demonstrate
the superiority of our proposed method over previous dictionary learning
approaches on both hand-crafted and deep features. The source code of our
proposed LCDL-SV is accessible at https://github.com/yinhefeng/LCDL-SV