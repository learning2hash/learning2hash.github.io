---
    layout: publication
    title: "SUVR: A Search-based Approach to Unsupervised Visual Representation Learning"
    authors: Xu Yi-Zhan, Chen Chih-Yao, Li Cheng-Te
    conference: Arxiv
    year: 2023
    bibkey: xu2023suvr
    additional_links:
       - {name: "DOI", url: "10.1109/ICASSP49357.2023.10096936"}
   - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2305.14754"}
    tags: ['Supervised', 'Arxiv', 'Unsupervised', 'Graph']
    ---
    {% raw %}
    Unsupervised learning has grown in popularity because of the difficulty of collecting annotated data and the development of modern frameworks that allow us to learn from unlabeled data. Existing studies, however, either disregard variations at different levels of similarity or only consider negative samples from one batch. We argue that image pairs should have varying degrees of similarity, and the negative samples should be allowed to be drawn from the entire dataset. In this work, we propose Search-based Unsupervised Visual Representation Learning (SUVR) to learn better image representations in an unsupervised manner. We first construct a graph from the image dataset by the similarity between images, and adopt the concept of graph traversal to explore positive samples. In the meantime, we make sure that negative samples can be drawn from the full dataset. Quantitative experiments on five benchmark image classification datasets demonstrate that SUVR can significantly outperform strong competing methods on unsupervised embedding learning. Qualitative experiments also show that SUVR can produce better representations in which similar images are clustered closer together than unrelated images in the latent space.
    {% endraw %}