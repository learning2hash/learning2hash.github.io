---
    layout: publication
    title: "Low-Precision Quantization for Efficient Nearest Neighbor Search"
    authors: Ko Anthony, Keivanloo Iman, Lakshman Vihan, Schkufza Eric
    conference: Arxiv
    year: 2021
    bibkey: ko2021low
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2110.08919"}
    tags: ['TIP', 'Arxiv', 'Quantisation']
    ---
    Fast k-Nearest Neighbor search over real-valued vector spaces (KNN) is an important algorithmic task for information retrieval and recommendation systems. We present a method for using reduced precision to represent vectors through quantized integer values, enabling both a reduction in the memory overhead of indexing these vectors and faster distance computations at query time. While most traditional quantization techniques focus on minimizing the reconstruction error between a point and its uncompressed counterpart, we focus instead on preserving the behavior of the underlying distance metric. Furthermore, our quantization approach is applied at the implementation level and can be combined with existing KNN algorithms. Our experiments on both open source and proprietary datasets across multiple popular KNN frameworks validate that quantized distance metrics can reduce memory by 60% and improve query throughput by 30%, while incurring only a 2% reduction in recall.