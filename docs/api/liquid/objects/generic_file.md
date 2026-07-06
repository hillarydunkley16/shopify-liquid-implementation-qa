---
title: 'Liquid objects: generic_file'
description: >-
  A file from a `file_reference` type
  [metafield](/docs/api/liquid/objects/metafield) that is neither an image or
  video.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/generic_file'
  md: 'https://shopify.dev/docs/api/liquid/objects/generic_file.md'
api_name: liquid
---

# generic\_​file

A file from a `file_reference` type [metafield](https://shopify.dev/docs/api/liquid/objects/metafield) that is neither an image or video.

***

**Tip:** To learn about metafield types, refer to \<a href="/apps/metafields/types">Metafield types\</a>.

***

## Properties

* * **alt**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The alt text of the media.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the file.

  * **media\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The media type of the model. Always returns `generic_file`.

  * **position**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The position of the media in the [`product.media` array](https://shopify.dev/docs/api/liquid/objects/product#product-media).

    If the source is a [`file_reference` metafield](https://shopify.dev/apps/metafields/types), then `nil` is returned.

  * **preview\_​image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * A preview image for the file.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for the file.

##### Example

```json
{
  "alt": null,
  "id": 21918386454593,
  "media_type": "generic_file",
  "position": null,
  "preview_image": {},
  "url": "//polinas-potent-potions.myshopify.com/cdn/shop/files/disclaimer.pdf?v=9043651738044769859"
}
```
