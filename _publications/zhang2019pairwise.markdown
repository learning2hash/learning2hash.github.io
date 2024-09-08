---
    layout: publication
    title: "Pairwise Teacher-Student Network for Semi-Supervised Hashing"
    authors: Zhang Shifeng, Li Jianmin, Zhang Bo
    conference: Arxiv
    year: 2019
    bibkey: zhang2019pairwise
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/1902.00643"}
    tags: ['Supervised', 'Graph', 'Semi-Supervised', 'Arxiv']
    ---
    Hashing method maps similar high-dimensional data to binary hashcodes with smaller hamming distance, and it has received broad attention due to its low storage cost and fast retrieval speed. Pairwise similarity is easily obtained and widely used for retrieval, and most supervised hashing algorithms are carefully designed for the pairwise supervisions. As labeling all data pairs is difficult, semi-supervised hashing is proposed which aims at learning efficient codes with limited labeled pairs and abundant unlabeled ones. Existing methods build graphs to capture the structure of dataset, but they are not working well for complex data as the graph is built based on the data representations and determining the representations of complex data is difficult. In this paper, we propose a novel teacher-student semi-supervised hashing framework in which the student is trained with the pairwise information produced by the teacher network. The network follows the smoothness assumption, which achieves consistent distances for similar data pairs so that the retrieval results are similar for neighborhood queries. Experiments on large-scale datasets show that the proposed method reaches impressive gain over the supervised baselines and is superior to state-of-the-art semi-supervised hashing methods.