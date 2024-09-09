---
layout: publication
title: "A Novel Framework to Jointly Compress and Index Remote Sensing Images for Efficient Content-Based Retrieval"
authors: Sumbul Gencer, Xiang Jun, Madam Nimisha Thekke, Demir Begüm
conference: Arxiv
year: 2022
bibkey: sumbul2022a
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2201.06459"}
  - {name: "Paper", url: "https://git.tu-berlin.de/rsim/RS-JCIF."}
tags: ['ARXIV', 'Image Retrieval']
---
Remote sensing (RS) images are usually stored in compressed format to reduce the storage size of the archives. Thus, existing content-based image retrieval (CBIR) systems in RS require decoding images before applying CBIR (which is computationally demanding in the case of large-scale CBIR problems). To address this problem, in this paper, we present a joint framework that simultaneously learns RS image compression and indexing. Thus, it eliminates the need for decoding RS images before applying CBIR. The proposed framework is made up of two modules. The first module compresses RS images based on an auto-encoder architecture. The second module produces hash codes with a high discrimination capability by employing soft pairwise, bit-balancing and classification loss functions. We also introduce a two stage learning strategy with gradient manipulation techniques to obtain image representations that are compatible with both RS image indexing and compression. Experimental results show the efficacy of the proposed framework when compared to widely used approaches in RS. The code of the proposed framework is available at https://git.tu-berlin.de/rsim/RS-JCIF.