---
layout: publication
title: Normalized Contrastive Learning For Text-video Retrieval
authors: Yookoon Park, Mahmoud Azab, Bo Xiong, Seungwhan Moon, Florian Metze, Gourab
  Kundu, Kirmani Ahmed
conference: Proceedings of the 2022 Conference on Empirical Methods in Natural Language
  Processing
year: 2022
bibkey: park2022normalized
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.11790'}]
tags: ["Datasets", "EMNLP", "Evaluation", "Multimodal Retrieval", "Video Retrieval"]
short_authors: Park et al.
---
Cross-modal contrastive learning has led the recent advances in multimodal
retrieval with its simplicity and effectiveness. In this work, however, we
reveal that cross-modal contrastive learning suffers from incorrect
normalization of the sum retrieval probabilities of each text or video
instance. Specifically, we show that many test instances are either over- or
under-represented during retrieval, significantly hurting the retrieval
performance. To address this problem, we propose Normalized Contrastive
Learning (NCL) which utilizes the Sinkhorn-Knopp algorithm to compute the
instance-wise biases that properly normalize the sum retrieval probabilities of
each instance so that every text and video instance is fairly represented
during cross-modal retrieval. Empirical study shows that NCL brings consistent
and significant gains in text-video retrieval on different model architectures,
with new state-of-the-art multimodal retrieval metrics on the ActivityNet,
MSVD, and MSR-VTT datasets without any architecture engineering.