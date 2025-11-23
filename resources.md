---
layout: default
title: Resources on Machine Learning for Hashing
---

<h2 style="font-size: 1.8em; margin-bottom: 10px;">📚 Resources on Machine Learning for Hashing</h2>
<p style="font-size: 1.05em;">
  A curated collection of <strong>books</strong>, <strong>courses</strong>, 
  <strong>datasets</strong>, and <strong>tools</strong> covering 
  <strong>Machine Learning for Hashing</strong>. Use the search bar below to 
  quickly find resources by title, domain, or description.
</p>

<!-- Slim Toolbar -->
<div id="resToolbar" class="toolbar" style="display:none;">
  <div class="left">
    <div class="search">
      <label for="resSearch"><strong>Search</strong></label>
      <input id="resSearch" type="search"
             placeholder="🔍 Search title, domain, description…"
             inputmode="search" />
      <button id="resetResSearch" type="button" aria-label="Clear search">Clear</button>
      <span id="resVisibleCount" class="small" aria-live="polite"></span>
    </div>
  </div>
</div>

<!-- Loading Indicator -->
<div id="loading" role="status" aria-live="polite">
  <p>Loading Resources Explorer …</p>
</div>

<!-- Cards View (auto-built from the lists below) -->
<div id="cardsGrid" class="cards" style="display:none;" aria-live="polite"></div>
<p id="emptyState" class="empty" style="display:none;">No resources match your search.</p>

<!-- Hidden Data Table (engine only) -->
<table id="resources-table" class="display stripe hover" style="width:100%; display:none;">
  <thead>
    <tr>
      <th>TitleHTML</th>
      <th>Category</th>
      <th>Subcategory</th>
      <th>DescHTML</th>
      <th>raw</th>
      <th>url</th>
      <th>domain</th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

<!-- Source content (rendered Markdown but hidden from users) -->
<details id="resourcesContent" markdown="1" hidden aria-hidden="true">
  <summary>Hidden resources source</summary>

# Resources on Machine Learning for Hashing

### 🎥📘 Introductory Video Material

