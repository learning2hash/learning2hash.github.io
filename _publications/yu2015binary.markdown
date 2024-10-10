---
layout: publication
title: On Binary Embedding Using Circulant Matrices
authors: Yu Felix X., Bhaskara Aditya, Kumar Sanjiv, Gong Yunchao, Chang Shih-fu
conference: "Arxiv"
year: 2015
bibkey: yu2015binary
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1511.06480"}
tags: ['ARXIV', 'Independent']
---
Binary embeddings provide efficient and powerful ways to perform operations on large scale data. However binary embedding typically requires long codes in order to preserve the discriminative power of the input space. Thus binary coding methods traditionally suffer from high computation and storage costs in such a scenario. To address this problem we propose Circulant Binary Embedding (CBE) which generates binary codes by projecting the data with a circulant matrix. The circulant structure allows us to use Fast Fourier Transform algorithms to speed up the computation. For obtaining (k)-bit binary codes from (d)-dimensional data this improves the time complexity from (O(dk)) to (O(d)) and the space complexity from (O(dk)) to (O(d)). We study two settings which differ in the way we choose the parameters of the circulant matrix. In the first the parameters are chosen randomly and in the second the parameters are learned using the data. For randomized CBE we give a theoretical analysis comparing it with binary embedding using an unstructured random projection matrix. The challenge here is to show that the dependencies in the entries of the circulant matrix do not lead to a loss in performance. In the second setting we design a novel time-frequency alternating optimization to learn data-dependent circulant projections which alternatively minimizes the objective in original and Fourier domains. In both the settings we show by extensive experiments that the CBE approach gives much better performance than the state-of-the-art approaches if we fix a running time and provides much faster computation with negligible performance degradation if we fix the number of bits in the embedding.
