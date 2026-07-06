---
title: 'Liquid objects: model_source'
description: A model source file.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/model_source'
  md: 'https://shopify.dev/docs/api/liquid/objects/model_source.md'
api_name: liquid
---

# model\_​source

A model source file.

## Properties

* * **format**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The format of the model source file.

  * **mime\_​type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) of the model source file.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) of the model source file.

##### Example

```json
{
  "format": "glb",
  "mime_type": "model/gltf-binary",
  "url": "//polinas-potent-potions.myshopify.com/cdn/shop/3d/models/o/eb9388299ce0557c/WaterBottle.glb?v=0"
}
```
