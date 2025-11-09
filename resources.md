---
layout: default
title: Resources
---
<h1>Resources on Machine Learning for Hashing</h1>

<!-- Slim Toolbar: search + visible count -->
<div id="resToolbar" class="toolbar" style="display:none;">
  <div class="left">
    <div class="search">
      <label for="resSearch"><strong>Search</strong></label>
      <input id="resSearch" type="search" placeholder="🔍 Search title, domain, description…" inputmode="search" />
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

<!-- Hidden Data Table (Data engine only; never shown) -->
<table id="resources-table" class="display stripe hover" style="width:100%; display:none;">
  <thead>
    <tr>
      <th>TitleHTML</th>     <!-- 0 -->
      <th>Category</th>      <!-- 1 -->
      <th>Subcategory</th>   <!-- 2 -->
      <th>DescHTML</th>      <!-- 3 -->
      <th>raw</th>           <!-- 4 -->
      <th>url</th>           <!-- 5 -->
      <th>domain</th>        <!-- 6 -->
    </tr>
  </thead>
  <tbody></tbody>
</table>

<!-- Source content (hidden). Markdown is rendered, but never shown. -->
<details id="resourcesContent" markdown="1" hidden aria-hidden="true">
  <summary>Hidden resources source</summary>

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

- **[Learning-Based Hashing for Approximate Nearest Neighbour (ANN) Search: Foundations and Early Advances](/papers/Learning_Based_Hashing_for_ANN_Search__Foundations_and_Early_Advances.pdf)** (Moran, 2025): A foundational survey introducing the core principles of learning-based hashing for ANN search. 

