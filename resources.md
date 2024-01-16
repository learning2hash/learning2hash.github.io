---
layout: default
title: Resources on Machine Learning for Hashing
comments: true
---
<iframe src="https://ghbtns.com/github-btn.html?user=learning2hash&repo=learning2hash.github.io&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>

### Conferences and Workshops

* [Practical Vector Search Challenge 2023](https://big-ann-benchmarks.com/neurips23.html)
* [Billion-Scale Approximate Nearest Neighbor Search Challenge: NeurIPS'21 competition track](http://big-ann-benchmarks.com/index.html#call)
* [Compact and Efficient Feature Representation and Learning in Computer Vision, ICCV 2019](http://www.ee.oulu.fi/~lili/CEFRLatICCV2019.html): a workshop dedicated to compact feature learning, including binary hashing methods. 
* [International Conference on Similarity Search and Applications](http://www.sisap.org/2020/): a conference dedicated to similarity search
* [Joint Workshop on Efficient Deep Learning in Computer Vision](https://workshop-edlcv.github.io/): co-located with the CVPR 2020 conference

### Introductory Video Material

Please also see the excellent [tutorial slides](https://cs.nju.edu.cn/lwj/slides/L2H.pdf) of [Dr. Wu-Jun Li](https://cs.nju.edu.cn/lwj/) for a nice introduction to the field.

[Dr Victor Lavrenko](https://www.youtube.com/user/victorlavrenko) has two excellent youtube videos [here](https://www.youtube.com/watch?v=Arni-zkqMBA) and [here](https://www.youtube.com/watch?v=dgH0NP8Qxa8), describing the basics of locality sensitive hashing (LSH). These are ideal for those just entering the field or curious how to apply the method to their problem domain.

<p><iframe width="560" height="315" src="https://www.youtube.com/embed/Arni-zkqMBA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/dgH0NP8Qxa8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

The 2017 Rice Machine Learning Workshop: Hashing Algorithms for Large-Scale Machine Learning:

<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/tQ0OJXowLJA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

### Survey Papers

The reader is encouraged to further explore the following survey publications:

* [Learning to Hash for Indexing Big Data - A Survey](https://arxiv.org/pdf/1509.05472.pdf)
* [A Survey on Learning to Hash](https://arxiv.org/pdf/1606.00185.pdf)
* [Learning Binary Hash Codes for Large-Scale Image Search](http://www.cs.utexas.edu/~grauman/temp/GraumanFergus_Hashing_chapterdraft.pdf)
* [Locality-Sensitive Hashing for Finding Nearest Neighbors](https://www.slaney.org/malcolm/yahoo/Slaney2008-LSHTutorial.pdf)

### Pre-Processed Datasets for Download

* [CIFAR-10 Gist Features (.mat format)](https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=0)
* [LabelMe Gist Features (.mat format)](https://www.dropbox.com/s/dwixb9ry4zwvcp9/LabelMe_gist.mat?dl=0)
* [MNIST Pixel Features (.mat format)](https://www.dropbox.com/s/x3j6ik6kvnw95h3/MNIST_gnd_release.mat?dl=0)
* [SIFT 1M Features (.mat format)](https://www.dropbox.com/s/29f6r7pqevfy2ck/sift1m.mat?dl=0)
* [20 Newsgroups (.mat format)](https://www.dropbox.com/s/wql7m8wuvn9efhj/20Newsgroups.mat?dl=0)
* [TDT2 (.mat format)](https://www.dropbox.com/s/qasz8z3sr1pjqog/TDT2.mat?dl=0)
* [BIGANN](http://corpus-texmex.irisa.fr/) consists of SIFT descriptors applied to images from extracted from a large image dataset.
* [Facebook SimSearchNet++](https://dl.fbaipublicfiles.com/billion-scale-ann-benchmarks/FB_ssnpp_database.u8bin)
* [Microsoft SPACEV-1B](https://github.com/microsoft/SPTAG/tree/master/datasets/SPACEV1B)
* [Yandex DEEP-1B](https://research.yandex.com/datasets/biganns)
* [Yandex Text-to-Image-1B](https://research.yandex.com/datasets/biganns)

### Courses
A few university courses are been taught covering aspects of machine of efficient computing. Below there are a few that have publicly available material:

* [Extreme Computing](http://www.inf.ed.ac.uk/teaching/courses/exc/index_17-18.html) in University of Edinburgh.
* [Text Technologies for Data Science](https://www.inf.ed.ac.uk/teaching/courses/tts/) in University of Edinburgh.

### Blog Posts

Blog posts provide a great way to learn about cutting edge research and ideas. Here are a few of our favourites:

* [Learning to Hash — Finding the Needle in the HayStack with AI](https://medium.com/@sean.j.moran/learning-to-hash-finding-the-needle-in-the-haystack-with-ai-24a15f85de0e)
* [Fast Near-Duplicate Image Search using Locality Sensitive Hashing](https://towardsdatascience.com/fast-near-duplicate-image-search-using-locality-sensitive-hashing-d4c16058efcb)
* [An Introduction to Hashing in the Era of Machine Learning](https://blog.bradfieldcs.com/an-introduction-to-hashing-in-the-era-of-machine-learning-6039394549b0)
* [Locality Sensitive Hashing: An effective way of reducing the dimensionality of your data](https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134)
* [Johnson–Lindenstrauss lemma](https://www.wikiwand.com/en/Johnson%E2%80%93Lindenstrauss_lemma)
* [LSH Ideas](http://rakaposhi.eas.asu.edu/s01-cse494-mailarchive/msg00054.html)
* [Introduction to Locality-Sensitive Hashing (nice visualisations!)](http://tylerneylon.com/a/lsh1/)
* [What is locality-sensitive hashing?](https://www.quora.com/What-is-locality-sensitive-hashing)

### Hashing Software Packages

* [Deep Hashing Toolbox](https://github.com/thulab/DeepHash)

### Books

Some favourite books on the general topic of large-scale machine learning:

* [Mining of Massive Datasets](http://www.mmds.org/): great content throughout on all sorts of large-scale data mining topics from Hadoop to Google AdWords. Book includes a detailed treatment of LSH.

* [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval-book.html): arguably a classic book on information retrieval basics, very well-written, with a comprehensive overview of data indexing and retrieval.

Please, feel free to submit a pull request to adding more links in this page.
