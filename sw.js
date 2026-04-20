const CACHE_NAME = 'puzzle-walk-v1';
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
                // オプション: 動的に取得した scenario.json などをキャッシュに追加
                return caches.open(CACHE_NAME).then(cache => {
                    if (event.request.url.indexOf('scenario.json') > -1) {
                        cache.put(event.request, response.clone());
                    }
                    return response;
                });
            });
        }).catch(() => {
            // オフラインかつキャッシュにない場合のフォールバック（不要ならエラーを返す）
            if (event.request.mode === 'navigate') {
                return caches.match('./index.html');
            }
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
