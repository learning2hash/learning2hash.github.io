---
    layout: publication
    title: "Orientation covariant aggregation of local descriptors with embeddings"
    authors: Tolias Giorgos  INRIA, Furon Teddy  INRIA, Jégou Hervé  INRIA
    conference: Arxiv
    year: 2014
    bibkey: tolias2014orientation
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1407.2170"}
    tags: ['ARXIV']
    ---
    Image search systems based on local descriptors typically achieve orientation invariance by aligning the patches on their dominant orientations. Albeit successful, this choice introduces too much invariance because it does not guarantee that the patches are rotated consistently. This paper introduces an aggregation strategy of local descriptors that achieves this covariance property by jointly encoding the angle in the aggregation stage in a continuous manner. It is combined with an efficient monomial embedding to provide a codebook-free method to aggregate local descriptors into a single vector representation. Our strategy is also compatible and employed with several popular encoding methods, in particular bag-of-words, VLAD and the Fisher vector. Our geometric-aware aggregation strategy is effective for image search, as shown by experiments performed on standard benchmarks for image and particular object retrieval, namely Holidays and Oxford buildings.