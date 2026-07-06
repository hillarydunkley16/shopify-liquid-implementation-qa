---
title: 'Liquid objects: sitemap'
description: >-
  The sitemap for a specific group in the [`robots.txt`
  file](/themes/architecture/templates/robots-txt-liquid).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/sitemap'
  md: 'https://shopify.dev/docs/api/liquid/objects/sitemap.md'
api_name: liquid
---

# sitemap

The sitemap for a specific group in the [`robots.txt` file](https://shopify.dev/themes/architecture/templates/robots-txt-liquid).

The sitemap provides information about the pages and content on a site, and the relationships between them, which helps crawlers crawl a site more efficiently.

***

**Tip:** To learn more about sitemaps, refer to \<a href="https://developers.google.com/search/docs/advanced/sitemaps/overview">Google\&#39;s documentation\</a>.

***

The `sitemap` object consists of a `Sitemap` directive, and a value of the URL that the sitemap is hosted at. For example:

```
Sitemap: https://your-store.myshopify.com/sitemap.xml
```

***

**Tip:** You can \<a href="/themes/seo/robots-txt">customize the \<code>robots.txt\</code> file\</a> with the \<a href="/themes/architecture/templates/robots-txt-liquid">\<code>robots.txt.liquid\</code> template\</a>.

***

## Properties

* * **directive**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Returns `Sitemap`.

  * **value**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL that the sitemap is hosted at.

##### Example

```json
{
  "directive": "Sitemap",
  "value": "https://polinas-potent-potions.myshopify.com/sitemap.xml"
}
```