- **[Dr. Wu-Jun Li's tutorial slides](https://cs.nju.edu.cn/lwj/slides/L2H.pdf)**: These tutorial slides by Dr. Wu-Jun Li offer a comprehensive introduction to learning to hash (L2H) techniques. It's an excellent resource for anyone seeking a deep understanding of hashing from a technical perspective.

- **[Intro to LSH - Part 1](https://www.youtube.com/watch?v=Arni-zkqMBA)**: In this video, Dr. Victor Lavrenko provides an introduction to Locality-Sensitive Hashing (LSH). Part 1 covers the basic concepts and intuition behind LSH, making it accessible for beginners.

- **[Intro to LSH - Part 2](https://www.youtube.com/watch?v=dgH0NP8Qxa8)**: Part 2 of Dr. Lavrenko's LSH series dives deeper into the mathematics and mechanics of how LSH works. 

- **[Hashing Algorithms for Large-Scale Machine Learning - 2017 Rice Machine Learning Workshop](https://www.youtube.com/embed/tQ0OJXowLJA)**: This video is a recording of a presentation from the 2017 Rice Machine Learning Workshop. It offers a detailed overview of various hashing algorithms used for large-scale machine learning.

### 🎤🧑‍🔬Conferences and Workshops

- **[IJCNN 2025: Scalable and Deep Graph Learning and Mining](https://www.ijcnn.org/)**: Workshop including hashing methods applied to graph structures for retrieval and similarity.
  
- **[Practical Vector Search Challenge 2023](https://big-ann-benchmarks.com/neurips23.html)**: This challenge aims to push the boundaries of approximate nearest neighbor (ANN) search techniques and offers a platform for researchers and developers to benchmark their solutions on billion-scale datasets.

- **[Billion-Scale Approximate Nearest Neighbor Search Challenge: NeurIPS'21 Competition Track](http://big-ann-benchmarks.com/index.html#call)**: Competitors must improve search accuracy and speed on extremely large datasets, providing valuable insights into the performance of state-of-the-art methods for nearest neighbor search.

- **[Compact and Efficient Feature Representation and Learning in Computer Vision, ICCV 2019](http://www.ee.oulu.fi/~lili/CEFRLatICCV2019.html)**: This workshop at ICCV 2019 focuses on efficient learning techniques for compact feature representations, including binary hashing methods. 

- **[International Conference on Similarity Search and Applications](http://www.sisap.org/2020/)**: SISAP is an annual conference dedicated to the study of similarity search techniques.
  
- **[Joint Workshop on Efficient Deep Learning in Computer Vision](https://workshop-edlcv.github.io/)**: This workshop, co-located with CVPR 2020, focused on the intersection of deep learning and efficient computing techniques for computer vision tasks. 

- **[IEEE International Conference on Data Engineering (ICDE)](https://icde.org/)**: ICDE is one of the leading conferences on data engineering, where researchers present advances in data management, indexing, and search. 

- **[ACM International Conference on Knowledge Discovery and Data Mining (KDD)](https://www.kdd.org/kdd2021/)**: KDD is a premier conference on data mining and machine learning. 

- **[SIAM International Conference on Data Mining (SDM)](https://www.siam.org/conferences/cm/conference/sdm22)**: SDM is an important conference for researchers in data mining, focusing on the latest developments in algorithms, data analysis, and big data applications. 

### 📄🔬 Survey Papers

For a deeper dive, these survey papers are excellent resources:

- **[Learning-Based Hashing for Approximate Nearest Neighbour (ANN) Search: Foundations and Early Advances](/papers/Learning_Based_Hashing_for_ANN_Search__Foundations_and_Early_Advances.pdf)** (Moran, 2025): A foundational survey introducing the core principles of learning-based hashing for ANN search. 

- **[Learning to Hash for Recommendation: A Survey](https://arxiv.org/abs/2412.03875)** (2024): A dedicated overview of hashing-based methods used in recommender systems, from binary encodings to retrieval-aware deep architectures.
  
- **[Learning to Hash for Indexing Big Data - A Survey](https://arxiv.org/pdf/1509.05472.pdf)**: This comprehensive survey explores the evolution of hashing techniques for indexing and retrieving big data.
  
- **[A Survey on Learning to Hash](https://arxiv.org/pdf/1606.00185.pdf)**: This survey provides a detailed overview of different learning-to-hash algorithms, categorized into unsupervised, semi-supervised, and supervised methods. 

- **[Learning Binary Hash Codes for Large-Scale Image Search](http://www.cs.utexas.edu/~grauman/temp/GraumanFergus_Hashing_chapterdraft.pdf)**: This paper focuses on learning binary hash codes for efficient large-scale image search. The paper is particularly useful for researchers working on image retrieval and large-scale computer vision tasks.

- **[Locality-Sensitive Hashing for Finding Nearest Neighbors](https://www.slaney.org/malcolm/yahoo/Slaney2008-LSHTutorial.pdf)**: This tutorial-style survey introduces Locality-Sensitive Hashing (LSH) as a method for efficient nearest neighbor search. It explains the principles behind LSH and demonstrates how it can be applied to large-scale datasets.

- **[Deep Learning for Hashing: A Survey](https://arxiv.org/pdf/1909.06046.pdf)**: This survey provides an in-depth overview of deep learning-based hashing techniques, which have become increasingly popular for large-scale retrieval tasks.

- **[Learning to Hash With Binary Deep Neural Networks: A Survey](https://www.sciencedirect.com/science/article/abs/pii/S016786552030208X)**: This survey focuses on binary deep neural networks and their use in learning to hash. It explores how these networks are trained to produce compact binary codes that can be used for efficient data retrieval in large-scale datasets.

### 🎓📚 Courses

Some university courses cover topics related to machine learning and efficient computing, with publicly available materials:

- **[Learning from Data](http://work.caltech.edu/telecourse.html)** by Yaser S. Abu-Mostafa et al.: A concise, intuitive introduction to the principles of supervised learning and generalization theory — foundational for understanding supervised hashing methods.

- **[Extreme Computing](http://www.inf.ed.ac.uk/teaching/courses/exc/index_17-18.html)** (University of Edinburgh): Focuses on the challenges and techniques involved in building and scaling systems for processing massive datasets.

- **[Text Technologies for Data Science](https://www.inf.ed.ac.uk/teaching/courses/tts/)** (University of Edinburgh): Covers processing, analysis, and modeling of textual data. Includes topics in text mining, NLP, and information retrieval — with relevance to similarity search and hashing.

- **[CS276: Information Retrieval](https://web.stanford.edu/class/cs276/)** (Stanford University): A comprehensive, foundational course covering algorithms for vector similarity search, ranking, indexing, and hashing.

#### 🧠 DeepLearning.AI Short Courses on Vector Search & ANN

- **[Vector Databases: from Embeddings to Applications](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/?utm_source=chatgpt.com)**: Learn how vector databases work (dense vs sparse search, multilingual embeddings, hybrid search) with real-world applications using Weaviate. *(~55 min)*

- **[Retrieval Optimization: from Tokenization to Vector Quantization](https://learn.deeplearning.ai/courses/retrieval-optimization-from-tokenization-to-vector-quantization/lesson/lpcaz/introduction?utm_source=chatgpt.com)**: Deep dive into ANN performance tuning — covering HNSW, product/scalar/binary quantization, and index compression techniques. Created with Qdrant.

- **[Building Applications with Vector Databases](https://www.deeplearning.ai/short-courses/building-applications-vector-databases/?utm_source=chatgpt.com)**: Hands-on course for building RAG, semantic search, hybrid retrieval, and anomaly detection apps using Pinecone.

- **[Retrieval Augmented Generation (RAG)](https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag/?utm_source=chatgpt.com)**: Explore architectures and implementation of RAG pipelines using vector indices, chunking, retrieval filtering, and prompt design.

- **[Knowledge Graphs for RAG](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/?utm_source=chatgpt.com)**: Learn how to connect vector embeddings with structured data using Neo4j to improve retrieval in multimodal and structured RAG systems.

- **[Prompt Compression and Query Optimization](https://www.deeplearning.ai/short-courses/prompt-compression-and-query-optimization/?utm_source=chatgpt.com)**: Covers retrieval latency reduction via query filtering, projection, re-ranking, and prompt shortening — with examples using MongoDB Atlas Vector Search.
 
### 📝📰  Blog Posts

Blog posts are a great way to keep up with cutting-edge research. Here are some of our favorites:

- **[ANN-Benchmarks](https://ann-benchmarks.com/index.html)**: A standard benchmarking platform for evaluating the performance of Approximate Nearest Neighbor (ANN) algorithms on a range of real-world and synthetic datasets. Continuously updated and widely cited, it provides reproducible results for comparison across indexing methods and libraries.
 
- **[Learning to Hash — Finding the Needle in the Haystack with AI](https://medium.com/@sean.j.moran/learning-to-hash-finding-the-needle-in-the-haystack-with-ai-24a15f85de0e)**: This blog post, authored by Sean Moran, provides a beginner-friendly introduction to the concept of learning to hash, focusing on how AI techniques like deep learning can improve approximate nearest neighbor search.

- **[Fast Near-Duplicate Image Search Using Locality-Sensitive Hashing](https://towardsdatascience.com/fast-near-duplicate-image-search-using-locality-sensitive-hashing-d4c16058efcb)**: This post explains how Locality-Sensitive Hashing (LSH) can be applied to find near-duplicate images efficiently. 

- **[An Introduction to Hashing in the Era of Machine Learning](https://blog.bradfieldcs.com/an-introduction-to-hashing-in-the-era-of-machine-learning-6039394549b0)**: This blog post gives an overview of hashing techniques, specifically in the context of modern machine learning applications. 

- **[Locality-Sensitive Hashing: Reducing Data Dimensionality](https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134)**: This article introduces Locality-Sensitive Hashing (LSH) as a method for reducing the dimensionality of high-dimensional data while preserving similarity. 

- **[Efficient Similarity Search with Faiss](https://engineering.fb.com/2020/11/23/ai-research/faiss/)**: This blog post, from Facebook AI Research (FAIR), provides an in-depth explanation of Faiss, an open-source library for efficient similarity search.
  
- **[Johnson–Lindenstrauss Lemma](https://www.wikiwand.com/en/Johnson%E2%80%93Lindenstrauss_lemma)**: This resource describes the Johnson-Lindenstrauss Lemma, a mathematical result that provides a way to reduce the dimensionality of data while approximately preserving distances between points.
  
- **[LSH Ideas](http://rakaposhi.eas.asu.edu/s01-cse494-mailarchive/msg00054.html)**: This article offers ideas and insights about Locality-Sensitive Hashing (LSH), focusing on its conceptual foundation and potential applications.
  
- **[Introduction to Locality-Sensitive Hashing (Great Visualizations)](http://tylerneylon.com/a/lsh1/)**: This tutorial, rich with visual aids, provides an easy-to-follow introduction to Locality-Sensitive Hashing (LSH). 

- **[What is Locality-Sensitive Hashing?](https://www.quora.com/What-is-locality-sensitive-hashing)**: This Quora discussion explains LSH in simple terms. It covers the core principles of how LSH works and why it is useful for approximate nearest neighbor search.

### 🧩💾 Hashing Software Packages

#### 📦 Hashing Algorithms

- **[Deep Hashing Toolbox](https://github.com/thulab/DeepHash)**: An open-source implementation designed for learning to hash with deep neural networks. Useful for deep similarity search research.
  
- **[Rensa (beowolx) – High-performance MinHash](https://github.com/beowolx/rensa)**: A Rust-based MinHash implementation with Python bindings. Fast and memory-efficient for deduplication tasks.

- **[Deep Supervised Hashing (DSH)](https://github.com/yxtay/Deep-Supervised-Hashing)**: A PyTorch implementation of Deep Supervised Hashing, which learns compact binary codes using supervision for high retrieval performance.

- **[HashNet](https://github.com/thuml/HashNet)**: Implements HashNet, a deep hashing method that handles imbalanced data distributions and learns binary hash codes end-to-end.

#### 🏗️ Indexing / ANN Libraries

- **[Faiss (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)**: A powerful library by Facebook AI Research for efficient similarity search of dense vectors. Supports PQ, IVF, HNSW, and more.

- **[Annoy (Approximate Nearest Neighbors Oh Yeah)](https://github.com/spotify/annoy)**: A C++/Python library from Spotify for fast approximate nearest neighbor search. Optimized for read-heavy workloads.

- **[NMSLIB](https://github.com/nmslib/nmslib)**: A cross-platform library for similarity search in non-metric spaces. Frequently used in search and recommendation systems.

- **[HNSWlib](https://github.com/nmslib/hnswlib)**: Implements Hierarchical Navigable Small World (HNSW) graphs for fast and accurate ANN search.

- **[ScaNN (Scalable Nearest Neighbors)](https://github.com/google-research/google-research/tree/master/scann)**: Developed by Google Research, ScaNN is optimized for vector similarity search at production scale using quantization and reordering.

#### 🛠️ Vector Databases

- **[Milvus](https://milvus.io/)**: A production-ready open-source vector database for similarity search. Supports multiple ANN algorithms and distributed deployments.

- **[Weaviate](https://weaviate.io/)**: An open-source vector database with semantic search capabilities, supporting hybrid search, classification, and modules like CLIP and OpenAI.

- **[Qdrant](https://qdrant.tech/)**: A fast and scalable vector database written in Rust. Provides gRPC and REST APIs and supports filtering and payload-based search.

### 🧪📊 Benchmarking Tools and Leaderboards

#### 🧪 ANN-Benchmarks: Comparing Nearest Neighbor Libraries

**[ANN-Benchmarks](https://github.com/erikbern/ann-benchmarks)** is the standard benchmarking framework for evaluating Approximate Nearest Neighbor (ANN) algorithms on a wide range of datasets and distance metrics.

It includes:
- Dockerized runners for 30+ ANN libraries including FAISS, HNSWlib, NMSLIB, Annoy, ScaNN, Milvus, and more.
- Scripts to run and visualize benchmarking results.
- Precomputed datasets in HDF5 format for fair and reproducible evaluation.

📄 Related Paper: [Aumüller et al. (2019)](https://arxiv.org/abs/1807.05614)

#### 🗃️ Evaluated Libraries on ANN-Benchmarks
Some key evaluated libraries:
- [FAISS](https://github.com/facebookresearch/faiss)
- [HNSWlib](https://github.com/nmslib/hnswlib)
- [Annoy](https://github.com/spotify/annoy)
- [ScaNN](https://github.com/google-research/google-research/tree/master/scann)
- [NMSLIB](https://github.com/nmslib/nmslib)
- [Weaviate](https://github.com/weaviate/weaviate)
- [Milvus](https://github.com/milvus-io/milvus)
- [Qdrant](https://github.com/qdrant/qdrant)
- [Elastiknn](https://github.com/alexklibisz/elastiknn)
- [SPTAG (Microsoft)](https://github.com/microsoft/SPTAG)
- [DiskANN (Microsoft)](https://github.com/microsoft/diskann)
- [PyNNDescent](https://github.com/lmcinnes/pynndescent)
- [FLANN](https://github.com/flann-lib/flann)

Full list: [github.com/erikbern/ann-benchmarks#evaluated](https://github.com/erikbern/ann-benchmarks#evaluated)

#### 📥 Precomputed Benchmark Datasets
All datasets are split into train/test sets with ground truth for top-100 neighbors:

| Dataset      | Dim | Train/Test       | Distance  | Download |
|--------------|-----|------------------|-----------|----------|
| DEEP1B       | 96  | 9.9M / 10k        | Angular   | [HDF5](http://ann-benchmarks.com/deep-image-96-angular.hdf5) |
| Fashion-MNIST| 784 | 60k / 10k         | Euclidean | [HDF5](http://ann-benchmarks.com/fashion-mnist-784-euclidean.hdf5) |
| SIFT         | 128 | 1M / 10k          | Euclidean | [HDF5](http://ann-benchmarks.com/sift-128-euclidean.hdf5) |
| GIST         | 960 | 1M / 1k           | Euclidean | [HDF5](http://ann-benchmarks.com/gist-960-euclidean.hdf5) |
| NYTimes      | 256 | 290k / 10k        | Angular   | [HDF5](http://ann-benchmarks.com/nytimes-256-angular.hdf5) |
| GloVe (25–200d)| — | 1.18M / 10k      | Angular   | [Link](https://github.com/erikbern/ann-benchmarks#datasets) |
| Last.fm      | 65  | 292k / 50k        | Angular   | [HDF5](http://ann-benchmarks.com/lastfm-64-dot.hdf5) |
| COCO-I2I     | 512 | 113k / 10k        | Angular   | [HDF5](https://github.com/fabiocarrara/str-encoders/releases/download/v0.1.3/coco-i2i-512-angular.hdf5) |
| COCO-T2I     | 512 | 113k / 10k        | Angular   | [HDF5](https://github.com/fabiocarrara/str-encoders/releases/download/v0.1.3/coco-t2i-512-angular.hdf5) |

More: [ann-benchmarks.com](http://ann-benchmarks.com)

#### 🧠 Related Projects

- **[Billion-Scale ANN Leaderboard](https://big-ann-benchmarks.com/neurips23.html)**: Continuously updated leaderboard comparing the performance of various billion-scale approximate nearest neighbor methods across recall, latency, and memory tradeoffs.

### 📚📖 Books

Here are a few recommended books on large-scale machine learning:

- **[Mining of Massive Datasets](https://amzn.to/42PeRDM)**: *(affiliate link)* This classic book explores large-scale data mining techniques, including graph processing, clustering, recommendation, and Locality-Sensitive Hashing (LSH). It's a core resource for anyone working on scalable algorithms for big data.

- **[Introduction to Information Retrieval](https://amzn.to/3WHTNvo)**: *(affiliate link)* Authored by Manning, Raghavan, and Schütze, this book is essential reading for understanding search engines, indexing, relevance, and vector space models — including chapters on hashing for text retrieval.

- **[Efficient Processing of Deep Neural Networks](https://link.springer.com/book/10.1007/978-3-031-01766-7)**: *(affiliate link)* A practical and theoretical guide to optimizing deep neural networks for deployment. It covers model compression, quantization, and hashing, making it highly relevant for efficient deep hashing research.

- **[Similarity Search: The Metric Space Approach](https://amzn.to/46ZLVLV)** *(affiliate link)* by Zezula et al.: A foundational text on similarity search in metric spaces, offering deep insight into indexing and retrieval techniques that predate modern hashing but remain highly relevant.

- **[Foundations of Data Science](https://amzn.to/47gHAms)** *(affiliate link)* by Blum, Hopcroft, and Kannan: A mathematically rigorous treatment of data science topics, including high-dimensional geometry, random projections, and algorithms that underlie LSH and related hashing techniques.

- **[Deep Learning](https://amzn.to/47updLU)** *(affiliate link)* by Goodfellow, Bengio, and Courville: The definitive book on deep learning. While not specific to hashing, it provides the theoretical backbone for understanding the neural network architectures used in deep supervised hashing models.

### 🗃️📥 Pre-Processed Datasets for Download

- **[CIFAR-10 Gist Features (.mat)](https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=0)**: This dataset contains GIST features extracted from the CIFAR-10 dataset, a popular image classification benchmark.

- **[LabelMe Gist Features (.mat)](https://www.dropbox.com/s/dwixb9ry4zwvcp9/LabelMe_gist.mat?dl=0)**: A set of GIST features extracted from the LabelMe dataset, which includes a large collection of labeled images. 

- **[MNIST Pixel Features (.mat)](https://www.dropbox.com/s/x3j6ik6kvnw95h3/MNIST_gnd_release.mat?dl=0)**: This dataset contains pixel-level features extracted from the MNIST dataset, a benchmark for handwritten digit recognition. 

- **[SIFT 1M Features (.mat)](https://www.dropbox.com/s/29f6r7pqevfy2ck/sift1m.mat?dl=0)**: This dataset consists of SIFT (Scale-Invariant Feature Transform) descriptors for one million image patches, commonly used in image matching and retrieval tasks.

- **[20 Newsgroups (.mat)](https://www.dropbox.com/s/wql7m8wuvn9efhj/20Newsgroups.mat?dl=0)**: This dataset contains features extracted from the 20 Newsgroups text dataset, a collection of approximately 20,000 documents categorized into 20 different newsgroups.
  
- **[TDT2 (.mat)](https://www.dropbox.com/s/qasz8z3sr1pjqog/TDT2.mat?dl=0)**: This dataset includes features from the Topic Detection and Tracking (TDT2) dataset, designed for research on text retrieval and clustering. 

- **[BIGANN Dataset](http://corpus-texmex.irisa.fr/)**: The BIGANN dataset includes SIFT descriptors extracted from a large collection of images. It is widely used for benchmarking large-scale approximate nearest neighbor (ANN) search algorithms.

- **[Facebook SimSearchNet++](https://dl.fbaipublicfiles.com/billion-scale-ann-benchmarks/FB_ssnpp_database.u8bin)**: A large-scale dataset developed by Facebook for the SimSearchNet++ model, which is used to benchmark billion-scale similarity search algorithms in the context of AI and machine learning applications.

- **[Microsoft SPACEV-1B](https://github.com/microsoft/SPTAG/tree/master/datasets/SPACEV1B)**: This dataset from Microsoft includes one billion vectors for testing large-scale similarity search algorithms. It is a benchmark for efficient vector retrieval systems and helps evaluate ANN algorithms' performance.

- **[Yandex DEEP-1B](https://research.yandex.com/datasets/biganns)**: The DEEP-1B dataset from Yandex consists of one billion deep image descriptors for benchmarking approximate nearest neighbor search algorithms. It provides a challenging, large-scale benchmark for evaluating hashing and ANN methods.

- **[Yandex Text-to-Image-1B](https://research.yandex.com/datasets/biganns)**: A dataset that includes one billion text-to-image matching features, useful for evaluating and benchmarking similarity search techniques that bridge the gap between text and image modalities.

- **[Deep1B Dataset](https://github.com/facebookresearch/faiss/wiki/Indexing-1B-vectors)**: The Deep1B dataset contains one billion deep representations of images, widely used in large-scale similarity search benchmarks.

- **[DEEP-10M](https://research.yandex.com/datasets)**: A smaller variant of the DEEP-1B dataset, containing 10 million deep image descriptors.

- **[GLUE Benchmark](https://gluebenchmark.com/)**: The General Language Understanding Evaluation (GLUE) benchmark consists of a variety of natural language processing tasks that test a model's understanding of language. While not traditionally used for image hashing, it provides valuable challenges for text-based hashing techniques.

</details>

<style>
  :root{
    --bg:#ffffff;
    --card:#fff;
    --muted:#6b7280;
    --line:#e5e7eb;
    --shadow:0 1px 2px rgba(0,0,0,.06), 0 8px 24px rgba(0,0,0,.04);
    --brand:#1a73e8;
  }

  /* Non-sticky, with category dividers */
  html { scroll-behavior: smooth; }
  .toolbar, .jumpbar, .cat-divider { position: static !important; }

  .toolbar{
    z-index:auto; background:#fff; border:1px solid var(--line);
    border-radius:12px; padding:10px 12px; margin:8px 0 12px;
    display:flex; align-items:center; gap:12px; box-shadow:var(--shadow);
    max-width:100%; box-sizing:border-box;
  }
  .toolbar .left{ flex:1 1 auto; min-width:0; }

  .search{
    display:flex; align-items:center; gap:.6rem; flex-wrap:wrap;
    width:100%; max-width:100%;
  }
  .search label{ font-weight:700; font-size:.85rem; }
  .search input{
    flex:1 1 240px;       /* grow within the card, shrink if needed */
    min-width:0;          /* allow shrinking without overflow */
    width:auto;           /* no fixed width */
    padding:.5rem .7rem;
    border:1px solid #cbd5e1; border-radius:8px;
    font-size:.95rem; background-color:#f8fafc;
    box-sizing:border-box;
  }
  .search input:focus{ outline:none; border-color:var(--brand); box-shadow:0 0 0 2px rgba(26,115,232,.18); }
  .search button{
    padding:.5rem .7rem; font-size:.85rem;
    border:1px solid #cbd5e1; border-radius:8px; background:#f8fafc; cursor:pointer;
    flex:0 0 auto;
  }
  .search button:hover{ background:#eef2f7; }
  .small{ color:var(--muted); font-size:.9em; }

  .jumpbar{
    display:flex; flex-wrap:wrap; gap:8px; padding:8px 0 12px; margin:0 0 8px;
    background:#fff;
  }
  .jumpbar a{
    display:inline-block; padding:.25rem .6rem;
    border:1px solid var(--line); border-radius:999px;
    text-decoration:none; color:#0f172a; font-size:.85rem;
  }
  .jumpbar a:hover{ background:#f3f4f6; }

  .cards{
    display:grid; gap:14px;
    grid-template-columns: repeat(auto-fill, minmax(280px,1fr));
  }

  .cat-divider{
    grid-column:1 / -1;
    font-size:1.05rem; font-weight:800; letter-spacing:.02em;
    margin:24px 0 6px; padding-top:12px;
    scroll-margin-top:24px;
  }
  .cat-divider::after{
    content:"";
    display:block; height:1px; margin-top:6px;
    background:repeating-linear-gradient(
      90deg, var(--line), var(--line) 8px, transparent 8px, transparent 16px
    );
  }

  .card{
    border:1px solid var(--line); border-radius:14px; background:var(--card);
    padding:14px; box-shadow:var(--shadow); transition:transform .06s ease;
    display:flex; flex-direction:column; gap:6px; min-width:0; cursor:pointer;
  }
  .card * { min-width:0; }
  .card:hover{ transform:translateY(-1px); }
  .meta{ display:flex; align-items:center; gap:8px; margin-bottom:2px; color:var(--muted); font-size:.85rem; flex-wrap:wrap; }
  .favicon{ width:16px; height:16px; border-radius:4px; background:#f3f4f6; }

  .title{
    font-weight:700; line-height:1.25; margin:2px 0 2px;
    display:-webkit-box; -webkit-box-orient:vertical; -webkit-line-clamp:2;
    overflow:hidden; word-break:break-word; overflow-wrap:anywhere;
  }
  .title a{ text-decoration:none; color:#0f172a; }
  .title a:hover{ text-decoration:underline; }

  .desc{
    color:#374151; font-size:.95rem; line-height:1.45;
    display:-webkit-box; -webkit-box-orient:vertical; -webkit-line-clamp:4;
    overflow:hidden; word-break:break-word; overflow-wrap:anywhere;
  }

  .badges{ display:flex; align-items:center; gap:6px; margin-top:6px; flex-wrap:wrap; }
  .badge{
    font-size:.75rem; border:1px solid var(--line); color:#0f172a; padding:.2rem .45rem;
    border-radius:999px; background:#f7f7fb; cursor:pointer;
  }

  .empty{ color:#6b7280; text-align:center; padding:24px 8px; }

  .dataTables_wrapper{ width:100%; overflow-x:hidden; }
  #resources-table{ width:100%; border-collapse:collapse; table-layout:auto; }
  #resources-table td{ white-space: normal !important; word-break: break-word; overflow-wrap:anywhere; vertical-align: top; }
  #resources-table th{ white-space: nowrap !important; overflow: hidden; text-overflow: ellipsis; vertical-align: middle; }
  .dataTables_filter{ display:none !important; }

  #loading{
    position:fixed; top:50%; left:50%; transform:translate(-50%,-50%);
    font-size:1.05em; text-align:center; z-index:1000;
    background:white; padding:.8em 1.2em; border:1px solid #ccc; border-radius:8px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
  }

  @media (max-width: 640px){
    .toolbar{ border-radius:10px; }
    .desc{ -webkit-line-clamp: 6; }
  }
</style>

<link rel="stylesheet" href="{{ '/assets/vendor/datatables-1.13.6.min.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/vendor/dataTables.responsive-2.5.0.min.css' | relative_url }}">
<script src="{{ '/assets/vendor/jquery-3.6.0.min.js' | relative_url }}" defer></script>
<script src="{{ '/assets/vendor/datatables-1.13.6.min.js' | relative_url }}" defer></script>
<script src="{{ '/assets/vendor/dataTables.responsive-2.5.0.min.js' | relative_url }}" defer></script>

<script>
(function(){
  function waitForDT(cb, tries = 80){
    if (window.jQuery && jQuery.fn && jQuery.fn.dataTable) return cb();
    if (tries <= 0) return cb(new Error('DataTables not loaded'));
    setTimeout(() => waitForDT(cb, tries - 1), 100);
  }
  function ready(fn){
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn, { once:true });
    } else { fn(); }
  }

  function readHashQuery(){
    const raw = window.location.hash ? window.location.hash.slice(1) : '';
    if (!raw) return '';
    try { return decodeURIComponent(raw.replace(/\+/g,' ')); } catch { return raw; }
  }
  function setHash(q){
    if (q && q.trim().length) history.replaceState(null, '', '#' + encodeURIComponent(q.trim()));
    else history.replaceState(null, '', location.pathname + location.search);
  }

  function textContentTrim(node){ return (node ? node.textContent : '').replace(/\s+/g,' ').trim(); }
  function escapeHtml(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;'); }
  function domainFromUrl(u){ try{ return new URL(u, location.origin).hostname; } catch(e){ return ''; } }
  function faviconForDomain(d){ return d ? 'https://www.google.com/s2/favicons?domain='+encodeURIComponent(d)+'&sz=32' : ''; }
  function debounce(fn, ms=120){ let t; return (...a)=>{ clearTimeout(t); t=setTimeout(()=>fn(...a), ms); }; }
  function slugify(s){ return (s||'uncategorised').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/(^-|-$)/g,''); }

  const loadingEl = document.getElementById('loading');
  const toolbarEl = document.getElementById('resToolbar');
  const inputEl   = document.getElementById('resSearch');
  const resetEl   = document.getElementById('resetResSearch');
  const countEl   = document.getElementById('resVisibleCount');
  const gridEl    = document.getElementById('cardsGrid');
  const emptyEl   = document.getElementById('emptyState');
  const contentEl = document.getElementById('resourcesContent');
  const jumpBarEl = document.getElementById('jumpBar');

  let datatable;

  function updateVisibleCount(){
    if (!datatable || !countEl) return;
    countEl.textContent = datatable.rows({ filter:'applied' }).count() + ' resources';
  }

  function applyFilter(q){
    if(!datatable) return;
    const query=(q||'').trim();
    if(inputEl) inputEl.value=query;
    datatable.search(query, false, true, true).draw(false);
    setHash(query);
    updateVisibleCount();
  }

  function withRenderedDetails(fn){
    if(!contentEl)return fn();
    const wasHidden = contentEl.hasAttribute('hidden');
    const prevDisplay = contentEl.style.display;
    const prevPos = contentEl.style.position;
    const prevLeft = contentEl.style.left;
    if (wasHidden) contentEl.removeAttribute('hidden');
    contentEl.style.display='block'; contentEl.style.position='absolute'; contentEl.style.left='-99999px';
    const out = fn();
    if (wasHidden) contentEl.setAttribute('hidden','');
    contentEl.style.display = prevDisplay || '';
    contentEl.style.position = prevPos || '';
    contentEl.style.left = prevLeft || '';
    return out;
  }

  function scrapeResources(){
    return withRenderedDetails(()=>{
      const rows = [];
      const walker = document.createTreeWalker(contentEl, NodeFilter.SHOW_ELEMENT, null);
      let currCat = '', currSub = '';

      while (walker.nextNode()){
        const el = walker.currentNode;

        if (/^H2$/i.test(el.tagName)) {
          currCat = textContentTrim(el).replace(/^#+\s*/,'');
          currSub = '';
        } else if (/^H3$/i.test(el.tagName)) {
          currSub = textContentTrim(el).replace(/^#+\s*/,'');
        } else if (/^LI$/i.test(el.tagName)) {
          const a = el.querySelector('a[href]');
          if (!a) continue;
          const url = a.getAttribute('href') || '';
          const title = textContentTrim(a) || '(untitled)';

          let full = textContentTrim(el);
          try{
            full = full.replace(new RegExp('^\\*?\\*?\\s*' + title.replace(/[.*+?^${}()|[\]\\]/g,'\\$&') + '\\s*:?\\s*','i'), '');
          }catch{}
          const desc = full;

          const domain = domainFromUrl(url);
          const titleHTML = `<a href="${url}" target="_blank" rel="noopener noreferrer">${escapeHtml(title)}</a>`;
          const descHTML  = desc ? escapeHtml(desc) : '';
          const raw = [title, currCat, currSub, desc, url, domain].join(' ').toLowerCase();

          rows.push([ titleHTML, currCat, currSub, descHTML, raw, url, domain ]);
        }
      }
      return rows;
    });
  }

  function renderCards(){
    if (!datatable) return;
    const rows = datatable.rows({ filter:'applied' }).data().toArray();
    gridEl.innerHTML = '';

    if (!rows.length){
      gridEl.style.display='none';
      emptyEl.style.display='';
      if (jumpBarEl) jumpBarEl.style.display='none';
      updateVisibleCount();
      return;
    }
    emptyEl.style.display='none';
    gridEl.style.display='grid';

    let lastCat = null;
    const catsForJump = [];

    rows.forEach(r => {
      const titleHTML = r[0];
      const cat       = r[1] || 'Uncategorised';
      const subcat    = r[2] || '';
      const descHTML  = r[3];
      const url       = r[5] || '';
      const domain    = r[6] || domainFromUrl(url);

      if (cat !== lastCat){
        const id = 'cat-' + slugify(cat);
        const divider = document.createElement('h2');
        divider.className = 'cat-divider';
        divider.id = id;
        divider.textContent = cat;
        divider.addEventListener('click', ()=> applyFilter(cat));
        gridEl.appendChild(divider);
        catsForJump.push({ cat, id });
        lastCat = cat;
      }

      const card = document.createElement('article');
      card.className = 'card';
      card.setAttribute('data-cat',cat);
      card.setAttribute('data-sub',subcat);
      card.setAttribute('data-domain',domain||'');

      card.innerHTML = `
        <div class="meta">
          <img class="favicon" src="${faviconForDomain(domain)}" alt="" loading="lazy">
          <span class="meta-domain" title="Filter by site">${domain || 'link'}</span>
          ${subcat ? '<span>•</span><button class="badge badge-sub" title="Filter by subcategory">'+escapeHtml(subcat)+'</button>' : ''}
        </div>
        <h3 class="title">${titleHTML}</h3>
        <div class="desc">${descHTML}</div>
        <div class="badges">
          ${subcat ? '<button class="badge badge-sub" title="Filter by subcategory">'+escapeHtml(subcat)+'</button>' : ''}
          <button class="badge badge-cat" title="Filter by category">${escapeHtml(cat)}</button>
        </div>
      `;

      card.addEventListener('click',(e)=>{
        if(e.target.closest('a')) return;
        const subBtn=e.target.closest('.badge-sub');
        const catBtn=e.target.closest('.badge-cat');
        const domEl=e.target.closest('.meta-domain');
        if(subBtn){ applyFilter(subcat); return; }
        if(catBtn){ applyFilter(cat); return; }
        if(domEl){ applyFilter(domain); return; }
        if(url && (e.metaKey||e.ctrlKey)){ window.open(url,'_blank','noopener'); return; }
        applyFilter(subcat || cat || domain || '');
      });

      card.setAttribute('role','group'); card.tabIndex=0;
      card.addEventListener('keydown',(e)=>{
        if(e.key==='Enter'){ applyFilter(subcat || cat || domain || ''); }
        else if((e.key==='o'||e.key==='O') && url){ window.open(url,'_blank','noopener'); }
      });

      gridEl.appendChild(card);
    });

    if (jumpBarEl){
      if (catsForJump.length){
        jumpBarEl.innerHTML = catsForJump.map(c=>`<a href="#${c.id}">${escapeHtml(c.cat)}</a>`).join('');
        jumpBarEl.style.display = '';
      } else {
        jumpBarEl.style.display = 'none';
      }
    }

    updateVisibleCount();
  }

  function start(err){
    try{
      if (err || !window.jQuery || !jQuery.fn || !jQuery.fn.dataTable) {
        if (loadingEl) loadingEl.innerHTML = '<p style="color:#b00020">Failed to load: DataTables missing.</p>';
        return;
      }

      const initialQuery = readHashQuery();
      if (inputEl && initialQuery) inputEl.value = initialQuery;

      const rows = scrapeResources();

      const dt = jQuery('#resources-table').DataTable({
        data: rows,
        columns: [
          { title: "Title"      },
          { title: "Category"   },
          { title: "Section"    },
          { title: "Description"},
          { title: "raw"        },
          { title: "url"        },
          { title: "domain"     }
        ],
        responsive: { details: false },
        autoWidth: false,
        paging: false,
        searching: true,
        order: [[1,'asc'], [2,'asc'], [0,'asc']],
        columnDefs: [
          { targets: [4], visible: false, searchable: true },
          { targets: [5,6], visible: false, searchable: false }
        ],
        initComplete: function(){
          datatable = this.api();

          if (loadingEl) loadingEl.style.display='none';
          toolbarEl.style.display='';
          gridEl.style.display='grid';

          if (initialQuery) datatable.search(initialQuery, false, true, true).draw();

          renderCards();
          datatable.on('draw', renderCards);

          const apply = debounce(() => {
            const q = inputEl ? (inputEl.value || '') : '';
            datatable.search(q, false, true, true).draw(false);
            setHash(q);
          }, 120);

          inputEl.addEventListener('input', apply);
          inputEl.addEventListener('keydown', (e)=>{ if (e.key==='Enter'){ e.preventDefault(); apply(); }});
          resetEl.addEventListener('click', () => {
            inputEl.value=''; datatable.search('', false, true, true).draw(false); setHash(''); inputEl.focus();
          });
          window.addEventListener('hashchange', () => {
            const q = readHashQuery();
            inputEl.value = q;
            datatable.search(q, false, true, true).draw(false);
          });

          document.addEventListener('keydown', (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
              e.preventDefault(); inputEl.focus();
            } else if (e.key === 'Escape') {
              inputEl.value=''; datatable.search('', false, true, true).draw(false); setHash('');
            }
          });

          setTimeout(() => datatable.columns.adjust().draw(false), 60);
          updateVisibleCount();
        }
      });

      if (rows.length === 0){
        gridEl.style.display = 'none';
        if (loadingEl) loadingEl.innerHTML = '<p>No resources detected to index.</p>';
      }

    } catch (e){
      console.error(e);
      if (loadingEl) loadingEl.innerHTML = '<p style="color:#b00020">Failed to load resources.</p>';
    }
  }

  ready(() => waitForDT(start));
})();
</script>

<p style="margin-top:2rem; color:#6b7280; font-size:.95em;">
  Please, feel free to submit a <a href="contributing.html">web form</a> to add more links to this page.
  As an Amazon Associate, this site earns from qualifying purchases. Some links may be affiliate (no extra cost).
</p>
