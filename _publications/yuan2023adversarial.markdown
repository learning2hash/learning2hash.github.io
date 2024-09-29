---
layout: publication
title: Semantic45;aware Adversarial Training For Reliable Deep Hashing Retrieval
authors: Yuan Xu, Zhang Zheng, Wang Xunguang, Wu Lin
conference: "in IEEE Transactions on Information Forensics and Security vol."
year: 2023
bibkey: yuan2023adversarial
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2310.14637"}
  - {name: "Code", url: "https://github.com/xandery&#45;geek/SAAT"}
tags: ['Has Code', 'Image Retrieval', 'Independent']
---
Deep hashing has been intensively studied and successfully applied in large45;scale image retrieval systems due to its efficiency and effectiveness. Recent studies have recognized that the existence of adversarial examples poses a security threat to deep hashing models that is adversarial vulnerability. Notably it is challenging to efficiently distill reliable semantic representatives for deep hashing to guide adversarial learning and thereby it hinders the enhancement of adversarial robustness of deep hashing45;based retrieval models. Moreover current researches on adversarial training for deep hashing are hard to be formalized into a unified minimax structure. In this paper we explore Semantic45;Aware Adversarial Training (SAAT) for improving the adversarial robustness of deep hashing models. Specifically we conceive a discriminative mainstay features learning (DMFL) scheme to construct semantic representatives for guiding adversarial learning in deep hashing. Particularly our DMFL with the strict theoretical guarantee is adaptively optimized in a discriminative learning manner where both discriminative and semantic properties are jointly considered. Moreover adversarial examples are fabricated by maximizing the Hamming distance between the hash codes of adversarial samples and mainstay features the efficacy of which is validated in the adversarial attack trials. Further we for the first time formulate the formalized adversarial training of deep hashing into a unified minimax optimization under the guidance of the generated mainstay codes. Extensive experiments on benchmark datasets show superb attack performance against the state45;of45;the45;art algorithms meanwhile the proposed adversarial training can effectively eliminate adversarial perturbations for trustworthy deep hashing45;based retrieval. Our code is available at https://github.com/xandery&#45;geek/SAAT.
