---
    layout: publication
    title: "Coding for Random Projections and Approximate Near Neighbor Search"
    authors: Li Ping, Mitzenmacher Michael, Shrivastava Anshumali
    conference: Arxiv
    year: 2014
    bibkey: li2014coding
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1403.8144"}
    tags: ['Arxiv', 'Quantisation']
    ---
    This technical note compares two coding (quantization) schemes for random projections in the context of sub-linear time approximate near neighbor search. The first scheme is based on uniform quantization while the second scheme utilizes a uniform quantization plus a uniformly random offset (which has been popular in practice). The prior work compared the two schemes in the context of similarity estimation and training linear classifiers, with the conclusion that the step of random offset is not necessary and may hurt the performance (depending on the similarity level). The task of near neighbor search is related to similarity estimation with importance distinctions and requires own study. In this paper, we demonstrate that in the context of near neighbor search, the step of random offset is not needed either and may hurt the performance (sometimes significantly so, depending on the similarity and other parameters).