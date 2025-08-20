---
layout: default
title: Search Open Source Learning to Hash Tools
description: A searchable list of open-source Learning to Hash tools
---

<h2 style="font-size: 1.8em; margin-bottom: 10px;">🧰 Open Source Learning to Hash Tools</h2>
<p style="font-size: 1.05em;">
  Search, filter, and sort to find relevant repositories.
</p>

<!-- Loading Indicator -->
<div id="loading" role="status" aria-live="polite">
  <p>Loading Open Source Learning to Hash Tools ...</p>
</div>

<!-- Controls -->
<div class="controls" id="toolsControls" style="display:none;">
  <div class="search">
    <label for="toolsSearch"><strong>Search</strong></label>
    <input id="toolsSearch" type="search" placeholder="🔍 Search repo, category, description…" inputmode="search" />
    <button id="resetToolsSearch" type="button" aria-label="Clear search">Clear</button>
    <span id="toolsVisibleCount" class="small" aria-live="polite"></span>
  </div>
</div>

<!-- Data Table -->
<table id="tools-table" class="display stripe hover" style="width:100%; display:none;">
  <thead>
    <tr>
      <th>Repo</th>
      <th>Category</th>
      <th>Stars</th>
      <th>Description</th>
      <th>cat_raw</th> <!-- hidden plain-text category for robust filtering -->
    </tr>
  </thead>
  <tbody></tbody>
</table>

<style>
  .dataTables_wrapper{ width:100%; overflow-x:hidden; }
  #loading{
    position:fixed; top:50%; left:50%; transform:translate(-50%,-50%);
    font-size:1.05em; text-align:center; z-index:1000;
    background:white; padding:.8em 1.2em; border:1px solid #ccc; border-radius:8px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
  }

  #tools-table{
    display:none;
    width:100%;
    border-collapse:collapse;
  }

  #tools-table td {
    white-space: normal !important;
    word-break: break-word;
    overflow-wrap: anywhere;
    vertical-align: top;
  }

  #tools-table th {
    white-space: nowrap !important;
    overflow: hidden;
    text-overflow: ellipsis;
    vertical-align: middle;
  }

  #tools-table th:nth-child(3),
  #tools-table td:nth-child(3){ text-align:right; }

  #tools-table, #tools-table * {
    -webkit-column-count: 1 !important;
    -moz-column-count: 1 !important;
    column-count: 1 !important;
  }

  #tools-table td:nth-child(4) .desc{
    display:block;
    line-height:1.35;
    overflow:hidden;
    display:-webkit-box;
    -webkit-box-orient:vertical;
    -webkit-line-clamp:3;
  }

  .controls{ display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:.6rem; margin:.6rem 0 .9rem; }
  .search{ display:flex; align-items:flex-start; gap:.6rem; flex-wrap:wrap; }
  .search label{ font-weight:700; font-size:.85rem; }
  .search input{ width:clamp(160px, 32vw, 520px); padding:.4rem .5rem; border:1px solid #aaa; border-radius:6px; font-size:.9rem; background-color:#f8f9fa; }
  .search input:focus{ outline:none; border-color:#0c5fce; box-shadow:0 0 0 2px rgba(26,115,232,.25); }
  .search button{ padding:.4rem .6rem; font-size:.85rem; border:1px solid #aaa; border-radius:6px; background:#f8f9fa; cursor:pointer; }
  .search button:hover{ background:#ececec; }
  .small{ color:#6b7280; font-size:.9em; }

  .dataTables_filter{ display:none !important; }

  /* Category chip inside the table */
  .tags-display{ display:flex; flex-wrap:wrap; gap:.25rem .35rem; }
  .tags-display .tag-chip{ font-size:.70rem; padding:.15rem .45rem; gap:.25rem; line-height:1.0; }
</style>

<!-- Dependencies -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css" />
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.5.0/css/responsive.dataTables.min.css" />
<script src="https://cdn.datatables.net/responsive/2.5.0/js/dataTables.responsive.min.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>

<script>
  var datatable;

  function updateVisibleCount(){
    if (!datatable) return;
    const el = document.getElementById('toolsVisibleCount');
    if (el) el.textContent = datatable.rows({ filter: 'applied' }).count() + ' rows';
  }

  // External search bar only
  let toolsSearchInput, toolsResetBtn;
  function initToolsSearchBar(){
    toolsSearchInput = document.getElementById('toolsSearch');
    toolsResetBtn = document.getElementById('resetToolsSearch');

    function doSearch(){
      if (!datatable) return;
      const q = (toolsSearchInput.value || '').trim();
      datatable.search(q).draw();
      updateVisibleCount();
    }

    toolsSearchInput.addEventListener('input', doSearch);
    toolsResetBtn.addEventListener('click', () => {
      toolsSearchInput.value='';
      datatable.search('').draw();
      updateVisibleCount();
      toolsSearchInput.focus();
    });

    document.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { 
        e.preventDefault(); toolsSearchInput.focus(); 
      }
      else if (e.key === 'Escape') { 
        toolsSearchInput.value=''; datatable.search('').draw(); updateVisibleCount(); 
      }
    });

    document.getElementById('toolsControls').style.display = '';
    updateVisibleCount();
  }

  $(document).ready(function () {
    $('#loading').show();

    d3.csv("github_topics.csv").then(function (data) {
      const rows = data.map(function (tool) {
        const github = (tool.repo || "").trim();
        const repo_url = "https://github.com/" + github;
        const desc_full = (tool.description || "").trim();
        const desc_short = desc_full.length > 400 ? (desc_full.substring(0, 400) + "…") : desc_full;
        const starsNum = tool.stars ? +tool.stars : 0;

        const category = (tool.category || '').trim() || 'Uncategorized';

        const chips = `<span class="tags-display">
          <span class="tag-chip" tabindex="-1" aria-hidden="true">${category}</span>
        </span>`;

        const escapedTitle = desc_full.replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
        const descCell = `<div class="desc" title="${escapedTitle}">${desc_short}</div>`;

        return [
          `<a href="${repo_url}" target="_blank" rel="noopener noreferrer">${github}</a>`,
          chips,
          starsNum,
          descCell,
          category
        ];
      });

      const dt = $('#tools-table').DataTable({
        data: rows,
        columns: [
          { title: "Repo" },
          { title: "Category" },
          { title: "Stars" },
          { title: "Description" },
          { title: "cat_raw" }
        ],
        responsive: {
          details: { type: 'inline', target: 'tr' },
          breakpoints: [
            { name: 'desktop', width: Infinity },
            { name: 'laptop',  width: 1440 },
            { name: 'tablet',  width: 1024 },
            { name: 'phone',   width: 640 }
          ]
        },
        autoWidth: false,
        paging: false,
        searching: true,
        order: [[2, 'desc']],
        columnDefs: [
          { targets: 2, type: 'num' },
          { responsivePriority: 1, targets: 0 },
          { responsivePriority: 2, targets: 2 },
          { responsivePriority: 3, targets: 3 },
          { responsivePriority: 4, targets: 1 },
          { targets: 4, visible: false, searchable: true }
        ],
        initComplete: function () {
          datatable = this.api();
          $('#loading').hide();
          $('#tools-table').show();
          initToolsSearchBar();
          datatable.on('draw', updateVisibleCount);
          updateVisibleCount();
        }
      });

    }).catch(function (error) {
      console.error("Error loading github_topics.csv:", error);
      $('#tools-table').after(`<div style="color:red; margin-top:10px;">Failed to load data.</div>`);
      $('#loading').hide();
    });
  });
</script>
