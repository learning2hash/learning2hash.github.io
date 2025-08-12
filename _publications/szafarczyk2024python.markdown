---
layout: publication
title: A Python Library For Efficient Computation Of Molecular Fingerprints
authors: "Micha\u0142 Szafarczyk, Piotr Ludynia, Przemys\u0142aw Kukla"
conference: Arxiv
year: 2024
bibkey: szafarczyk2024python
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2403.19718'}]
tags: ["Tools & Libraries"]
short_authors: "Micha\u0142 Szafarczyk, Piotr Ludynia, Przemys\u0142aw Kukla"
---
Machine learning solutions are very popular in the field of chemoinformatics,
where they have numerous applications, such as novel drug discovery or
molecular property prediction. Molecular fingerprints are algorithms commonly
used for vectorizing chemical molecules as a part of preprocessing in this kind
of solution. However, despite their popularity, there are no libraries that
implement them efficiently for large datasets, utilizing modern, multicore
architectures. On top of that, most of them do not provide the user with an
intuitive interface, or one that would be compatible with other machine
learning tools.
  In this project, we created a Python library that computes molecular
fingerprints efficiently and delivers an interface that is comprehensive and
enables the user to easily incorporate the library into their existing machine
learning workflow. The library enables the user to perform computation on large
datasets using parallelism. Because of that, it is possible to perform such
tasks as hyperparameter tuning in a reasonable time. We describe tools used in
implementation of the library and asses its time performance on example
benchmark datasets. Additionally, we show that using molecular fingerprints we
can achieve results comparable to state-of-the-art ML solutions even with very
simple models.