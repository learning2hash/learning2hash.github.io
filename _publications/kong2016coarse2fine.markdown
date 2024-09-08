---
    layout: publication
    title: "Coarse2Fine: Two-Layer Fusion For Image Retrieval"
    authors: Kong Gaipeng, Dong Le, Dong Wenpu, Zheng Liang, Tian Qi
    conference: Arxiv
    year: 2016
    bibkey: kong2016coarse2fine
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1607.00719"}
    tags: ['Arxiv', 'TIP', 'Image Retrieval']
    ---
    {% raw %}
    This paper addresses the problem of large-scale image retrieval. We propose a two-layer fusion method which takes advantage of global and local cues and ranks database images from coarse to fine (C2F). Departing from the previous methods fusing multiple image descriptors simultaneously, C2F is featured by a layered procedure composed by filtering and refining. In particular, C2F consists of three components. 1) Distractor filtering. With holistic representations, noise images are filtered out from the database, so the number of candidate images to be used for comparison with the query can be greatly reduced. 2) Adaptive weighting. For a certain query, the similarity of candidate images can be estimated by holistic similarity scores in complementary to the local ones. 3) Candidate refining. Accurate retrieval is conducted via local features, combining the pre-computed adaptive weights. Experiments are presented on two benchmarks, \emph{i.e.,} Holidays and Ukbench datasets. We show that our method outperforms recent fusion methods in terms of storage consumption and computation complexity, and that the accuracy is competitive to the state-of-the-arts.
    {% endraw %}