---
layout: publication
title: Local Similarity45;aware Deep Feature Embedding
authors: Chen Huang, Chen Change Loy, Xiaoou Tang
conference: "Neural Information Processing Systems"
year: 2016
bibkey: huang2016local
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2016/hash/556f391937dfd4398cbac35e050a2177-Abstract.html"}
tags: ['Image Retrieval', 'NEURIPS']
---
Existing deep embedding methods in vision tasks are capable of learning a compact Euclidean space from images where Euclidean distances correspond to a similarity metric. To make learning more effective and efficient hard sample mining is usually employed with samples identified through computing the Euclidean feature distance. However the global Euclidean distance cannot faithfully characterize the true feature similarity in a complex visual feature space where the intraclass distance in a high45;density region may be larger than the interclass distance in low45;density regions. In this paper we introduce a Position45;Dependent Deep Metric (PDDM) unit which is capable of learning a similarity metric adaptive to local feature structure. The metric can be used to select genuinely hard samples in a local neighborhood to guide the deep embedding learning in an online and robust manner. The new layer is appealing in that it is pluggable to any convolutional networks and is trained end45;to45;end. Our local similarity45;aware feature embedding not only demonstrates faster convergence and boosted performance on two complex image retrieval datasets its large margin nature also leads to superior generalization results under the large and open set scenarios of transfer learning and zero45;shot learning on ImageNet 2010 and ImageNet45;10K datasets.
