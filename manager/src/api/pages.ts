class Pagination {
  constructor(options) {
    this.container = options.container; // 分页容器
    this.currentPage = 1;               // 当前页码
    this.totalPages = 10;               // 总页数
    this.maxVisible = 5;                // 最大可见页码数

    this.init();
  }

  // 初始化方法
  init() {
    this.render();
    this.bindEvents();
  }

  // 生成页码数组（带省略号逻辑）
  generatePages() {
    const pages = [];
    const half = Math.floor(this.maxVisible / 2);
    let start = Math.max(1, this.currentPage - half);
    let end = Math.min(this.totalPages, start + this.maxVisible - 1);

    // 调整边界情况
    if (end - start < this.maxVisible - 1) {
      start = Math.max(1, end - this.maxVisible + 1);
    }

    // 生成页码序列
    for (let i = start; i <= end; i++) pages.push(i);

    // 处理前导省略号
    if (start > 1) {
      if (start > 2) pages.unshift('...');
      pages.unshift(1);
    }

    // 处理后导省略号
    if (end < this.totalPages) {
      if (end < this.totalPages - 1) pages.push('...');
      pages.push(this.totalPages);
    }

    return pages;
  }

  // 渲染分页组件
  render() {
    const pages = this.generatePages();
    const prevDisabled = this.currentPage === 1 ? 'disabled' : '';
    const nextDisabled = this.currentPage === this.totalPages ? 'disabled' : '';

    const html = `
      <div class="pagination">
        <button class="prev ${prevDisabled}">← 上页</button>
        ${pages.map(page =>
      page === '...'
        ? '<span class="ellipsis">...</span>'
        : `<button class="page ${this.currentPage === page ? 'active' : ''}">${page}</button>`
    ).join('')}
        <button class="next ${nextDisabled}">→ 下一页</button>
      </div>
    `;

    this.container.innerHTML = html;
  }

  // 事件绑定
  bindEvents() {
    this.container.addEventListener('click', (e) => {
      const target = e.target.closest('button');
      if (!target) return;

      if (target.classList.contains('prev')) {
        this.goToPage(this.currentPage - 1);
      } else if (target.classList.contains('next')) {
        this.goToPage(this.currentPage + 1);
      } else if (target.classList.contains('page')) {
        this.goToPage(Number(target.textContent));
      }
    });
  }

  // 跳转页面
  goToPage(page) {
    if (
      page < 1 ||
      page > this.totalPages ||
      page === this.currentPage
    ) return;

    this.currentPage = page;
    this.render();
    // 这里可以添加实际的页面内容加载逻辑
    console.log(`跳转到第 ${page} 页`);
  }
}

// 使用示例
const container = document.querySelector('#pagination-container');
new Pagination({ container });