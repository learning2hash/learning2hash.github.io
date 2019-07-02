---
layout: default
title: Resources on Machine Learning for Hashing
comments: true
---

### Learning-to-Hash Survey Paper

The full literature survey that accompanies this website is available [as a research paper](http://seanjmoran.com/pdfs/hashing_review.pdf) currently under submission to a peer-reviewed journal. Full citation information will appear here in due course. In the meantime please feel free to cite the following thesis upon which the review is based:

<pre>
@phdthesis{Moran16,
  author       = {Sean Moran}, 
  title        = {Learning to hash for large-scale image retrieval},
  school       = {University of Edinburgh},
  year         = 2016,
}
</pre>

### Presentations and Relevant Introductory Material

Please also see the excellent [tutorial slides](https://cs.nju.edu.cn/lwj/slides/L2H.pdf) of [Dr. Wu-Jun Li](https://cs.nju.edu.cn/lwj/) for a nice introduction to the field.

[Dr Victor Lavrenko](https://www.youtube.com/user/victorlavrenko) has two excellent youtube videos [here](https://www.youtube.com/watch?v=Arni-zkqMBA) and [here](https://www.youtube.com/watch?v=dgH0NP8Qxa8), describing the basics of locality sensitive hashing (LSH). These are ideal for those just entering the field or curious how to apply the method to their problem domain.

<p><iframe width="560" height="315" src="https://www.youtube.com/embed/Arni-zkqMBA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/dgH0NP8Qxa8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

The reader is encouraged to further explore the following survey publications:

* [Learning to Hash for Indexing Big Data - A Survey](https://arxiv.org/pdf/1509.05472.pdf)
* [A Survey on Learning to Hash](https://arxiv.org/pdf/1606.00185.pdf)
* [Learning Binary Hash Codes for Large-Scale Image Search](http://www.cs.utexas.edu/~grauman/temp/GraumanFergus_Hashing_chapterdraft.pdf)
* [Locality-Sensitive Hashing for Finding Nearest Neighbors](https://www.slaney.org/malcolm/yahoo/Slaney2008-LSHTutorial.pdf)

### Courses
A few university courses are been taught covering aspects of machine of efficient computing. Below there are a few that have publicly available material.
* [Extreme Computing](http://www.inf.ed.ac.uk/teaching/courses/exc/index_17-18.html) in University of Edinburgh.
* [Text Technologies for Data Science](https://www.inf.ed.ac.uk/teaching/courses/tts/) in University of Edinburgh.

### Blog Posts
Blog posts provide a great way to learn about cutting edge research and ideas. Here are a few of our favourites:
* [Fast Near-Duplicate Image Search using Locality Sensitive Hashing](https://towardsdatascience.com/fast-near-duplicate-image-search-using-locality-sensitive-hashing-d4c16058efcb)
* [An Introduction to Hashing in the Era of Machine Learning](https://blog.bradfieldcs.com/an-introduction-to-hashing-in-the-era-of-machine-learning-6039394549b0)
* [Locality Sensitive Hashing: An effective way of reducing the dimensionality of your data](https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134)
* [Johnson–Lindenstrauss lemma](https://www.wikiwand.com/en/Johnson%E2%80%93Lindenstrauss_lemma)
* [LSH Ideas](http://rakaposhi.eas.asu.edu/s01-cse494-mailarchive/msg00054.html)

Please, feel free to submit a pull request to adding more links in this page.

{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = https://learning2hash.github.io/resources.html;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = learning2hash/resources; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://https-learning2hash-github-io-resources-html.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
{% endif %}
