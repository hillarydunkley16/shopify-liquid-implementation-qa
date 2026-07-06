---
title: 'Liquid filters: product_img_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for a [product image](/docs/api/liquid/objects/product).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/product_img_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/product_img_url.md'
api_name: liquid
---

# product\_​img\_​url

```oobleck
variable | product_img_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for a [product image](https://shopify.dev/docs/api/liquid/objects/product).

This can be the product's `featured_image` or any image from the `images` array.

**Deprecated:**

The `product_img_url` filter has been replaced by [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

##### Code

```liquid
{{ product.featured_image | product_img_url }}
```

##### Data

```json
{
  "product": {
    "featured_image": "files/science-beakers-blue-light-new.jpg"
  }
}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_small.jpg?v=1683744744
```

### The size parameter

```oobleck
image | product_img_url: string
```

By default, the `product_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size).

##### Code

```liquid
{{ product.images[0] | product_img_url: 'large' }}
```

##### Data

```json
{
  "product": {
    "images": [
      "files/science-beakers-blue-light-new.jpg",
      "products/science-beakers-blue-light.jpg",
      "files/science-beakers-blue-light_9c5badcd-ea54-4ddc-916c-a45c6c67c704.jpg",
      "files/science-beakers-blue-light_40984233-47bf-4b8b-844c-88020e3da712.jpg"
    ]
  }
}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/files/science-beakers-blue-light-new_large.jpg?v=1683744744
```
