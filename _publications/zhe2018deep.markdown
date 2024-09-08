---
    layout: publication
    title: "Deep Class-Wise Hashing: Semantics-Preserving Hashing via Class-wise Loss"
    authors: Zhe Xuefei, Chen Shifeng, Yan Hong
    conference: Arxiv
    year: 2018
    bibkey: zhe2018deep
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1803.04137"}
    tags: ['Image Retrieval', 'Supervised', 'Deep Learning', 'Arxiv']
    ---
    Deep supervised hashing has emerged as an influential solution to large-scale semantic image retrieval problems in computer vision. In the light of recent progress, convolutional neural network based hashing methods typically seek pair-wise or triplet labels to conduct the similarity preserving learning. However, complex semantic concepts of visual contents are hard to capture by similar/dissimilar labels, which limits the retrieval performance. Generally, pair-wise or triplet losses not only suffer from expensive training costs but also lack in extracting sufficient semantic information. In this regard, we propose a novel deep supervised hashing model to learn more compact class-level similarity preserving binary codes. Our deep learning based model is motivated by deep metric learning that directly takes semantic labels as supervised information in training and generates corresponding discriminant hashing code. Specifically, a novel cubic constraint loss function based on Gaussian distribution is proposed, which preserves semantic variations while penalizes the overlap part of different classes in the embedding space. To address the discrete optimization problem introduced by binary codes, a two-step optimization strategy is proposed to provide efficient training and avoid the problem of gradient vanishing. Extensive experiments on four large-scale benchmark databases show that our model can achieve the state-of-the-art retrieval performance. Moreover, when training samples are limited, our method surpasses other supervised deep hashing methods with non-negligible margins.