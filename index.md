# Awesome Papers on Learning to Hash

<iframe src="https://ghbtns.com/github-btn.html?user=learning2hash&repo=learning2hash.github.io&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>

### 🏷 Browse Papers by Tag

Explore the latest research by browsing papers categorized by tags. Select a tag below to dive deeper into specific topics within the field of learning to hash:

{% assign rawtags = Array.new %}
{% for publication in site.publications %}
  {% assign ttags = publication.tags  %}  
  {% assign rawtags = rawtags | concat: ttags %}  
{% endfor %}
{% assign rawtags = rawtags | uniq | sort %}
{% for tag in rawtags %}<tag><a href="/tags.html#{{ tag }}">{{ tag }}</a></tag> {% endfor %}

### Understanding Learning to Hash

This website is a resource for researchers looking to explore, share, and discover recent advancements in the field of learning to hash. It serves as a *living literature review*, allowing readers to navigate models organized by a [taxonomy](\base-taxonomy) based on key properties. Anyone can contribute to this growing resource by submitting new papers via a simple form. For details, see the [*Contributing* section](contributing.html).

To start, visit the ["All Papers"](https://learning2hash.github.io/papers.html) section from the right-hand menu and browse the full list of contributions.

### Background: What is Learning to Hash?

At its core, *[Nearest Neighbour Search](https://en.wikipedia.org/wiki/Nearest_neighbor_search)* is the task of finding the most similar data points to a given query in a large dataset. This operation is fundamental to many fields, from Bioinformatics to Natural Language Processing (NLP) and Computer Vision.

Some notable applications include:

- **[Scalable Source Code Search](https://arxiv.org/abs/2111.04473)**: Using MinHash to enable code-to-code recommendations across large-scale source code repositories.
- **[Efficient Transformers](https://openreview.net/pdf?id=rkgNKkHtvB)**: Locality Sensitive Hashing (LSH) helps make large Transformer models more efficient, cutting down training costs.
- **[Social Media Event Tracking](https://www.aclweb.org/anthology/P14-5007)**: A system for detecting and tracking interesting events on social media in real time using LSH.
- **[Earthquake Detection](https://dawn.cs.stanford.edu/2018/09/05/quake/)**: Comparing time series of seismic activity to detect earthquakes using LSH.
- **[Fraud Detection at Uber](https://eng.uber.com/lsh/)**: Uber employs LSH to identify suspicious taxi rides based on spatial data.
- **[Audio Fingerprinting](https://santhoshhari.github.io/Locality-Sensitive-Hashing/)**: Matching a snippet of audio to a large database (think Shazam!) using learning-to-hash methods.
- **[Genomic Research](https://www.ncbi.nlm.nih.gov/pubmed/26006009)**: Biologists use LSH to assemble genomes and find genes with similar expression profiles.
- **[Image Retrieval](https://ai.google/research/pubs/pub34634)**: Google applies LSH along with [PageRank](https://en.wikipedia.org/wiki/PageRank) to index massive collections of images.
- **[Malware Detection](https://media.kaspersky.com/en/enterprise-security/Kaspersky-Lab-Whitepaper-Machine-Learning.pdf)**: Hash learning models help antivirus software quickly match code snippets to known viruses.

### How Learning to Hash Works

Learning to hash is about creating binary hash codes that capture the similarity between data points. These hash codes are then used to index data into hash tables, making it possible to quickly find similar items based on the query. 

For example, in the image below, the system generates a hashcode for an image of a tiger and compares it only to data points within the same hash table bucket. This method dramatically reduces the number of comparisons needed, making search faster than brute-force approaches. Although there’s a small trade-off in accuracy, the speed benefits are substantial in practice.

![Locality Sensitive Hashing (LSH)](/public/media/hashing.png?raw=true "Locality Sensitive Hashing (LSH)")

*Image from the [PhD thesis of Sean Moran](https://learning2hash.github.io/cite.html).*

For more detailed introductory material, visit our [*Resources*](resources.html) page.

### Contribute to the Growing Research

The field of learning to hash is rapidly evolving, and this website aims to stay current by inviting contributions from researchers. If you come across new work in this area, you can easily add it by creating a markdown file and submitting a pull request through our GitHub page. For full instructions, visit the [*Contributing* section](contributing.html).

Copyright © [Sean Moran](https://sjmoran.github.io/) 2024. All opinions expressed here are my own.
