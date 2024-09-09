---
    layout: publication
    title: "Implicit Sparse Code Hashing"
    authors: Lin Tsung-Yu, Ke Tsung-Wei, Liu Tyng-Luh
    conference: Arxiv
    year: 2015
    bibkey: lin2015implicit
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1512.00130"}
    tags: ['ARXIV', 'Supervised', 'Unsupervised']
    ---
    We address the problem of converting large-scale high-dimensional image data into binary codes so that approximate nearest-neighbor search over them can be efficiently performed. Different from most of the existing unsupervised approaches for yielding binary codes, our method is based on a dimensionality-reduction criterion that its resulting mapping is designed to preserve the image relationships entailed by the inner products of sparse codes, rather than those implied by the Euclidean distances in the ambient space. While the proposed formulation does not require computing any sparse codes, the underlying computation model still inevitably involves solving an unmanageable eigenproblem when extremely high-dimensional descriptors are used. To overcome the difficulty, we consider the column-sampling technique and presume a special form of rotation matrix to facilitate subproblem decomposition. We test our method on several challenging image datasets and demonstrate its effectiveness by comparing with state-of-the-art binary coding techniques.