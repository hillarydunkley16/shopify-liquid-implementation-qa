---
title: 'Liquid filters: link_to_vendor'
description: >-
  Generates an HTML `<a>` tag with an `href` attribute linking to a [collection
  page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection)
  that lists all products of a given

  product vendor.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/link_to_vendor'
  md: 'https://shopify.dev/docs/api/liquid/filters/link_to_vendor.md'
api_name: liquid
---

# link\_​to\_​vendor

```oobleck
string | link_to_vendor
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Generates an HTML `<a>` tag with an `href` attribute linking to a [collection page](https://shopify.dev/docs/storefronts/themes/architecture/templates/collection) that lists all products of a given product vendor.

##### Code

```liquid
{{ "Polina's Potent Potions" | link_to_vendor }}
```

##### Output

```html
<a href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>
```

### HTML attributes

```oobleck
string | link_to_vendor: attribute: string
```

You can specify [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a#attributes) by including a parameter that matches the attribute name, and the desired value.

##### Code

```liquid
{{ "Polina's Potent Potions" | link_to_vendor: class: 'link-class' }}
```

##### Output

```html
<a class="link-class" href="/collections/vendors?q=Polina%27s%20Potent%20Potions" title="Polina&#39;s Potent Potions">Polina's Potent Potions</a>
```
