# How to Publish the Dashboard (Shareable Phone Link)

## The live link
**https://safeharbor-reddit-helper.netlify.app/**

This is the URL to open on your phone and send to Saddie. It shows today's Reddit
posts to help with. (If it ever shows "0 / Loading" in a real browser — not the
chat preview — the uploaded file was an old/broken one; re-publish per below.)

## What gets published
One file: `6_load-the-dashboard/output/dashboard.html`
It is fully self-contained — today's posts are baked inside it. Nothing else is needed.

## Publish / update each day (Netlify Drop — no account needed)
1. After `run reddit` finishes, find `6_load-the-dashboard/output/dashboard.html`.
2. Go to **https://app.netlify.com/drop**
3. Drag `dashboard.html` onto the page.
4. Netlify gives a URL. Open it on your phone to check the posts show.

## Keep ONE permanent link (recommended — do this once)
On the Netlify result page, click **"Sign up to claim this site"** (free).
Once claimed, the site keeps the SAME url (the safeharbor-reddit-helper one above).
Each day, open that site in Netlify → **Deploys** → drag the new `dashboard.html`
to replace it. Same link, fresh posts.

## Important: open in a real browser
A web-page fetcher / preview that does not run JavaScript will show "0 / Loading"
because the cards are drawn by the page's script. On a normal phone or desktop
browser it renders all the posts. This is normal.

## Future automation
When Anthropic's Netlify connector is back online (it returned "Server not found"
during setup), the pipeline can auto-publish to this same URL at the end of every
`run reddit`, so you never drag the file manually. Ask Claude to wire it up then.
