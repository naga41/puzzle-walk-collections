const CACHE_NAME = 'puzzle-walk-v2';
const ASSETS_TO_CACHE = [
    './',
    './index.html',
    './app.html',
    './core/css/style.css',
    './core/js/engine.js',
    './manifest.json',
    './contents/tokyo-rediscovery/scenario.json'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(ASSETS_TO_CACHE);
        })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            // キャッシュがあれば返す、なければネットワークへリクエスト
            return cachedResponse || fetch(event.request).then(response => {
                return caches.open(CACHE_NAME).then(cache => {
                    if (event.request.url.indexOf('scenario.json') > -1) {
                        cache.put(event.request, response.clone());
                    }
                    return response;
                });
            });
        }).catch((err) => {
            // オフラインかつキャッシュにない場合のフォールバック
            if (event.request.mode === 'navigate') {
                return caches.match('./index.html');
            }
            // faviconなど、キャッシュにもなく取得にも失敗した場合は空のレスポンスを返す
            return new Response('', { status: 404, statusText: 'Not Found' });
        })
    );
});

self.addEventListener('activate', (event) => {
    // 古いキャッシュの削除
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames.map((name) => {
                    if (name !== CACHE_NAME) {
                        return caches.delete(name);
                    }
                })
            );
        })
    );
});
