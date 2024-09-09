---
    layout: publication
    title: "Optimal Projection Guided Transfer Hashing for Image Retrieval"
    authors: Liu Ji, Zhang Lei
    conference: Arxiv
    year: 2019
    bibkey: liu2019optimal
    additional_links:
      - {name: "Paper", url: "https://arxiv.org/abs/1903.00252"}
  - {name: "Code", url: "https://github.com/liuji93/GTH."}
    tags: ['ARXIV', 'Image Retrieval', 'Supervised', 'Unsupervised']
    ---
    Recently, learning to hash has been widely studied for image retrieval thanks to the computation and storage efficiency of binary codes. For most existing learning to hash methods, sufficient training images are required and used to learn precise hashing codes. However, in some real-world applications, there are not always sufficient training images in the domain of interest. In addition, some existing supervised approaches need a amount of labeled data, which is an expensive process in term of time, label and human expertise. To handle such problems, inspired by transfer learning, we propose a simple yet effective unsupervised hashing method named Optimal Projection Guided Transfer Hashing (GTH) where we borrow the images of other different but related domain i.e., source domain to help learn precise hashing codes for the domain of interest i.e., target domain. Besides, we propose to seek for the maximum likelihood estimation (MLE) solution of the hashing functions of target and source domains due to the domain gap. Furthermore,an alternating optimization method is adopted to obtain the two projections of target and source domains such that the domain hashing disparity is reduced gradually. Extensive experiments on various benchmark databases verify that our method outperforms many state-of-the-art learning to hash methods. The implementation details are available at https://github.com/liuji93/GTH.