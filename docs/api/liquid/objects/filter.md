---
title: 'Liquid objects: filter'
description: >-
  A [storefront
  filter](https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/filter'
  md: 'https://shopify.dev/docs/api/liquid/objects/filter.md'
api_name: liquid
---

# filter

A [storefront filter](https://help.shopify.com/manual/online-store/themes/customizing-themes/storefront-filters).

To learn about supporting filters in your theme, refer to [Support storefront filtering](https://shopify.dev/themes/navigation-search/filtering/storefront-filtering/support-storefront-filtering).

## Properties

* * **active\_​values**

    array of [filter\_value](https://shopify.dev/docs/api/liquid/objects/filter_value)

  * The values of the filter that are currently active.

    The array can have values only for `boolean` and `list` type filters.

  * **false\_​value**

    [filter\_value](https://shopify.dev/docs/api/liquid/objects/filter_value)

  * The `false` filter value.

    Returns a value for `boolean` type filters if the unfiltered view has at least one result with the `false` filter value. Otherwise, it returns `nil`.

  * **inactive\_​values**

    array of [filter\_value](https://shopify.dev/docs/api/liquid/objects/filter_value)

  * The values of the filter that are currently inactive.

    The array can have values only for `boolean` and `list` type filters.

  * **label**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The customer-facing label for the filter.

  * **max\_​value**

    [filter\_value](https://shopify.dev/docs/api/liquid/objects/filter_value)

  * The highest filter value.

    Returns a value only for `price_range` type filters. Returns `nil` for other types.

  * **min\_​value**

    [filter\_value](https://shopify.dev/docs/api/liquid/objects/filter_value)

  * The lowest filter value.

    Returns a value only for `price_range` type filters. Returns `nil` for other types.

  * **operator**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The logical operator used by the filter. Returns a value only for `boolean` and `list` type filters. Returns `nil` for other types.

    Example: For a filter named `color` with values `red` and `blue`:

    * If the operator is `AND`, it will filter items that are both red and blue.
    * If the operator is `OR`, it will filter items that are either red or blue or both.

    Filters that support the `AND` operator:

    * Product tags
    * Metafields of type `list.single_line_text_field` and `list.metaobject_reference`

    | Possible values | Description |
    | - | - |
    | AND | Includes products that match all buyer selections. |
    | OR | Includes products that match at least one buyer selection. |

  * **param\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL parameter for the filter. For example, `filter.v.option.color`.

  * **presentation**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * Describes how to present the filter values.

    Returns a value only for `list` type filters. Returns `nil` for other types.

    | Possible values |
    | - |
    | image |
    | swatch |
    | text |

  * **range\_​max**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The highest product price within the collection or search results.

    Returns a value only for `price_range` type filters. Returns `nil` for other types.

  * **true\_​value**

    [filter\_value](https://shopify.dev/docs/api/liquid/objects/filter_value)

  * The `true` filter value.

    Returns a value for `boolean` type filters if the unfiltered view has at least one result with the `true` filter value. Otherwise, it returns `nil`.

  * **type**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The type of the filter.

    | Possible values |
    | - |
    | boolean |
    | list |
    | price\_range |

  * **url\_​to\_​remove**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The current page URL with the URL parameter related to the filter removed.

  * **values**

    array of [filter\_value](https://shopify.dev/docs/api/liquid/objects/filter_value)

  * The values of the filter.

    The array can have values only for `boolean` and `list` type filters.

### Returned by

* [collection.filters](https://shopify.dev/docs/api/liquid/objects/collection#collection-filters)
* [search.filters](https://shopify.dev/docs/api/liquid/objects/search#search-filters)
