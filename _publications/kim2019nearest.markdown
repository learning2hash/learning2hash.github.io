---
    layout: publication
    title: "Nearest Neighbor Search-Based Bitwise Source Separation Using Discriminant Winner-Take-All Hashing"
    authors: Kim Sunwoo, Kim Minje
    conference: Arxiv
    year: 2019
    bibkey: kim2019nearest
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1908.09799"}
    tags: ['Arxiv', 'ACL']
    ---
    We propose an iteration-free source separation algorithm based on Winner-Take-All (WTA) hash codes, which is a faster, yet accurate alternative to a complex machine learning model for single-channel source separation in a resource-constrained environment. We first generate random permutations with WTA hashing to encode the shape of the multidimensional audio spectrum to a reduced bitstring representation. A nearest neighbor search on the hash codes of an incoming noisy spectrum as the query string results in the closest matches among the hashed mixture spectra. Using the indices of the matching frames, we obtain the corresponding ideal binary mask vectors for denoising. Since both the training data and the search operation are bitwise, the procedure can be done efficiently in hardware implementations. Experimental results show that the WTA hash codes are discriminant and provide an affordable dictionary search mechanism that leads to a competent performance compared to a comprehensive model and oracle masking.