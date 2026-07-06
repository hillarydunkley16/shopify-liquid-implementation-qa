---
title: 'Liquid objects: blogs'
description: All of the blogs in the store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/blogs'
  md: 'https://shopify.dev/docs/api/liquid/objects/blogs.md'
api_name: liquid
---

# blogs

All of the blogs in the store.

### Directly accessible in

* Global

You can use `blogs` to access a blog by its [handle](https://shopify.dev/docs/api/liquid/basics#handles).

##### Code

```liquid
{% for article in blogs.potion-notions.articles %}
  {{- article.title | link_to: article.url }}
{% endfor %}
```

##### Output

```html
<a href="/blogs/potion-notions/homebrew-start-making-potions-at-home" title="">Homebrew: start making potions at home</a>

<a href="/blogs/potion-notions/new-potions-for-spring" title="">New potions for spring</a>

<a href="/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion" title="">How to tell if you're out of invisibility potion</a>
```
