---
layout: publication
title: 'Biodeephash: Mapping Biometrics Into A Stable Code'
authors: Song Baogang, Zhao Dongdong, Yan Jiang, Li Huanhuan, Jiang Hao
conference: Arxiv
year: 2024
bibkey: song2024biodeephash
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.03704'}]
tags: ["Compact Codes", "Datasets", "Hashing Methods", "Neural Hashing"]
short_authors: Song et al.
---
With the wide application of biometrics, more and more attention has been
paid to the security of biometric templates. However most of existing biometric
template protection (BTP) methods have some security problems, e.g. the problem
that protected templates leak part of the original biometric data (exists in
Cancelable Biometrics (CB)), the use of error-correcting codes (ECC) leads to
decodable attack, statistical attack (exists in Biometric Cryptosystems (BCS)),
the inability to achieve revocability (exists in methods using Neural Network
(NN) to learn pre-defined templates), the inability to use cryptographic hash
to guarantee strong security (exists in CB and methods using NN to learn latent
templates). In this paper, we propose a framework called BioDeepHash based on
deep hashing and cryptographic hashing to address the above four problems,
where different biometric data of the same user are mapped to a stable code
using deep hashing instead of predefined binary codes thus avoiding the use of
ECC. An application-specific binary string is employed to achieve revocability.
Then cryptographic hashing is used to get the final protected template to
ensure strong security. Ultimately our framework achieves not storing any data
that would leak part of the original biometric data. We also conduct extensive
experiments on facial and iris datasets. Our method achieves an improvement of
10.12\\(%\\) on the average Genuine Acceptance Rate (GAR) for iris data and
3.12\\(%\\) for facial data compared to existing methods. In addition, BioDeepHash
achieves extremely low False Acceptance Rate (FAR), i.e. 0\\(%\\) FAR on the iris
dataset and the highest FAR on the facial dataset is only 0.0002\\(%\\).