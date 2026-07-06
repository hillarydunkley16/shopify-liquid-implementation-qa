---
title: 'Liquid filters: link_to'
description: Generates an HTML `<a>` tag.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/link_to'
  md: 'https://shopify.dev/docs/api/liquid/filters/link_to.md'
api_name: liquid
---

# link\_​to

```oobleck
string | link_to: string
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<a>` tag.

##### Code

```liquid
{{ 'Shopify' | link_to: 'https://www.shopify.com' }}
```

##### Output

```html
<a href="https://www.shopify.com" title="" rel="nofollow">Shopify</a>
```

### HTML attributes

```oobleck
string | link_to_type: attribute: string
```

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attributes) by including a parameter that matches the attribute name, and the desired value.

##### Code

```liquid
{{ 'Shopify' | link_to: 'https://www.shopify.com', class: 'link-class' }}
```

##### Output

```html
<a class="link-class" href="https://www.shopify.com" rel="nofollow">Shopify</a>
```
