---
layout: publication
title: Deep Polarized Network for Supervised Learning of Accurate Binary Hashing Codes
authors: Fan Lixin, Ng, Ju, Zhang, Chan
conference: Proceedings of the Twenty-Ninth International Joint Conference on Artificial
  Intelligence
year: 2020
bibkey: fan2020deep
citations: 81
additional_links: [{name: Paper, url: 'https://www.ijcai.org/proceedings/2020/0115.pdf'}]
tags: ["Distance-Metric-Learning", "Datasets", "AAAI", "Compact-Codes", "Tools-&-Libraries", "Hashing-Methods", "IJCAI", "Supervised"]
short_authors: Fan et al.
---
This paper proposes a novel deep polarized network (DPN) for learning to hash, in which each channel in the network outputs is pushed far away
from zero by employing a differentiable bit-wise hinge-like loss which is dubbed as polarization loss. Reformulated within a generic Hamming Distance Metric Learning framework [Norouzi et al.,
2012], the proposed polarization loss bypasses the requirement to prepare pairwise labels for (dis-)similar items and, yet, the proposed loss strictly bounds from above the pairwise Hamming Distance based losses. The intrinsic connection between pairwise and pointwise label information, as
disclosed in this paper, brings about the following methodological improvements: (a) we may directly employ the proposed differentiable polarization loss with no large deviations incurred from
the target Hamming distance based loss; and (b) the subtask of assigning binary codes becomes extremely simple — even random codes assigned to each class suffice to result in state-of-the-art performances, as demonstrated in CIFAR10, NUS-WIDE and ImageNet100 datasets.