---
layout: publication
title: Cgat Center-guided Adversarial Training For Deep Hashing-based Retrieval
authors: Wang Xunguang, Lin Yiqun, Li Xiaomeng
conference: "Arxiv"
year: 2022
bibkey: wang2022cgat
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2204.10779"}
  - {name: "Code", url: "https://github.com/xunguangwang/CgAT"}
tags: ['ARXIV', 'Has Code', 'Image Retrieval', 'Independent']
---
Deep hashing has been extensively utilized in massive image retrieval because of its efficiency and effectiveness. However deep hashing models are vulnerable to adversarial examples making it essential to develop adversarial defense methods for image retrieval. Existing solutions achieved limited defense performance because of using weak adversarial samples for training and lacking discriminative optimization objectives to learn robust features. In this paper we present a min-max based Center-guided Adversarial Training namely CgAT to improve the robustness of deep hashing networks through worst adversarial examples. Specifically we first formulate the center code as a semantically-discriminative representative of the input image content which preserves the semantic similarity with positive samples and dissimilarity with negative examples. We prove that a mathematical formula can calculate the center code immediately. After obtaining the center codes in each optimization iteration of the deep hashing network they are adopted to guide the adversarial training process. On the one hand CgAT generates the worst adversarial examples as augmented data by maximizing the Hamming distance between the hash codes of the adversarial examples and the center codes. On the other hand CgAT learns to mitigate the effects of adversarial samples by minimizing the Hamming distance to the center codes. Extensive experiments on the benchmark datasets demonstrate the effectiveness of our adversarial training algorithm in defending against adversarial attacks for deep hashing-based retrieval. Compared with the current state-of-the-art defense method we significantly improve the defense performance by an average of 18.6137; 12.3537; and 11.5637; on FLICKR-25K NUS-WIDE and MS-COCO respectively. The code is available at https://github.com/xunguangwang/CgAT.
