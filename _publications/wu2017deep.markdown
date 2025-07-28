---
layout: publication
title: Deep Incremental Hashing Network For Efficient Image Retrieval
authors: Dayan Wu, Dai, Liu, Li, Wang
conference: Proceedings of the 2017 ACM on International Conference on Multimedia
  Retrieval
year: 2017
bibkey: wu2017deep
citations: 67
additional_links: [{name: Paper, url: 'http://openaccess.thecvf.com/content_CVPR_2019/papers/Wu_Deep_Incremental_Hashing_Network_for_Efficient_Image_Retrieval_CVPR_2019_paper.pdf'}]
tags: ["Efficiency", "Hashing Methods", "Image Retrieval", "Neural Hashing"]
short_authors: Wu et al.
---
Hashing has shown great potential in large-scale image retrieval due to its storage and computation efficiency, especially the recent deep supervised hashing methods. To achieve promising performance, deep supervised hashing methods require a large amount of training data from different classes. However, when images of new categories emerge, existing deep hashing methods have to retrain the CNN model and generate hash codes for all the database images again, which is impractical for large-scale retrieval system.
In this paper, we propose a novel deep hashing framework, called Deep Incremental Hashing Network (DIHN), for learning hash codes in an incremental manner. DIHN learns the hash codes for the new coming images directly, while keeping the old ones unchanged. Simultaneously, a deep hash function for query set is learned by preserving the similarities between training points. Extensive experiments on two widely used image retrieval benchmarks demonstrate that the proposed DIHN framework can significantly decrease the training time while keeping the state-of-the-art retrieval accuracy.