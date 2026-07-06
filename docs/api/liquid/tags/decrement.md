---
title: 'Liquid tags: decrement'
description: >-
  Creates a new variable, with a default value of -1, that's decreased by 1 with
  each subsequent call.


  > Caution:

  > Predefined Liquid objects can be overridden by variables with the same name.

  > To make sure that you can access all Liquid objects, make sure that your
  variable name doesn't match a predefined object's name.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/decrement'
  md: 'https://shopify.dev/docs/api/liquid/tags/decrement.md'
api_name: liquid
---

# decrement

Creates a new variable, with a default value of -1, that's decreased by 1 with each subsequent call.

***

**Caution:** Predefined Liquid objects can be overridden by variables with the same name. To make sure that you can access all Liquid objects, make sure that your variable name doesn\&#39;t match a predefined object\&#39;s name.

***

Variables that are declared with `decrement` are unique to the [layout](https://shopify.dev/themes/architecture/layouts), [template](https://shopify.dev/themes/architecture/templates), or [section](https://shopify.dev/themes/architecture/sections) file that they're created in. However, the variable is shared across [snippets](https://shopify.dev/themes/architecture/snippets) included in the file.

Similarly, variables that are created with `decrement` are independent from those created with [`assign`](https://shopify.dev/docs/api/liquid/tags/assign) and [`capture`](https://shopify.dev/docs/api/liquid/tags/capture). However, `decrement` and [`increment`](https://shopify.dev/docs/api/liquid/tags/increment) share variables.

## Syntax

```oobleckTag
{% decrement variable_name %}
```

### variable\_name

The name of the variable being decremented.

##### Code

```liquid
{% decrement variable %}
{% decrement variable %}
{% decrement variable %}
```

##### Output

```html
-1
-2
-3
```
