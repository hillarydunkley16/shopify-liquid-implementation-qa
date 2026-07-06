---
title: 'Liquid filters: link_to_type'
description: >-
  Generates an HTML `<a>` tag with an `href` attribute linking to a [collection
  page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection)
  that lists all products of the given

  product type.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/link_to_type'
  md: 'https://shopify.dev/docs/api/liquid/filters/link_to_type.md'
api_name: liquid
---

# link\_​to\_​type

```oobleck
string | link_to_type
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<a>` tag with an `href` attribute linking to a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products of the given product type.

##### Code

```liquid
{{ 'Health' | link_to_type }}
```

##### Output

```html
<a href="/collections/types?q=Health" title="Health">Health</a>
```

### HTML attributes

```oobleck
string | link_to_type: attribute: string
```

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attributes) by including a parameter that matches the attribute name, and the desired value.

##### Code

```liquid
{{ 'Health' | link_to_type: class: 'link-class' }}
```

##### Output

```html
<a class="link-class" href="/collections/types?q=Health" title="Health">Health</a>
```
