---
layout: default
title: Resources
---

<h2 style="font-size: 1.8em; margin-bottom: 10px;">📚 Resources on Machine Learning for Hashing</h2>
<p style="font-size: 1.05em;">
  A curated collection of <strong>papers</strong>, <strong>datasets</strong>, 
  <strong>courses</strong>, and <strong>tools</strong> covering all aspects of 
  <strong>machine learning for hashing</strong>. Use the search bar to quickly 
  find relevant resources across categories.
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

<!-- Loading -->
<div id="loading" role="status" aria-live="polite">
  <p>Loading Resources Explorer …</p>
</div>

<!-- Cards -->
<div id="cardsGrid" class="cards" style="display:none;" aria-live="polite"></div>
<p id="emptyState" class="empty" style="display:none;">No resources match your search.</p>

<!-- Hidden Data Table -->
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

<!-- Hidden markdown data (indexed into cards) -->
<details id="resourcesContent" markdown="1" hidden aria-hidden="true">
  <summary>Hidden resources source</summary>

### 🎥📘 Introductory Video Material
<!-- (content unchanged) -->
</details>

<style>
  :root{
    --bg:#ffffff;
    --card:#fff;
    --muted:#6b7280;
    --line:#e5e7eb;
    --shadow:0 1px 2px rgba(0,0,0,.06), 0 8px 24px rgba(0,0,0,.04);
    --brand:#1a73e8;

    /* If you have a fixed site header/ribbon, set its height here */
    --site-header: 0px;   /* e.g. 56px */
    --sticky-gap: 12px;   /* breathing room below header */
  }

  html { scroll-behavior: smooth; }

  /* === STICKY TOOLBAR === */
  .toolbar{
    position: sticky;
    top: calc(var(--site-header) + var(--sticky-gap));
    z-index: 20;
    background: linear-gradient(#fff, rgba(255,255,255,.92));
    backdrop-filter: blur(4px);
    border:1px solid var(--line);
    border-radius:12px; padding:10px 12px; margin:8px 0 12px;
    display:flex; align-items:center; gap:12px;
    box-shadow: var(--shadow);
    max-width:100%; box-sizing:border-box;
  }
  /* Slightly stronger shadow when stuck (toggled by JS) */
  .toolbar.is-stuck{ box-shadow: 0 2px 10px rgba(0,0,0,.08); }

  .toolbar .left{ flex:1 1 auto; min-width:0; }

  .search{
    display:flex; align-items:center; gap:.6rem; flex-wrap:wrap;
    width:100%; max-width:100%;
  }
  .search label{ font-weight:700; font-size:.85rem; }
  .search input{
    flex:1 1 240px; min-width:0; width:auto;
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
  .small{ color:#6b7280; font-size:.9em; }

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
    /* prevent anchor jumps hiding under sticky toolbar */
    scroll-margin-top: calc(var(--site-header) + var(--sticky-gap) + 12px);
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
  .card:hover{ transform:translateY(-1px); }
  .meta{ display:flex; align-items:center; gap:8px; color:#6b7280; font-size:.85rem; flex-wrap:wrap; }
  .favicon{ width:16px; height:16px; border-radius:4px; background:#f3f4f6; }
  .title{ font-weight:700; line-height:1.25; margin:2px 0; overflow:hidden;
    display:-webkit-box; -webkit-box-orient:vertical; -webkit-line-clamp:2; word-break:break-word; }
  .title a{ text-decoration:none; color:#0f172a; }
  .title a:hover{ text-decoration:underline; }
  .desc{ color:#374151; font-size:.95rem; line-height:1.45;
    display:-webkit-box; -webkit-box-orient:vertical; -webkit-line-clamp:4; overflow:hidden; }
  .badges{ display:flex; gap:6px; margin-top:6px; flex-wrap:wrap; }
  .badge{ font-size:.75rem; border:1px solid var(--line); padding:.2rem .45rem; border-radius:999px; background:#f7f7fb; cursor:pointer; }
  .empty{ color:#6b7280; text-align:center; padding:24px 8px; }

  #loading{
    position:fixed; top:50%; left:50%; transform:translate(-50%,-50%);
    font-size:1.05em; text-align:center; z-index:1000;
    background:white; padding:.8em 1.2em; border:1px solid #ccc; border-radius:8px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
  }
  @media (max-width:640px){
    .desc{-webkit-line-clamp:6;}
    :root{ --sticky-gap: 8px; }
  }
</style>

<link rel="stylesheet" href="{{ '/assets/vendor/datatables-1.13.6.min.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/vendor/dataTables.responsive-2.5.0.min.css' | relative_url }}">
<script src="{{ '/assets/vendor/jquery-3.6.0.min.js' | relative_url }}" defer></script>
<script src="{{ '/assets/vendor/datatables-1.13.6.min.js' | relative_url }}" defer></script>
<script src="{{ '/assets/vendor/dataTables.responsive-2.5.0.min.js' | relative_url }}" defer></script>

<script>
(function(){
  function waitForDT(cb, tries=80){
    if(window.jQuery && jQuery.fn && jQuery.fn.dataTable) return cb();
    if(tries<=0) return cb(new Error('DataTables not loaded'));
    setTimeout(()=>waitForDT(cb,tries-1),100);
  }
  function ready(fn){
    if(document.readyState==='loading')
      document.addEventListener('DOMContentLoaded',fn,{once:true});
    else fn();
  }
  function readHashQuery(){
    const raw=window.location.hash?window.location.hash.slice(1):'';
    if(!raw) return '';
    try{return decodeURIComponent(raw.replace(/\+/g,' '));}catch{return raw;}
  }
  function setHash(q){
    if(q&&q.trim().length)history.replaceState(null,'','#'+encodeURIComponent(q.trim()));
    else history.replaceState(null,'',location.pathname+location.search);
  }
  function textContentTrim(n){return(n?n.textContent:'').replace(/\s+/g,' ').trim();}
  function escapeHtml(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');}
  function domainFromUrl(u){try{return new URL(u,location.origin).hostname;}catch(e){return'';}}
  function debounce(fn,ms=120){let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),ms);};}
  function slugify(s){return(s||'uncategorised').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/(^-|-$)/g,'');}

  const loadingEl=document.getElementById('loading');
  const toolbarEl=document.getElementById('resToolbar');
  const inputEl=document.getElementById('resSearch');
  const resetEl=document.getElementById('resetResSearch');
  const countEl=document.getElementById('resVisibleCount');
  const gridEl=document.getElementById('cardsGrid');
  const emptyEl=document.getElementById('emptyState');
  const contentEl=document.getElementById('resourcesContent');
  const jumpBarEl=document.getElementById('jumpBar');
  let datatable;

  function updateVisibleCount(){
    if(!datatable||!countEl)return;
    countEl.textContent=datatable.rows({filter:'applied'}).count()+' resources';
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
    const prevHidden=contentEl.hasAttribute('hidden');
    const prevDisplay=contentEl.style.display;
    const prevPos=contentEl.style.position;
    const prevLeft=contentEl.style.left;
    if(prevHidden)contentEl.removeAttribute('hidden');
    contentEl.style.display='block'; contentEl.style.position='absolute';
    contentEl.style.left='-99999px';
    const out=fn();
    if(prevHidden)contentEl.setAttribute('hidden','');
    contentEl.style.display=prevDisplay||''; contentEl.style.position=prevPos||''; contentEl.style.left=prevLeft||'';
    return out;
  }

  function scrapeResources(){
    return withRenderedDetails(()=>{
      const rows=[]; const walker=document.createTreeWalker(contentEl,NodeFilter.SHOW_ELEMENT,null);
      let currCat='',currSub='';
      while(walker.nextNode()){
        const el=walker.currentNode;
        if(/^H3$/i.test(el.tagName)){currCat=textContentTrim(el);currSub='';}
        else if(/^H4$/i.test(el.tagName)){currSub=textContentTrim(el);}
        else if(/^LI$/i.test(el.tagName)){
          const a=el.querySelector('a[href]'); if(!a)continue;
          const url=a.getAttribute('href')||''; const title=textContentTrim(a)||'(untitled)';
          let full=textContentTrim(el);
          try{ full=full.replace(new RegExp('^\\*?\\*?\\s*'+title.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\s*:?\\s*','i'),''); }catch{}
          const desc=full; const domain=domainFromUrl(url);
          const titleHTML=`<a href="${url}" target="_blank" rel="noopener noreferrer">${escapeHtml(title)}</a>`;
          const descHTML=desc?escapeHtml(desc):'';
          const raw=[title,currCat,currSub,desc,url,domain].join(' ').toLowerCase();
          rows.push([titleHTML,currCat,currSub,descHTML,raw,url,domain]);
        }
      }
      return rows;
    });
  }

  function renderCards(){
    if(!datatable)return;
    const rows=datatable.rows({filter:'applied'}).data().toArray();
    gridEl.innerHTML='';
    if(!rows.length){
      gridEl.style.display='none'; emptyEl.style.display=''; updateVisibleCount();
      if(jumpBarEl)jumpBarEl.style.display='none'; return;
    }
    emptyEl.style.display='none'; gridEl.style.display='grid';
    let lastCat=null; const catsForJump=[];

    rows.forEach(r=>{
      const titleHTML=r[0], cat=r[1]||'Uncategorised', subcat=r[2]||'', descHTML=r[3], url=r[5]||'', domain=r[6]||domainFromUrl(r[5]);

      if(cat!==lastCat){
        const id='cat-'+slugify(cat);
        const divider=document.createElement('h2');
        divider.className='cat-divider'; divider.id=id; divider.textContent=cat;
        divider.addEventListener('click', ()=> applyFilter(cat));
        gridEl.appendChild(divider);
        catsForJump.push({cat,id}); lastCat=cat;
      }

      const card=document.createElement('article');
      card.className='card';
      card.setAttribute('data-cat',cat);
      card.setAttribute('data-sub',subcat);
      card.setAttribute('data-domain',domain||'');

      card.innerHTML=`
        <div class="meta">
          <img class="favicon" src="https://www.google.com/s2/favicons?domain=${encodeURIComponent(domain||'')}&sz=32" alt="" loading="lazy">
          <span class="meta-domain" title="Filter by site">${domain||'link'}</span>
          ${subcat?'<span>•</span><button class="badge badge-sub" title="Filter by subcategory">'+String(subcat).replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[m]))+'</button>':''}
        </div>
        <h3 class="title">${titleHTML}</h3>
        <div class="desc">${descHTML}</div>
        <div class="badges">
          ${subcat?'<button class="badge badge-sub" title="Filter by subcategory">'+String(subcat).replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[m]))+'</button>':''}
          <button class="badge badge-cat" title="Filter by category">${String(cat).replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[m]))}</button>
        </div>
      `;

      card.addEventListener('click',(e)=>{
        const a=e.target.closest('a'); if(a) return;
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

    if(jumpBarEl){
      if(catsForJump.length){
        jumpBarEl.innerHTML=catsForJump.map(c=>`<a href="#${c.id}">${c.cat}</a>`).join('');
        jumpBarEl.style.display='';
      } else jumpBarEl.style.display='none';
    }

    updateVisibleCount();
  }

  function start(err){
    try{
      if(err||!window.jQuery||!jQuery.fn.dataTable){
        if(loadingEl)loadingEl.innerHTML='<p style="color:#b00020">Failed to load: DataTables missing.</p>';
        return;
      }
      const initialQuery=readHashQuery();
      if(inputEl&&initialQuery)inputEl.value=initialQuery;

      const rows=scrapeResources();

      const dt=jQuery('#resources-table').DataTable({
        data:rows,
        columns:[
          {title:"Title"},
          {title:"Category"},
          {title:"Section"},
          {title:"Description"},
          {title:"raw"},
          {title:"url"},
          {title:"domain"}
        ],
        responsive:{details:false},
        autoWidth:false,
        paging:false,
        searching:true,
        order:[[1,'asc'],[2,'asc'],[0,'asc']],
        columnDefs:[
          {targets:[4], visible:false, searchable:true},
          {targets:[5,6], visible:false, searchable:false}
        ],
        initComplete:function(){
          datatable=this.api();

          if(loadingEl)loadingEl.style.display='none';
          toolbarEl.style.display=''; gridEl.style.display='grid';

          if(initialQuery) datatable.search(initialQuery, false, true, true).draw();

          renderCards();
          datatable.on('draw', renderCards);

          const apply = (()=>{
            let t; return ()=>{ clearTimeout(t); t=setTimeout(()=>{
              const q=inputEl?(inputEl.value||''):'';
              datatable.search(q, false, true, true).draw(false);
              setHash(q);
            },120); };
          })();

          inputEl.addEventListener('input', apply);
          inputEl.addEventListener('keydown', e=>{ if(e.key==='Enter'){ e.preventDefault(); apply(); }});
          resetEl.addEventListener('click', ()=>{
            inputEl.value=''; datatable.search('', false, true, true).draw(false);
            setHash(''); inputEl.focus();
          });

          window.addEventListener('hashchange', ()=>{
            const q=readHashQuery();
            inputEl.value=q;
            datatable.search(q, false, true, true).draw(false);
          });

          document.addEventListener('keydown', (e)=>{
            if((e.metaKey||e.ctrlKey) && e.key.toLowerCase()==='k'){
              e.preventDefault(); inputEl.focus();
            } else if(e.key==='Escape'){
              inputEl.value=''; datatable.search('', false, true, true).draw(false); setHash('');
            }
          });

          setTimeout(()=>datatable.columns.adjust().draw(false),60);
          updateVisibleCount();
        }
      });

      if(rows.length===0){
        gridEl.style.display='none';
        if(loadingEl)loadingEl.innerHTML='<p>No resources detected to index.</p>';
      }
    }catch(e){
      console.error(e);
      if(loadingEl)loadingEl.innerHTML='<p style="color:#b00020">Failed to load resources.</p>';
    }
  }
  ready(()=>waitForDT(start));

  /* Optional: add a stronger shadow when the toolbar is "stuck" */
  try{
    const el=document.getElementById('resToolbar');
    if(el && 'IntersectionObserver' in window){
      const s=document.createElement('div');
      s.style.position='relative'; s.style.height='1px';
      el.parentNode.insertBefore(s, el);
      new IntersectionObserver(([e])=>{
        el.classList.toggle('is-stuck', !e.isIntersecting);
      }, { rootMargin: `-${getComputedStyle(document.documentElement).getPropertyValue('--sticky-gap').trim()||'12px'} 0px 0px 0px` }).observe(s);
    }
  }catch(_e){}
})();
</script>

<p style="margin-top:2rem; color:#6b7280; font-size:.95em;">
  Please, feel free to submit a <a href="contributing.markdown">web form</a> to add more links to this page.
  As an Amazon Associate, this site earns from qualifying purchases made. Some links may be affiliate links (at no extra cost).
</p>
