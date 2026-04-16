const CACHE_NAME = 'corefy-v3';
const ASSETS = [
  '/corefy/',
  '/corefy/index.html',
  'https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&display=swap'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
  ));
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(cached => cached || fetch(e.request)));
});

// ── TIMER NOTIFICATIONS ──
let timerTimeout = null;

self.addEventListener('message', e => {
  if (e.data.type === 'START_TIMER') {
    const { delay, label, isRest } = e.data;
    if (timerTimeout) clearTimeout(timerTimeout);
    timerTimeout = setTimeout(() => {
      self.registration.showNotification('COREFY ⏱', {
        body: isRest ? '✅ Repos terminé — GO !' : `⏹ ${label} — STOP !`,
        icon: '/corefy/icon-192.png',
        badge: '/corefy/icon-192.png',
        vibrate: [200, 100, 200, 100, 400],
        tag: 'corefy-timer',
        renotify: true,
        silent: false
      });
      timerTimeout = null;
    }, delay);
  }
  if (e.data.type === 'CANCEL_TIMER') {
    if (timerTimeout) { clearTimeout(timerTimeout); timerTimeout = null; }
  }
});

self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(
    clients.matchAll({ type: 'window' }).then(list => {
      for (const c of list) {
        if (c.url.includes('/corefy') && 'focus' in c) return c.focus();
      }
      if (clients.openWindow) return clients.openWindow('/corefy/');
    })
  );
});
