/**
 * local-fix.js
 * Fixes issues that occur when previewing a Duda-exported site locally.
 * The Duda platform uses lazy-loading (data-src) and entrance animations
 * that require their backend JS (livesite.js) to initialize. This script
 * bypasses those dependencies for local preview purposes.
 */

(function () {
    // Fix lazy-loaded images: copy data-src -> src so images actually load
    function fixLazyImages() {
        document.querySelectorAll('img[data-src]').forEach(function (img) {
            if (!img.src || img.src === window.location.href) {
                img.src = img.getAttribute('data-src');
            }
        });
    }

    // Run immediately and again after a short delay for any dynamically added images
    fixLazyImages();
    setTimeout(fixLazyImages, 500);
    setTimeout(fixLazyImages, 1500);
})();
