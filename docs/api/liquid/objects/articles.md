---
title: 'Liquid objects: articles'
description: All of the articles across the blogs in the store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/articles'
  md: 'https://shopify.dev/docs/api/liquid/objects/articles.md'
api_name: liquid
---

# articles

All of the articles across the blogs in the store.

### Directly accessible in

* Global

You can use `articles` to access an article by its [handle](https://shopify.dev/docs/api/liquid/basics#handles).

##### Code

```liquid
{% assign article = articles['potion-notions/new-potions-for-spring'] %}
{{ article.title | link_to: article.url }}
```

##### Output

```html
<a href="/blogs/potion-notions/new-potions-for-spring" title="">New potions for spring</a>
```
