---
title: 'Liquid objects: current_page'
description: The current page number.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/current_page'
  md: 'https://shopify.dev/docs/api/liquid/objects/current_page.md'
api_name: liquid
---

# current\_​page

The current page number.

The `current_page` object has a value of 1 for non-paginated resources.

### Directly accessible in

* Global

##### Code

```liquid
{{ page_title }}{% unless current_page == 1 %} - Page {{ current_page }}{% endunless %}
```

##### Output

```html
Ingredients - Page 2
```
