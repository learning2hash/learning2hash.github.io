---
layout: publication
title: Enabling Practical And Privacy-preserving Image Processing
authors: Chao Wang, Shubing Yang, Xiaoyan Sun, Jun Dai, Dongfang Zhao
conference: Arxiv
year: 2024
bibkey: wang2024enabling
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.03568'}]
tags: ["Efficiency"]
short_authors: Wang et al.
---
Fully Homomorphic Encryption (FHE) enables computations on encrypted data,
preserving confidentiality without the need for decryption. However, FHE is
often hindered by significant performance overhead, particularly for
high-precision and complex data like images. Due to serious efficiency issues,
traditional FHE methods often encrypt images by monolithic data blocks (such as
pixel rows), instead of pixels. However, this strategy compromises the
advantages of homomorphic operations and disables pixel-level image processing.
In this study, we address these challenges by proposing and implementing a
pixel-level homomorphic encryption approach, iCHEETAH, based on the CKKS
scheme. To enhance computational efficiency, we introduce three novel caching
mechanisms to pre-encrypt radix values or frequently occurring pixel values,
substantially reducing redundant encryption operations. Extensive experiments
demonstrate that our approach achieves up to a 19-fold improvement in
encryption speed compared to the original CKKS, while maintaining high image
quality. Additionally, real-world image applications such as mean filtering,
brightness enhancement, image matching and watermarking are tested based on
FHE, showcasing up to a 91.53% speed improvement. We also proved that our
method is IND-CPA (Indistinguishability under Chosen Plaintext Attack) secure,
providing strong encryption security. These results underscore the practicality
and efficiency of iCHEETAH, marking a significant advancement in
privacy-preserving image processing at scale.