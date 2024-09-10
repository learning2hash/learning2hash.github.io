---
layout: default
title: Resources
---
# Resources on Machine Learning for Hashing

### Conferences and Workshops

- [Practical Vector Search Challenge 2023](https://big-ann-benchmarks.com/neurips23.html): A competition focused on developing indexing data structures and search algorithms for vector search problems.
- [Billion-Scale Approximate Nearest Neighbor Search Challenge: NeurIPS'21 Competition Track](http://big-ann-benchmarks.com/index.html#call): A large-scale challenge to improve approximate nearest neighbor search methods.
- [Compact and Efficient Feature Representation and Learning in Computer Vision, ICCV 2019](http://www.ee.oulu.fi/~lili/CEFRLatICCV2019.html): A workshop focused on compact feature learning, including binary hashing methods.
- [International Conference on Similarity Search and Applications](http://www.sisap.org/2020/): A conference dedicated to similarity search techniques and applications.
- [Joint Workshop on Efficient Deep Learning in Computer Vision](https://workshop-edlcv.github.io/): Co-located with CVPR 2020, focusing on efficient deep learning techniques.

### Introductory Video Material

For a thorough introduction to learning to hash, check out [Dr. Wu-Jun Li's tutorial slides](https://cs.nju.edu.cn/lwj/slides/L2H.pdf).

Additionally, [Dr. Victor Lavrenko](https://www.youtube.com/user/victorlavrenko) has two great videos explaining the basics of locality-sensitive hashing (LSH):
- [Intro to LSH - Part 1](https://www.youtube.com/watch?v=Arni-zkqMBA)
- [Intro to LSH - Part 2](https://www.youtube.com/watch?v=dgH0NP8Qxa8)

<p><iframe width="560" height="315" src="https://www.youtube.com/embed/Arni-zkqMBA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>
<p><iframe width="560" height="315" src="https://www.youtube.com/embed/dgH0NP8Qxa8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

Here’s another valuable resource from the 2017 Rice Machine Learning Workshop: *Hashing Algorithms for Large-Scale Machine Learning*:

<p><iframe width="560" height="315" src="https://www.youtube.com/embed/tQ0OJXowLJA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></p>

### Survey Papers

For a deeper dive, these survey papers are excellent resources:

- [Learning to Hash for Indexing Big Data - A Survey](https://arxiv.org/pdf/1509.05472.pdf)
- [A Survey on Learning to Hash](https://arxiv.org/pdf/1606.00185.pdf)
- [Learning Binary Hash Codes for Large-Scale Image Search](http://www.cs.utexas.edu/~grauman/temp/GraumanFergus_Hashing_chapterdraft.pdf)
- [Locality-Sensitive Hashing for Finding Nearest Neighbors](https://www.slaney.org/malcolm/yahoo/Slaney2008-LSHTutorial.pdf)

### Pre-Processed Datasets for Download

- [CIFAR-10 Gist Features (.mat)](https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=0)
- [LabelMe Gist Features (.mat)](https://www.dropbox.com/s/dwixb9ry4zwvcp9/LabelMe_gist.mat?dl=0)
- [MNIST Pixel Features (.mat)](https://www.dropbox.com/s/x3j6ik6kvnw95h3/MNIST_gnd_release.mat?dl=0)
- [SIFT 1M Features (.mat)](https://www.dropbox.com/s/29f6r7pqevfy2ck/sift1m.mat?dl=0)
- [20 Newsgroups (.mat)](https://www.dropbox.com/s/wql7m8wuvn9efhj/20Newsgroups.mat?dl=0)
- [TDT2 (.mat)](https://www.dropbox.com/s/qasz8z3sr1pjqog/TDT2.mat?dl=0)
- [BIGANN Dataset](http://corpus-texmex.irisa.fr/): SIFT descriptors applied to images from a large dataset.
- [Facebook SimSearchNet++](https://dl.fbaipublicfiles.com/billion-scale-ann-benchmarks/FB_ssnpp_database.u8bin)
- [Microsoft SPACEV-1B](https://github.com/microsoft/SPTAG/tree/master/datasets/SPACEV1B)
- [Yandex DEEP-1B](https://research.yandex.com/datasets/biganns)
- [Yandex Text-to-Image-1B](https://research.yandex.com/datasets/biganns)
- [Deep1B Dataset](https://github.com/facebookresearch/faiss/wiki/Indexing-1B-vectors): A billion-scale dataset used for benchmarking similarity search algorithms&#8203;:contentReference[oaicite:0]{index=0}.

### Courses

Some university courses cover topics related to machine learning and efficient computing, with publicly available materials:

- [Extreme Computing](http://www.inf.ed.ac.uk/teaching/courses/exc/index_17-18.html) at the University of Edinburgh
- [Text Technologies for Data Science](https://www.inf.ed.ac.uk/teaching/courses/tts/) at the University of Edinburgh
- [CS276: Information Retrieval](https://web.stanford.edu/class/cs276/) at Stanford University: This course covers topics on vector similarity search and hashing&#8203;:contentReference[oaicite:1]{index=1}.

### Blog Posts

Blog posts are a great way to keep up with cutting-edge research. Here are some of our favorites:

- [Learning to Hash — Finding the Needle in the Haystack with AI](https://medium.com/@sean.j.moran/learning-to-hash-finding-the-needle-in-the-haystack-with-ai-24a15f85de0e)
- [Fast Near-Duplicate Image Search Using Locality-Sensitive Hashing](https://towardsdatascience.com/fast-near-duplicate-image-search-using-locality-sensitive-hashing-d4c16058efcb)
- [An Introduction to Hashing in the Era of Machine Learning](https://blog.bradfieldcs.com/an-introduction-to-hashing-in-the-era-of-machine-learning-6039394549b0)
- [Locality-Sensitive Hashing: Reducing Data Dimensionality](https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134)
- [Efficient Similarity Search with Faiss](https://engineering.fb.com/2020/11/23/ai-research/faiss/): A comprehensive explanation of Faiss, its development, and how it handles similarity search at scale&#8203;:contentReference[oaicite:2]{index=2}.
- [Johnson–Lindenstrauss Lemma](https://www.wikiwand.com/en/Johnson%E2%80%93Lindenstrauss_lemma)
- [LSH Ideas](http://rakaposhi.eas.asu.edu/s01-cse494-mailarchive/msg00054.html)
- [Introduction to Locality-Sensitive Hashing (Great Visualizations)](http://tylerneylon.com/a/lsh1/)
- [What is Locality-Sensitive Hashing?](https://www.quora.com/What-is-locality-sensitive-hashing)

### Hashing Software Packages

- [Faiss (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss): A powerful library for efficient similarity search and clustering of dense vectors, used for large-scale datasets&#8203;:contentReference[oaicite:3]{index=3}&#8203;:contentReference[oaicite:4]{index=4}.
- [Annoy (Approximate Nearest Neighbors Oh Yeah)](https://github.com/spotify/annoy): Developed by Spotify, this C++ library is designed for fast approximate nearest neighbor search in high-dimensional spaces&#8203;:contentReference[oaicite:5]{index=5}.
- [Deep Hashing Toolbox](https://github.com/thulab/DeepHash)

### Books

Here are a few recommended books on large-scale machine learning:

- [Mining of Massive Datasets](http://www.mmds.org/): Covers large-scale data mining topics, including a detailed section on LSH.
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval-book.html): A classic textbook on information retrieval, featuring comprehensive coverage of data indexing and retrieval techniques.
- [Efficient Processing of Deep Neural Networks](https://link.springer.com/book/10.2200/S01004ED1V01Y202004CAC050): A detailed exploration of techniques for processing deep neural networks efficiently&#8203;:contentReference[oaicite:6]{index=6}&#8203;:contentReference[oaicite:7]{index=7}.

Feel free to contribute more resources by submitting a pull request.
