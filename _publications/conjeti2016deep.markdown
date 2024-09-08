---
    layout: publication
    title: "Deep Residual Hashing"
    authors: Conjeti Sailesh, Roy Abhijit Guha, Katouzian Amin, Navab Nassir
    conference: Arxiv
    year: 2016
    bibkey: conjeti2016deep
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1612.05400"}
    tags: ['TIP', 'Arxiv', 'Image Retrieval', 'Supervised', 'Quantisation']
    ---
    Hashing aims at generating highly compact similarity preserving code words which are well suited for large-scale image retrieval tasks. Most existing hashing methods first encode the images as a vector of hand-crafted features followed by a separate binarization step to generate hash codes. This two-stage process may produce sub-optimal encoding. In this paper, for the first time, we propose a deep architecture for supervised hashing through residual learning, termed Deep Residual Hashing (DRH), for an end-to-end simultaneous representation learning and hash coding. The DRH model constitutes four key elements: (1) a sub-network with multiple stacked residual blocks; (2) hashing layer for binarization; (3) supervised retrieval loss function based on neighbourhood component analysis for similarity preserving embedding; and (4) hashing related losses and regularisation to control the quantization error and improve the quality of hash coding. We present results of extensive experiments on a large public chest x-ray image database with co-morbidities and discuss the outcome showing substantial improvements over the latest state-of-the art methods.