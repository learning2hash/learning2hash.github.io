---
    layout: publication
    title: "Medical Image Retrieval via Nearest Neighbor Search on Pre-trained Image Features"
    authors: Gupta Deepak, Loane Russell, Gayen Soumya, Demner-Fushman Dina
    conference: Arxiv
    year: 2022
    bibkey: gupta2022medical
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/2210.02401"}
  - {name: "Code", url: "https://github.com/deepaknlp/DLS."}
    tags: ['ARXIV', 'Image Retrieval', 'TIP']
    ---
    Nearest neighbor search (NNS) aims to locate the points in high-dimensional space that is closest to the query point. The brute-force approach for finding the nearest neighbor becomes computationally infeasible when the number of points is large. The NNS has multiple applications in medicine, such as searching large medical imaging databases, disease classification, diagnosis, etc. With a focus on medical imaging, this paper proposes DenseLinkSearch an effective and efficient algorithm that searches and retrieves the relevant images from heterogeneous sources of medical images. Towards this, given a medical database, the proposed algorithm builds the index that consists of pre-computed links of each point in the database. The search algorithm utilizes the index to efficiently traverse the database in search of the nearest neighbor. We extensively tested the proposed NNS approach and compared the performance with state-of-the-art NNS approaches on benchmark datasets and our created medical image datasets. The proposed approach outperformed the existing approach in terms of retrieving accurate neighbors and retrieval speed. We also explore the role of medical image feature representation in content-based medical image retrieval tasks. We propose a Transformer-based feature representation technique that outperformed the existing pre-trained Transformer approach on CLEF 2011 medical image retrieval task. The source code of our experiments are available at https://github.com/deepaknlp/DLS.