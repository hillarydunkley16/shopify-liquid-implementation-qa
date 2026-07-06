---
title: 'Liquid objects: filter_value_display'
description: The visual representation of a filter value.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/filter_value_display'
  md: 'https://shopify.dev/docs/api/liquid/objects/filter_value_display.md'
api_name: liquid
---

# filter\_​value\_​display

The visual representation of a filter value.

**deprecated:**

Deprecated in favor of the [swatch](https://shopify.dev/docs/api/liquid/objects/swatch) drop.

## Properties

* * **type**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The type of visual representation.

    | Possible values |
    | - |
    | colors |
    | image |

  * **value**

  * The visual representation.

    Can be a list of [`colors`](https://shopify.dev/docs/api/liquid/objects/color) or an [`image`](https://shopify.dev/docs/api/liquid/objects/image). Refer to the [`type`](#filter_value_display-type) property to determine the type of visual representation.

### Returned by

* [filter\_​value.display](https://shopify.dev/docs/api/liquid/objects/filter_value#filter_value-display)
