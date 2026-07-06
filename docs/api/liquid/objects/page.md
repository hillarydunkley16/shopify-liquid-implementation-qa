---
title: 'Liquid objects: page'
description: >-
  A
  [page](https://help.shopify.com/manual/online-store/themes/theme-structure/pages)
  on a store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/page'
  md: 'https://shopify.dev/docs/api/liquid/objects/page.md'
api_name: liquid
---

# page

A [page](https://help.shopify.com/manual/online-store/themes/theme-structure/pages) on a store.

## Properties

* * **author**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The author of the page.

  * **content**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The content of the page.

  * **handle**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [handle](https://shopify.dev/docs/api/liquid/basics#handles) of the page.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the page.

  * **metafields**

  * The [metafields](https://shopify.dev/docs/api/liquid/objects/metafield) applied to the page.

    **Tip:** To learn about how to create metafields, refer to \<a href="/apps/metafields/manage">Create and manage metafields\</a> or visit the \<a href="https://help.shopify.com/manual/metafields">Shopify Help Center\</a>.

  * **published\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the page was published.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **template\_​suffix**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the [custom template](https://shopify.dev/themes/architecture/templates#alternate-templates) assigned to the page.

    The name doesn't include the `page.` prefix, or the file extension (`.json` or `.liquid`).

    If a custom template isn't assigned to the page, then `nil` is returned.

  * **title**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The title of the page.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL of the page.

##### Example

```json
{
  "author": null,
  "content": "<p>Polina's Potent Potions was started by Polina in 1654.</p>\n<p>We use all-natural locally sourced ingredients for our potions.</p>",
  "handle": "about-us",
  "id": 83536642113,
  "metafields": {},
  "published_at": "2022-05-04 17:47:03 -0400",
  "template_suffix": "",
  "title": "About us",
  "url": {}
}
```

## Templates using page

[Theme architecture](https://shopify.dev/themes/architecture/templates/page)

[page template](https://shopify.dev/themes/architecture/templates/page)