- **[Learning to Hash for Recommendation: A Survey](https://arxiv.org/abs/2412.03875)** (2024): A dedicated overview of hashing-based methods used in recommender systems, from binary encodings to retrieval-aware deep architectures.
  
- **[Learning to Hash for Indexing Big Data - A Survey](https://arxiv.org/pdf/1509.05472.pdf)**

- **[A Survey on Learning to Hash](https://arxiv.org/pdf/1606.00185.pdf)**

- **[Learning Binary Hash Codes for Large-Scale Image Search](http://www.cs.utexas.edu/~grauman/temp/GraumanFergus_Hashing_chapterdraft.pdf)**

- **[Locality-Sensitive Hashing for Finding Nearest Neighbors](https://www.slaney.org/malcolm/yahoo/Slaney2008-LSHTutorial.pdf)**

- **[Deep Learning for Hashing: A Survey](https://arxiv.org/pdf/1909.06046.pdf)**

- **[Learning to Hash With Binary Deep Neural Networks: A Survey](https://www.sciencedirect.com/science/article/abs/pii/S016786552030208X)**

### 🎓📚 Courses

- **[Learning from Data](http://work.caltech.edu/telecourse.html)**
- **[Extreme Computing](http://www.inf.ed.ac.uk/teaching/courses/exc/index_17-18.html)**
- **[Text Technologies for Data Science](https://www.inf.ed.ac.uk/teaching/courses/tts/)**
- **[CS276: Information Retrieval](https://web.stanford.edu/class/cs276/)**

#### 🧠 DeepLearning.AI Short Courses on Vector Search & ANN
- **[Vector Databases: from Embeddings to Applications](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/?utm_source=chatgpt.com)**
- **[Retrieval Optimization: from Tokenization to Vector Quantization](https://learn.deeplearning.ai/courses/retrieval-optimization-from-tokenization-to-vector-quantization/lesson/lpcaz/introduction?utm_source=chatgpt.com)**
- **[Building Applications with Vector Databases](https://www.deeplearning.ai/short-courses/building-applications-vector-databases/?utm_source=chatgpt.com)**
- **[Retrieval Augmented Generation (RAG)](https://www.deeplearning.ai/courses/retrieval-augmented-generation-rag/?utm_source=chatgpt.com)**
- **[Knowledge Graphs for RAG](https://www.deeplearning.ai/short-courses/knowledge-graphs-rag/?utm_source=chatgpt.com)**
- **[Prompt Compression and Query Optimization](https://www.deeplearning.ai/short-courses/prompt-compression-and-query-optimization/?utm_source=chatgpt.com)**

### 📝📰  Blog Posts
- **[ANN-Benchmarks](https://ann-benchmarks.com/index.html)**
- **[Learning to Hash — Finding the Needle in the Haystack with AI](https://medium.com/@sean.j.moran/learning-to-hash-finding-the-needle-in-the-haystack-with-ai-24a15f85de0e)**
- **[Fast Near-Duplicate Image Search Using LSH](https://towardsdatascience.com/fast-near-duplicate-image-search-using-locality-sensitive-hashing-d4c16058efcb)**
- **[An Introduction to Hashing in the Era of ML](https://blog.bradfieldcs.com/an-introduction-to-hashing-in-the-era-of-machine-learning-6039394549b0)**
- **[Locality-Sensitive Hashing: Reducing Data Dimensionality](https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134)**
- **[Efficient Similarity Search with Faiss](https://engineering.fb.com/2020/11/23/ai-research/faiss/)**
- **[Johnson–Lindenstrauss Lemma](https://www.wikiwand.com/en/Johnson%E2%80%93Lindenstrauss_lemma)**
- **[LSH Ideas](http://rakaposhi.eas.asu.edu/s01-cse494-mailarchive/msg00054.html)**
- **[Intro to LSH (Great Visualizations)](http://tylerneylon.com/a/lsh1/)**
- **[What is LSH?](https://www.quora.com/What-is-locality-sensitive-hashing)**

### 🧩💾 Hashing Software Packages

#### 📦 Hashing Algorithms
- **[Deep Hashing Toolbox](https://github.com/thulab/DeepHash)**
- **[Rensa (beowolx) – High-performance MinHash](https://github.com/beowolx/rensa)**
- **[Deep Supervised Hashing (DSH)](https://github.com/yxtay/Deep-Supervised-Hashing)**
- **[HashNet](https://github.com/thuml/HashNet)**

#### 🏗️ Indexing / ANN Libraries
- **[Faiss](https://github.com/facebookresearch/faiss)**
- **[Annoy](https://github.com/spotify/annoy)**
- **[NMSLIB](https://github.com/nmslib/nmslib)**
- **[HNSWlib](https://github.com/nmslib/hnswlib)**
- **[ScaNN](https://github.com/google-research/google-research/tree/master/scann)**

#### 🛠️ Vector Databases
- **[Milvus](https://milvus.io/)**
- **[Weaviate](https://weaviate.io/)**
- **[Qdrant](https://qdrant.tech/)**

### 🧪📊 Benchmarking Tools and Leaderboards
- **[ANN-Benchmarks](https://github.com/erikbern/ann-benchmarks)** — Aumüller et al. (2019)
- **[Billion-Scale ANN Leaderboard](https://big-ann-benchmarks.com/neurips23.html)**

### 📚📖 Books
- **[Mining of Massive Datasets](https://amzn.to/42PeRDM)**
- **[Introduction to Information Retrieval](https://amzn.to/3WHTNvo)**
- **[Efficient Processing of Deep Neural Networks](https://link.springer.com/book/10.1007/978-3-031-01766-7)**
- **[Similarity Search: The Metric Space Approach](https://amzn.to/46ZLVLV)**
- **[Foundations of Data Science](https://amzn.to/47gHAms)**
- **[Deep Learning](https://amzn.to/47updLU)**

### 🗃️📥 Pre-Processed Datasets for Download
- **[CIFAR-10 Gist Features (.mat)](https://www.dropbox.com/s/875u1rkva9iffpj/Gist512CIFAR10.mat?dl=0)**
- **[LabelMe Gist Features (.mat)](https://www.dropbox.com/s/dwixb9ry4zwvcp9/LabelMe_gist.mat?dl=0)**
- **[MNIST Pixel Features (.mat)](https://www.dropbox.com/s/x3j6ik6kvnw95h3/MNIST_gnd_release.mat?dl=0)**
- **[SIFT 1M Features (.mat)](https://www.dropbox.com/s/29f6r7pqevfy2ck/sift1m.mat?dl=0)**
- **[20 Newsgroups (.mat)](https://www.dropbox.com/s/wql7m8wuvn9efhj/20Newsgroups.mat?dl=0)**
- **[TDT2 (.mat)](https://www.dropbox.com/s/qasz8z3sr1pjqog/TDT2.mat?dl=0)**
- **[BIGANN Dataset](http://corpus-texmex.irisa.fr/)**
- **[Facebook SimSearchNet++](https://dl.fbaipublicfiles.com/billion-scale-ann-benchmarks/FB_ssnpp_database.u8bin)**
- **[Microsoft SPACEV-1B](https://github.com/microsoft/SPTAG/tree/master/datasets/SPACEV1B)**
- **[Yandex DEEP-1B](https://research.yandex.com/datasets/biganns)**
- **[Yandex Text-to-Image-1B](https://research.yandex.com/datasets/biganns)**
- **[Deep1B Dataset](https://github.com/facebookresearch/faiss/wiki/Indexing-1B-vectors)**
- **[DEEP-10M](https://research.yandex.com/datasets)**
- **[GLUE Benchmark](https://gluebenchmark.com/)**
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

  .toolbar{
    position:sticky; top:0; z-index:20;
    background: linear-gradient(#fff, rgba(255,255,255,.92));
    backdrop-filter: blur(4px);
    border:1px solid var(--line);
    border-radius:12px; padding:10px 12px; margin:8px 0 12px;
    display:flex; align-items:center; justify-content:flex-start; gap:12px;
    box-shadow: var(--shadow);
  }

  .search{ display:flex; align-items:center; gap:.6rem; flex-wrap:wrap; }
  .search label{ font-weight:700; font-size:.85rem; }
  .search input{
    width:clamp(220px, 32vw, 560px); padding:.45rem .6rem;
    border:1px solid #cbd5e1; border-radius:8px; font-size:.95rem; background-color:#f8fafc;
  }
  .search input:focus{ outline:none; border-color:var(--brand); box-shadow:0 0 0 2px rgba(26,115,232,.18); }
  .search button{
    padding:.45rem .6rem; font-size:.85rem; border:1px solid #cbd5e1; border-radius:8px; background:#f8fafc; cursor:pointer;
  }
  .search button:hover{ background:#eef2f7; }
  .small{ color:var(--muted); font-size:.9em; }

  .cards{
    display:grid; gap:14px;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  }
  .card{
    border:1px solid var(--line); border-radius:14px; background:var(--card);
    padding:14px; box-shadow: var(--shadow); transition: transform .06s ease;
  }
  .card:hover{ transform: translateY(-1px); }
  .meta{ display:flex; align-items:center; gap:8px; margin-bottom:8px; color:var(--muted); font-size:.85rem; }
  .favicon{ width:16px; height:16px; border-radius:4px; background:#f3f4f6; }
  .title{ font-weight:700; line-height:1.25; margin:0 0 6px; }
  .title a{ text-decoration:none; color:#0f172a; }
  .title a:hover{ text-decoration:underline; }
  .desc{ color:#374151; font-size:.95rem; line-height:1.45; display:-webkit-box; -webkit-box-orient:vertical; -webkit-line-clamp:4; overflow:hidden; }
  .badges{ display:flex; align-items:center; gap:6px; margin-top:10px; flex-wrap:wrap; }
  .badge{
    font-size:.75rem; border:1px solid var(--line); color:#0f172a; padding:.2rem .45rem; border-radius:999px; background:#f7f7fb;
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
  // Wait for jQuery + DataTables (handles defer race)
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

  // Hash helpers (/#query)
  function readHashQuery(){
    const raw = window.location.hash ? window.location.hash.slice(1) : '';
    if (!raw) return '';
    try { return decodeURIComponent(raw.replace(/\+/g,' ')); } catch { return raw; }
  }
  function setHash(q){
    if (q && q.trim().length) history.replaceState(null, '', '#' + encodeURIComponent(q.trim()));
    else history.replaceState(null, '', location.pathname + location.search);
  }

  // Utils
  function textContentTrim(node){ return (node ? node.textContent : '').replace(/\s+/g,' ').trim(); }
  function escapeHtml(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;'); }
  function domainFromUrl(u){ try{ return new URL(u, location.origin).hostname; } catch(e){ return ''; } }
  function faviconForDomain(d){ return d ? 'https://www.google.com/s2/favicons?domain='+encodeURIComponent(d)+'&sz=32' : ''; }
  function debounce(fn, ms=120){ let t; return (...a)=>{ clearTimeout(t); t=setTimeout(()=>fn(...a), ms); }; }

  // DOM refs
  const loadingEl = document.getElementById('loading');
  const toolbarEl = document.getElementById('resToolbar');
  const inputEl   = document.getElementById('resSearch');
  const resetEl   = document.getElementById('resetResSearch');
  const countEl   = document.getElementById('resVisibleCount');
  const gridEl    = document.getElementById('cardsGrid');
  const emptyEl   = document.getElementById('emptyState');
  const contentEl = document.getElementById('resourcesContent');

  let datatable;

  function updateVisibleCount(){
    if (!datatable || !countEl) return;
    countEl.textContent = datatable.rows({ filter:'applied' }).count() + ' resources';
  }

  function renderCards(){
    if (!datatable) return;
    const rows = datatable.rows({ filter:'applied' }).data().toArray();
    gridEl.innerHTML = '';

    if (!rows.length){
      gridEl.style.display='none';
      emptyEl.style.display='';
      updateVisibleCount();
      return;
    }
    emptyEl.style.display='none';
    gridEl.style.display='grid';

    rows.forEach(r => {
      const titleHTML = r[0];
      const cat       = r[1] || '';
      const subcat    = r[2] || '';
      const descHTML  = r[3];
      const url       = r[5] || '';
      const domain    = r[6] || domainFromUrl(url);

      const card = document.createElement('article');
      card.className = 'card';
      card.innerHTML = `
        <div class="meta">
          <img class="favicon" src="${faviconForDomain(domain)}" alt="" loading="lazy">
          <span>${domain || 'link'}</span>
          ${cat ? '<span>•</span><span>'+escapeHtml(cat)+'</span>' : ''}
          ${subcat ? '<span>•</span><span>'+escapeHtml(subcat)+'</span>' : ''}
        </div>
        <h3 class="title">${titleHTML}</h3>
        <div class="desc">${descHTML}</div>
        <div class="badges">
          ${cat ? '<span class="badge">'+escapeHtml(cat)+'</span>' : ''}
          ${subcat ? '<span class="badge">'+escapeHtml(subcat)+'</span>' : ''}
        </div>
      `;

      if (url){
        const a = card.querySelector('.title a');
        if (!a){
          const h3 = card.querySelector('.title');
          h3.innerHTML = `<a href="${url}" target="_blank" rel="noopener">${escapeHtml(h3.textContent)}</a>`;
        }
      }

      gridEl.appendChild(card);
    });

    updateVisibleCount();
  }

  // Scrape hidden lists into rows
  function scrapeResources(){
    const rows = [];
    if (!contentEl) return rows;

    const walker = document.createTreeWalker(contentEl, NodeFilter.SHOW_ELEMENT, null);
    let currCat = '', currSub = '';

    while (walker.nextNode()){
      const el = walker.currentNode;

      if (/^H3$/i.test(el.tagName)) {
        currCat = textContentTrim(el).replace(/^#+\s*/,'');
        currSub = '';
      } else if (/^H4$/i.test(el.tagName)) {
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
          { title: "Title"      }, // 0
          { title: "Category"   }, // 1
          { title: "Section"    }, // 2
          { title: "Description"}, // 3
          { title: "raw"        }, // 4
          { title: "url"        }, // 5
          { title: "domain"     }  // 6
        ],
        responsive: { details: false },
        autoWidth: false,
        paging: false,
        searching: true,
        order: [[1,'asc'], [2,'asc'], [0,'asc']],
        columnDefs: [
          { targets: [4,5,6], visible: false, searchable: false }
        ],
        initComplete: function(){
          datatable = this.api();

          if (loadingEl) loadingEl.style.display='none';
          toolbarEl.style.display='';
          gridEl.style.display='grid';

          if (initialQuery) datatable.search(initialQuery).draw();

          renderCards();
          datatable.on('draw', renderCards);

          const apply = debounce(() => {
            const q = inputEl ? (inputEl.value || '') : '';
            datatable.search(q).draw(false);
            setHash(q);
          }, 120);

          inputEl.addEventListener('input', apply);
          inputEl.addEventListener('keydown', (e)=>{ if (e.key==='Enter'){ e.preventDefault(); apply(); }});
          resetEl.addEventListener('click', () => {
            inputEl.value=''; datatable.search('').draw(false); setHash(''); inputEl.focus();
          });
          window.addEventListener('hashchange', () => {
            const q = readHashQuery();
            inputEl.value = q;
            datatable.search(q).draw(false);
          });

          document.addEventListener('keydown', (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
              e.preventDefault(); inputEl.focus();
            } else if (e.key === 'Escape') {
              inputEl.value=''; datatable.search('').draw(false); setHash('');
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
  Please, feel free to submit a <a href="contributing.markdown">web form</a> to add more links to this page.
  As an Amazon Associate, this site earns from qualifying purchases made. Some links may be affiliate links (at no extra cost).
</p>
