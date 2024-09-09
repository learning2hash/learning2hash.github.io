---
    layout: publication
    title: "Unified Functional Hashing in Automatic Machine Learning"
    authors: Gillard Ryan, Jonany Stephen, Miao Yingjie, Munn Michael, de Souza Connal, Dungay Jonathan, Liang Chen, So David R., Le Quoc V., Real Esteban
    conference: Arxiv
    year: 2023
    bibkey: gillard2023unified
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/2302.05433"}
    tags: ['ARXIV', 'Graph', 'TIP', 'TOM']
    ---
    The field of Automatic Machine Learning (AutoML) has recently attained impressive results, including the discovery of state-of-the-art machine learning solutions, such as neural image classifiers. This is often done by applying an evolutionary search method, which samples multiple candidate solutions from a large space and evaluates the quality of each candidate through a long training process. As a result, the search tends to be slow. In this paper, we show that large efficiency gains can be obtained by employing a fast unified functional hash, especially through the functional equivalence caching technique, which we also present. The central idea is to detect by hashing when the search method produces equivalent candidates, which occurs very frequently, and this way avoid their costly re-evaluation. Our hash is "functional" in that it identifies equivalent candidates even if they were represented or coded differently, and it is "unified" in that the same algorithm can hash arbitrary representations; e.g. compute graphs, imperative code, or lambda functions. As evidence, we show dramatic improvements on multiple AutoML domains, including neural architecture search and algorithm discovery. Finally, we consider the effect of hash collisions, evaluation noise, and search distribution through empirical analysis. Altogether, we hope this paper may serve as a guide to hashing techniques in AutoML.