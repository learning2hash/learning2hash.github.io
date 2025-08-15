---
layout: publication
title: Learning A Deep \(\ell_\infty\) Encoder For Hashing
authors: Zhangyang Wang, Yingzhen Yang, Shiyu Chang, Qing Ling, Thomas S. Huang
conference: Arxiv
year: 2016
bibkey: wang2016learning
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1604.01475'}]
tags: ["Hashing Methods", "Quantization", "Robustness", "Supervised"]
short_authors: Wang et al.
---
We investigate the \(\ell_\infty\)-constrained representation which
demonstrates robustness to quantization errors, utilizing the tool of deep
learning. Based on the Alternating Direction Method of Multipliers (ADMM), we
formulate the original convex minimization problem as a feed-forward neural
network, named \textit\{Deep \(\ell_\infty\) Encoder\}, by introducing the novel
Bounded Linear Unit (BLU) neuron and modeling the Lagrange multipliers as
network biases. Such a structural prior acts as an effective network
regularization, and facilitates the model initialization. We then investigate
the effective use of the proposed model in the application of hashing, by
coupling the proposed encoders under a supervised pairwise loss, to develop a
\textit\{Deep Siamese \(\ell_\infty\) Network\}, which can be optimized from end to
end. Extensive experiments demonstrate the impressive performances of the
proposed model. We also provide an in-depth analysis of its behaviors against
the competitors.