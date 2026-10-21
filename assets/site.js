// Lightbox for the screenshot galleries (no dependencies).
(function () {
  const overlay = document.createElement('div');
  overlay.id = 'lightbox';
  overlay.style.cssText = 'position:fixed;inset:0;background:rgba(4,8,16,.94);display:none;' +
    'align-items:center;justify-content:center;z-index:99;cursor:zoom-out;padding:24px';
  const img = document.createElement('img');
  img.style.cssText = 'max-width:100%;max-height:100%;border-radius:12px;box-shadow:0 30px 80px rgba(0,0,0,.6)';
  overlay.appendChild(img);
  document.body.appendChild(overlay);
  const close = () => { overlay.style.display = 'none'; };
  overlay.addEventListener('click', close);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  document.querySelectorAll('.shot').forEach(a => {
    a.addEventListener('click', e => {
      e.preventDefault();
      img.src = a.getAttribute('href');
      overlay.style.display = 'flex';
    });
  });
})();
