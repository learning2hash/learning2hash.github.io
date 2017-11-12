---
layout: publication
title: "Bit-Scalable Deep Hashing With Regularized Similarity Learning for Image Retrieval and Person Re-Identification"
authors: R. Zhang, L. Lin, R. Zhang, W. Zuo, L. Zhang
conference: TIP
year: 2015
bibkey: zhang2015bit
additional_links:
   - {name: "PDF", url: "http://arxiv.org/pdf/1508.04535v2.pdf"}
   - {name: "Code", url: "https://github.com/ruixuejianfei/BitScalableDeepHash"}
---
Extracting informative image features and learning
effective approximate hashing functions are two crucial steps in
image retrieval . Conventional methods often study these two
steps separately, e.g., learning hash functions from a predefined
hand-crafted feature space. Meanwhile, the bit lengths of output
hashing codes are preset in most previous methods, neglecting the
significance level of different bits and restricting their practical
flexibility. To address these issues, we propose a supervised
learning framework to generate compact and bit-scalable hashing
codes directly from raw images. We pose hashing learning as
a problem of regularized similarity learning. Specifically, we
organize the training images into a batch of triplet samples,
each sample containing two images with the same label and one
with a different label. With these triplet samples, we maximize
the margin between matched pairs and mismatched pairs in the
Hamming space. In addition, a regularization term is introduced
to enforce the adjacency consistency, i.e., images of similar
appearances should have similar codes. The deep convolutional
neural network is utilized to train the model in an end-to-end
fashion, where discriminative image features and hash functions
are simultaneously optimized. Furthermore, each bit of our
hashing codes is unequally weighted so that we can manipulate
the code lengths by truncating the insignificant bits. Our
framework outperforms state-of-the-arts on public benchmarks
of similar image search and also achieves promising results in
the application of person re-identification in surveillance. It is
also shown that the generated bit-scalable hashing codes well
preserve the discriminative powers with shorter code lengths.
