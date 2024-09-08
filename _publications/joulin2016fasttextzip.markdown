---
layout: publication
title: FastText.zip: Compressing text classification models
authors: Joulin Armand, Grave Edouard, Bojanowski Piotr, Douze Matthijs, Jégou Hérve, Mikolov Tomas
conference: Arxiv
year: 2016
bibkey: joulin2016fasttextzip
additional_links:
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1612.03651"}
tags: ['Arxiv', 'Quantisation']
---
We consider the problem of producing compact architectures for text classification, such that the full model fits in a limited amount of memory. After considering different solutions inspired by the hashing literature, we propose a method built upon product quantization to store word embeddings. While the original technique leads to a loss in accuracy, we adapt this method to circumvent quantization artefacts. Our experiments carried out on several benchmarks show that our approach typically requires two orders of magnitude less memory than fastText while being only slightly inferior with respect to accuracy. As a result, it outperforms the state of the art by a good margin in terms of the compromise between memory usage and accuracy.
