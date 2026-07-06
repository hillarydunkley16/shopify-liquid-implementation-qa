---
title: 'Liquid filters: collection_img_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for a [collection's
  image](/docs/api/liquid/objects/collection#collection-image).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/collection_img_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/collection_img_url.md'
api_name: liquid
---

# collection\_​img\_​url

```oobleck
variable | collection_img_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for a [collection's image](https://shopify.dev/docs/api/liquid/objects/collection#collection-image).

**Deprecated:**

The `collection_img_url` filter has been replaced by [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

##### Code

```liquid
{{ collection.image | collection_img_url }}
```

##### Data

```json
{
  "collection": {
    "image": "collections/sale-written-in-lights.jpg"
  }
}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/collections/sale-written-in-lights.jpg?v=1657654130
```

### The size parameter

```oobleck
image | collection_img_url: string
```

By default, the `collection_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size).

##### Code

```liquid
{{ collection.image | collection_img_url: 'large' }}
```

##### Data

```json
{
  "collection": {
    "image": "collections/sale-written-in-lights.jpg"
  }
}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/collections/sale-written-in-lights_large.jpg?v=1657654130
```
