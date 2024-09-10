---
layout: publication
title: "Supervised Hashing with Kernels"
authors: W. Liu, J. Wang, R. Ji, Y. Jiang, S. Chang
conference: CVPR
year: 2012
bibkey: liu2012supervised
additional_links:
   - {name: "PDF", url: "http://www.ee.columbia.edu/~wliu/CVPR12_ksh.pdf"}
   - {name: "Code", url: "https://github.com/ColumbiaDVMM/Supervised-Hashing-with-Kernels"}
---
Recent years have witnessed the growing popularity of
hashing in large-scale vision problems. It has been shown
that the hashing quality could be boosted by leveraging supervised
information into hash function learning. However,
the existing supervised methods either lack adequate performance
or often incur cumbersome model training. In this
paper, we propose a novel kernel-based supervised hashing
model which requires a limited amount of supervised information,
i.e., similar and dissimilar data pairs, and a feasible
training cost in achieving high quality hashing. The idea
is to map the data to compact binary codes whose Hamming
distances are minimized on similar pairs and simultaneously
maximized on dissimilar pairs. Our approach is
distinct from prior works by utilizing the equivalence between
optimizing the code inner products and the Hamming
distances. This enables us to sequentially and efficiently
train the hash functions one bit at a time, yielding very
short yet discriminative codes. We carry out extensive experiments
on two image benchmarks with up to one million
samples, demonstrating that our approach significantly outperforms
the state-of-the-arts in searching both metric distance
neighbors and semantically similar neighbors, with
accuracy gains ranging from 13% to 46%.
