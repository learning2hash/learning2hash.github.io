---
layout: publication
title: 'Weakly-paired Cross-modal Hashing'
authors: Xuanwu Liu, Jun Wang, Guoxian Yu, Carlotta Domeniconi, Xiangliang Zhang
conference: "Arxiv"
year: 2019
citations: 0
bibkey: liu2019weakly
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1905.12203'}
tags: ['Hashing Methods', 'Applications', 'Modality-Specific Hashing', 'Tools and Libraries', 'Hashing Fundamentals', 'Multi-Modal Hashing']
---
Hashing has been widely adopted for large-scale data retrieval in many
domains, due to its low storage cost and high retrieval speed. Existing
cross-modal hashing methods optimistically assume that the correspondence
between training samples across modalities are readily available. This
assumption is unrealistic in practical applications. In addition, these methods
generally require the same number of samples across different modalities, which
restricts their flexibility. We propose a flexible cross-modal hashing approach
(Flex-CMH) to learn effective hashing codes from weakly-paired data, whose
correspondence across modalities are partially (or even totally) unknown.
FlexCMH first introduces a clustering-based matching strategy to explore the
local structure of each cluster, and thus to find the potential correspondence
between clusters (and samples therein) across modalities. To reduce the impact
of an incomplete correspondence, it jointly optimizes in a unified objective
function the potential correspondence, the cross-modal hashing functions
derived from the correspondence, and a hashing quantitative loss. An
alternative optimization technique is also proposed to coordinate the
correspondence and hash functions, and to reinforce the reciprocal effects of
the two objectives. Experiments on publicly multi-modal datasets show that
FlexCMH achieves significantly better results than state-of-the-art methods,
and it indeed offers a high degree of flexibility for practical cross-modal
hashing tasks.
