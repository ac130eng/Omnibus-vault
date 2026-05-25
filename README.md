# Omnibus Vault — PWA

A mobile-first comic omnibus collection tracker with live eBay price lookups.

## Files
- `index.html` — main app
- `manifest.json` — PWA manifest
- `sw.js` — service worker (offline support)
- `icons/` — app icons

## Deploy for free in 2 minutes

### Option A: Netlify Drop (easiest, no account needed)
1. Go to https://app.netlify.com/drop
2. Drag the entire `omnibus-pwa` folder onto the page
3. Netlify gives you a live URL instantly (e.g. https://random-name-123.netlify.app)
4. Open that URL on your phone
5. Tap Share → Add to Home Screen (iOS) or Install App (Android)
6. Done — icon on your home screen, works like a native app

### Option B: GitHub Pages (free, permanent URL)
1. Create a free GitHub account at github.com
2. New repository → name it `omnibus-vault` → Public
3. Upload all files (drag & drop in the browser)
4. Settings → Pages → Source: main branch → Save
5. Your URL: https://yourusername.github.io/omnibus-vault
6. Add to home screen same as above

### Option C: Vercel
1. Go to vercel.com → New Project
2. Import from GitHub (use Option B first) or drag folder
3. Deploy → get your URL

## Features
- Add books with title, publisher, condition, price paid, purchase date, read status, notes
- Filter by publisher or unread
- Live eBay sold price lookup (requires internet)
- Tracks gain/loss vs. what you paid
- Export to CSV
- Works offline after first load (app shell cached)
- Data stored locally on your device (localStorage)

## Notes
- Data is stored on the device — uninstalling clears it. Export CSV regularly as backup.
- Price lookup uses the Anthropic API + web search. Requires an active internet connection.
- For iOS: Safari → Share → Add to Home Screen (Chrome on iOS does not support PWA install)
