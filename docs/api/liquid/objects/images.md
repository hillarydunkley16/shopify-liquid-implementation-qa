---
title: 'Liquid objects: images'
description: >-
  All of the [images](/docs/api/liquid/objects/image) that have been
  [uploaded](https://help.shopify.com/manual/online-store/images/theme-images#upload-images)

  to a store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/images'
  md: 'https://shopify.dev/docs/api/liquid/objects/images.md'
api_name: liquid
---

# images

All of the [images](https://shopify.dev/docs/api/liquid/objects/image) that have been [uploaded](https://help.shopify.com/manual/online-store/images/theme-images#upload-images) to a store.

### Directly accessible in

* Global

You can access images from the `images` array by their filename.

##### Code

```liquid
{{ images['potions-header.png'] | image_url: width: 300 | image_tag }}
```

##### Output

```html
<img src="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300" alt="" srcset="//polinas-potent-potions.myshopify.com/cdn/shop/files/potions-header.png?v=1650325393&amp;width=300 300w" width="300" height="173" style="object-position:1.9231% 9.7917%;">
```
