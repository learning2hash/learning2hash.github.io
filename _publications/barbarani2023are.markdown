---
    layout: publication
    title: "Are Local Features All You Need for Cross-Domain Visual Place Recognition"
    authors: Barbarani Giovanni, Mostafa Mohamad, Bayramov Hajali, Trivigno Gabriele, Berton Gabriele, Masone Carlo, Caputo Barbara
    conference: Arxiv
    year: 2023
    bibkey: barbarani2023are
    additional_links:
       - {name: "License", url: "http://arxiv.org/licenses/nonexclusive-distrib/1.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2304.05887"}
   - {name: "Code", url: "https://github.com/gbarbarani/re-ranking-for-VPR."}
    tags: ['Arxiv']
    ---
    Visual Place Recognition is a task that aims to predict the coordinates of an image (called query) based solely on visual clues. Most commonly, a retrieval approach is adopted, where the query is matched to the most similar images from a large database of geotagged photos, using learned global descriptors. Despite recent advances, recognizing the same place when the query comes from a significantly different distribution is still a major hurdle for state of the art retrieval methods. Examples are heavy illumination changes (e.g. night-time images) or substantial occlusions (e.g. transient objects). In this work we explore whether re-ranking methods based on spatial verification can tackle these challenges, following the intuition that local descriptors are inherently more robust than global features to domain shifts. To this end, we provide a new, comprehensive benchmark on current state of the art models. We also introduce two new demanding datasets with night and occluded queries, to be matched against a city-wide database. Code and datasets are available at https://github.com/gbarbarani/re-ranking-for-VPR.