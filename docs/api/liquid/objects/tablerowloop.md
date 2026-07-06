---
title: 'Liquid objects: tablerowloop'
description: 'Information about a parent [`tablerow` loop](/docs/api/liquid/tags/tablerow).'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/tablerowloop'
  md: 'https://shopify.dev/docs/api/liquid/objects/tablerowloop.md'
api_name: liquid
---

# tablerowloop

Information about a parent [`tablerow` loop](https://shopify.dev/docs/api/liquid/tags/tablerow).

## Properties

* * **col**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the current column.

  * **col\_​first**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the current column is the first in the row. Returns `false` if not.

  * **col\_​last**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the current column is the last in the row. Returns `false` if not.

  * **col0**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 0-based index of the current column.

  * **first**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the current iteration is the first. Returns `false` if not.

  * **index**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the current iteration.

  * **index0**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 0-based index of the current iteration.

  * **last**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the current iteration is the last. Returns `false` if not.

  * **length**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The total number of iterations in the loop.

  * **rindex**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of the current iteration, in reverse order.

  * **rindex0**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 0-based index of the current iteration, in reverse order.

  * **row**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The 1-based index of current row.

##### Example

```json
{
  "col": 1,
  "col0": 0,
  "col_first": true,
  "col_last": false,
  "first": true,
  "index": 1,
  "index0": 0,
  "last": false,
  "length": 5,
  "rindex": 5,
  "rindex0": 4,
  "row": 1
}
```
