---
layout: publication
title: Text-based Person Search In Full Images Via Semantic-driven Proposal Generation
authors: Shizhou Zhang, de Cheng, Wenlong Luo, Yinghui Xing, Duo Long, Hao Li, Kai
  Niu, Guoqiang Liang, Yanning Zhang
conference: Arxiv
year: 2021
bibkey: zhang2021text
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.12965'}]
tags: ["Datasets", "Evaluation", "Scalability", "Tools & Libraries"]
short_authors: Zhang et al.
---
Finding target persons in full scene images with a query of text description
has important practical applications in intelligent video surveillance.However,
different from the real-world scenarios where the bounding boxes are not
available, existing text-based person retrieval methods mainly focus on the
cross modal matching between the query text descriptions and the gallery of
cropped pedestrian images. To close the gap, we study the problem of text-based
person search in full images by proposing a new end-to-end learning framework
which jointly optimize the pedestrian detection, identification and
visual-semantic feature embedding tasks. To take full advantage of the query
text, the semantic features are leveraged to instruct the Region Proposal
Network to pay more attention to the text-described proposals. Besides, a
cross-scale visual-semantic embedding mechanism is utilized to improve the
performance. To validate the proposed method, we collect and annotate two
large-scale benchmark datasets based on the widely adopted image-based person
search datasets CUHK-SYSU and PRW. Comprehensive experiments are conducted on
the two datasets and compared with the baseline methods, our method achieves
the state-of-the-art performance.