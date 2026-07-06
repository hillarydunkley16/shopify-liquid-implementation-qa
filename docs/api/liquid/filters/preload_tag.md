---
title: 'Liquid filters: preload_tag'
description: >-
  Generates an HTML `<link>` tag with a `rel` attribute of `preload` to
  prioritize loading a given Shopify-hosted asset.

  The asset URL is also added to the [Link
  header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link)

  with a `rel` attribute of `preload`.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/preload_tag'
  md: 'https://shopify.dev/docs/api/liquid/filters/preload_tag.md'
api_name: liquid
---

# preload\_​tag

```oobleck
string | preload_tag: as: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<link>` tag with a `rel` attribute of `preload` to prioritize loading a given Shopify-hosted asset. The asset URL is also added to the [Link header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Link) with a `rel` attribute of `preload`.

You should use this filter sparingly. For example, consider preloading only resources necessary for rendering above-the-fold content. To learn more about preloading resources, refer to [Performance best practices for Shopify themes](https://shopify.dev/themes/best-practices/performance#preload-key-resources-defer-or-avoid-loading-others).

***

**Tip:** If you want to preload a stylesheet, then use \<a href="/docs/api/liquid/filters/stylesheet\_tag">\<code>\<span class="PreventFireFoxApplyingGapToWBR">stylesheet\<wbr/>\_tag\</span>\</code>\</a>. If you want to preload an image, then use \<a href="/docs/api/liquid/filters/image\_tag">\<code>\<span class="PreventFireFoxApplyingGapToWBR">image\<wbr/>\_tag\</span>\</code>\</a>.

***

The input to this filter must be a URL from one of the following filters:

* [`asset_url`](https://shopify.dev/docs/api/liquid/filters/asset_url)
* [`global_asset_url`](https://shopify.dev/docs/api/liquid/filters/global_asset_url)
* [`shopify_asset_url`](https://shopify.dev/docs/api/liquid/filters/shopify_asset_url)

The `preload_tag` filter also requires an [`as` parameter](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link#attr-as) based on the kind of resource being preloaded.

##### Code

```liquid
{{ 'cart.js' | asset_url | preload_tag: as: 'script' }}
```

##### Output

```html
<link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410" as="script" rel="preload">
```

### HTML attributes

```oobleck
string | preload_tag: as: string, attribute: string
```

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link#attributes) by adding a parameter that matches the attribute name, and the desired value.

##### Code

```liquid
{{ 'cart.js' | asset_url | preload_tag: as: 'script', type: 'text/javascript' }}
```

##### Output

```html
<link href="//polinas-potent-potions.myshopify.com/cdn/shop/t/4/assets/cart.js?v=83971781268232213281663872410" as="script" type="text/javascript" rel="preload">
```
