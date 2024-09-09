---
layout: publication
title: A Novel Feature Descriptor for Image Retrieval by Combining Modified Color Histogram and Diagonally Symmetric Co-occurrence Texture Pattern
authors: Bhunia Ayan Kumar, Bhattacharyya Avirup, Banerjee Prithaj, Roy Partha Pratim, Murala Subrahmanyam
conference: "Arxiv"
year: 2018
bibkey: bhunia2018a
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1801.00879"}
tags: ['ARXIV', 'Image Retrieval']
---
In this paper we have proposed a novel feature descriptors combining color and texture information collectively. In our proposed color descriptor component the inter-channel relationship between Hue (H) and Saturation (S) channels in the HSV color space has been explored which was not done earlier. We have quantized the H channel into a number of bins and performed the voting with saturation values and vice versa by following a principle similar to that of the HOG descriptor where orientation of the gradient is quantized into a certain number of bins and voting is done with gradient magnitude. This helps us to study the nature of variation of saturation with variation in Hue and nature of variation of Hue with the variation in saturation. The texture component of our descriptor considers the co-occurrence relationship between the pixels symmetric about both the diagonals of a 3x3 window. Our work is inspired from the work done by Dubey et al.1. These two components viz. color and texture information individually perform better than existing texture and color descriptors. Moreover when concatenated the proposed descriptors provide significant improvement over existing descriptors for content base color image retrieval. The proposed descriptor has been tested for image retrieval on five databases including texture image databases - MIT VisTex database and Salzburg texture database and natural scene databases Corel 1K Corel 5K and Corel 10K. The precision and recall values experimented on these databases are compared with some state-of-art local patterns. The proposed method provided satisfactory results from the experiments.
