---
title: 'Liquid filters: article_img_url'
description: >-
  Returns the [CDN URL](/themes/best-practices/performance/platform#shopify-cdn)
  for an [article's image](/docs/api/liquid/objects/article#article-image).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/article_img_url'
  md: 'https://shopify.dev/docs/api/liquid/filters/article_img_url.md'
api_name: liquid
---

# article\_​img\_​url

```oobleck
variable | article_img_url
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns the [CDN URL](https://shopify.dev/themes/best-practices/performance/platform#shopify-cdn) for an [article's image](https://shopify.dev/docs/api/liquid/objects/article#article-image).

**Deprecated:**

The `article_img_url` filter has been replaced by [`image_url`](https://shopify.dev/docs/api/liquid/filters/image_url).

##### Code

```liquid
{{ article.image | article_img_url }}
```

##### Data

```json
{
  "article": {
    "image": "articles/beakers-for-science-with-water.jpg"
  }
}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/articles/beakers-for-science-with-water_small.jpg?v=1654385193
```

### size

```oobleck
image | article_img_url: string
```

By default, the `article_img_url` filter returns the `small` version of the image (100 x 100 px). However, you can specify a [size](https://shopify.dev/docs/api/liquid/filters/img_url#img_url-size).

##### Code

```liquid
{{ article.image | article_img_url: 'large' }}
```

##### Data

```json
{
  "article": {
    "image": "articles/beakers-for-science-with-water.jpg"
  }
}
```

##### Output

```html
//polinas-potent-potions.myshopify.com/cdn/shop/articles/beakers-for-science-with-water_large.jpg?v=1654385193
```
