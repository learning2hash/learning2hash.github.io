---
layout: publication
title: 'BEBLID: Boosted Efficient Binary Local Image Descriptor'
authors: "Su\xE1rez Iago, Sfeir Ghesn, Buenaposada Jos\xE9 M., Baumela Luis"
conference: Pattern Recognition Letters
year: 2020
bibkey: "su\xE1rez2024beblid"
citations: 89
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.04482'}]
tags: ["Efficiency", "Evaluation"]
short_authors: "Su\xE1rez et al."
---
Efficient matching of local image features is a fundamental task in many
computer vision applications. However, the real-time performance of top
matching algorithms is compromised in computationally limited devices, such as
mobile phones or drones, due to the simplicity of their hardware and their
finite energy supply. In this paper we introduce BEBLID, an efficient learned
binary image descriptor. It improves our previous real-valued descriptor,
BELID, making it both more efficient for matching and more accurate. To this
end we use AdaBoost with an improved weak-learner training scheme that produces
better local descriptions. Further, we binarize our descriptor by forcing all
weak-learners to have the same weight in the strong learner combination and
train it in an unbalanced data set to address the asymmetries arising in
matching and retrieval tasks. In our experiments BEBLID achieves an accuracy
close to SIFT and better computational efficiency than ORB, the fastest
algorithm in the literature.