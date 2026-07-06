---
title: 'Liquid tags: tablerow'
description: Generates HTML table rows for every item in an array.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/tablerow'
  md: 'https://shopify.dev/docs/api/liquid/tags/tablerow.md'
api_name: liquid
---

# tablerow

Generates HTML table rows for every item in an array.

The `tablerow` tag must be wrapped in HTML `<table>` and `</table>` tags.

***

**Tip:** Every \<code>tablerow\</code> loop has an associated \<a href="/docs/api/liquid/objects/tablerowloop">\<code>tablerowloop\</code> object\</a> with information about the loop.

***

## Syntax

```oobleckTag
{% tablerow variable in array %}
  expression
{% endtablerow %}
```

### variable

The current item in the array.

### array

The array to iterate over.

### expression

The expression to render.

##### Code

```liquid
<table>
  {% tablerow product in collection.products %}
    {{ product.title }}
  {% endtablerow %}
</table>
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td><td class="col3">
    Health potion
  </td><td class="col4">
    Invisibility potion
  </td></tr>

</table>
```

## tablerow tag parameters

### cols

## Syntax

```oobleckTag
{% tablerow variable in array cols: number %}
  expression
{% endtablerow %}
```

You can define how many columns the table should have using the `cols` parameter.

##### Code

```liquid
<table>
  {% tablerow product in collection.products cols: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td></tr>
<tr class="row2"><td class="col1">
    Health potion
  </td><td class="col2">
    Invisibility potion
  </td></tr>

</table>
```

### limit

## Syntax

```oobleckTag
{% tablerow variable in array limit: number %}
  expression
{% endtablerow %}
```

You can limit the number of iterations using the `limit` parameter.

##### Code

```liquid
<table>
  {% tablerow product in collection.products limit: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
<table>
  <tr class="row1">
<td class="col1">
    Draught of Immortality
  </td><td class="col2">
    Glacier ice
  </td></tr>

</table>
```

### offset

## Syntax

```oobleckTag
{% tablerow variable in array offset: number %}
  expression
{% endtablerow %}
```

You can specify a 1-based index to start iterating at using the `offset` parameter.

##### Code

```liquid
<table>
  {% tablerow product in collection.products offset: 2 %}
    {{ product.title }}
  {% endtablerow %}
</table>
```

##### Data

```json
{
  "collection": {
    "products": [
      {
        "title": "Draught of Immortality"
      },
      {
        "title": "Glacier ice"
      },
      {
        "title": "Health potion"
      },
      {
        "title": "Invisibility potion"
      }
    ]
  }
}
```

##### Output

```html
<table>
  <tr class="row1">
<td class="col1">
    Health potion
  </td><td class="col2">
    Invisibility potion
  </td></tr>

</table>
```

### range

## Syntax

```oobleckTag
{% tablerow variable in (number..number) %}
  expression
{% endtablerow %}
```

Instead of iterating over specific items in an array, you can specify a numeric range to iterate over.

***

**Note:** You can define the range using both literal and variable values.

***

##### Code

```liquid
<table>
  {% tablerow i in (1..3) %}
    {{ i }}
  {% endtablerow %}
</table>

{%- assign lower_limit = 2 -%}
{%- assign upper_limit = 4 -%}

<table>
  {% tablerow i in (lower_limit..upper_limit) %}
    {{ i }}
  {% endtablerow %}
</table>
```

##### Output

```html
<table>
  <tr class="row1">
<td class="col1">
    1
  </td><td class="col2">
    2
  </td><td class="col3">
    3
  </td></tr>

</table><table>
  <tr class="row1">
<td class="col1">
    2
  </td><td class="col2">
    3
  </td><td class="col3">
    4
  </td></tr>

</table>
```

# tablerowloop**object**

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
