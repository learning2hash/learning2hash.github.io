---
layout: publication
title: Neural Image Compression Using Masked Sparse Visual Representation
authors: Wei Jiang, Wei Wang, Yue Chen
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: jiang2023neural
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.11661'}]
tags: []
short_authors: Wei Jiang, Wei Wang, Yue Chen
---
We study neural image compression based on the Sparse Visual Representation
(SVR), where images are embedded into a discrete latent space spanned by
learned visual codebooks. By sharing codebooks with the decoder, the encoder
transfers integer codeword indices that are efficient and cross-platform
robust, and the decoder retrieves the embedded latent feature using the indices
for reconstruction. Previous SVR-based compression lacks effective mechanism
for rate-distortion tradeoffs, where one can only pursue either high
reconstruction quality or low transmission bitrate. We propose a Masked
Adaptive Codebook learning (M-AdaCode) method that applies masks to the latent
feature subspace to balance bitrate and reconstruction quality. A set of
semantic-class-dependent basis codebooks are learned, which are weighted
combined to generate a rich latent feature for high-quality reconstruction. The
combining weights are adaptively derived from each input image, providing
fidelity information with additional transmission costs. By masking out
unimportant weights in the encoder and recovering them in the decoder, we can
trade off reconstruction quality for transmission bits, and the masking rate
controls the balance between bitrate and distortion. Experiments over the
standard JPEG-AI dataset demonstrate the effectiveness of our M-AdaCode
approach.