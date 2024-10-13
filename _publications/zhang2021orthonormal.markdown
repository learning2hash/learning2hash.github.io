---
layout: publication
title: Orthonormal Product Quantization Network For Scalable Face Image Retrieval
authors: Zhang Ming, Zhe Xuefei, Yan Hong
conference: "Arxiv"
year: 2021
bibkey: zhang2021orthonormal
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2107.00327"}
tags: ['ARXIV', 'Deep Learning', 'Image Retrieval', 'Quantisation']
---
Existing deep quantization methods provided an efficient solution for
large-scale image retrieval. However, the significant intra-class variations
like pose, illumination, and expressions in face images, still pose a challenge
for face image retrieval. In light of this, face image retrieval requires
sufficiently powerful learning metrics, which are absent in current deep
quantization works. Moreover, to tackle the growing unseen identities in the
query stage, face image retrieval drives more demands regarding model
generalization and system scalability than general image retrieval tasks. This
paper integrates product quantization with orthonormal constraints into an
end-to-end deep learning framework to effectively retrieve face images.
Specifically, a novel scheme that uses predefined orthonormal vectors as
codewords is proposed to enhance the quantization informativeness and reduce
codewords' redundancy. A tailored loss function maximizes discriminability
among identities in each quantization subspace for both the quantized and
original features. An entropy-based regularization term is imposed to reduce
the quantization error. Experiments are conducted on four commonly-used face
datasets under both seen and unseen identities retrieval settings. Our method
outperforms all the compared deep hashing/quantization state-of-the-arts under
both settings. Results validate the effectiveness of the proposed orthonormal
codewords in improving models' standard retrieval performance and
generalization ability. Combing with further experiments on two general image
datasets, it demonstrates the broad superiority of our method for scalable
image retrieval.
