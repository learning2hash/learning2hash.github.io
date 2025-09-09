---
layout: publication
title: Accelerate Learning Of Deep Hashing With Gradient Attention
authors: Long-Kai Huang, Jianda Chen, Sinno Pan
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: huang2019accelerate
citations: 24
additional_links: [{name: Paper, url: 'http://openaccess.thecvf.com/content_ICCV_2019/papers/Huang_Accelerate_Learning_of_Deep_Hashing_With_Gradient_Attention_ICCV_2019_paper.pdf'}]
tags: ["Datasets", "Evaluation", "Hashing Methods", "ICCV", "Image Retrieval", "Neural Hashing", "Scalability"]
short_authors: Long-Kai Huang, Jianda Chen, Sinno Pan
---
Recent years have witnessed the success of learning to hash in fast large-scale image retrieval. As deep learning has shown its superior performance on many computer vision applications, recent designs of learning-based hashing models have been moving from shallow ones to deep architectures. However, based on our analysis, we find that gradient descent based algorithms used in deep hashing models would potentially cause hash codes of a pair of training instances to be updated towards the directions of each other simultaneously during optimization. In the worst case, the paired hash codes switch their directions after update, and consequently, their corresponding distance in the Hamming space remain unchanged. This makes the overall learning process highly inefficient. To address this issue, we propose a new deep hashing model integrated with a novel gradient attention mechanism. Extensive experimental results on three benchmark datasets show that our proposed algorithm is able to accelerate the learning process and obtain competitive retrieval performance compared with state-of-the-art deep hashing models.