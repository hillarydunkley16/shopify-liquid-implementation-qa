---
title: 'Liquid filters: slice'
description: >-
  Returns a substring or series of array items, starting at a given 0-based
  index.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/slice'
  md: 'https://shopify.dev/docs/api/liquid/filters/slice.md'
api_name: liquid
---

# slice

```oobleck
string | slice
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Returns a substring or series of array items, starting at a given 0-based index.

By default, the substring has a length of one character, and the array series has one array item. However, you can provide a second parameter to specify the number of characters or array items.

##### Code

```liquid
{{ collection.title | slice: 0 }}
{{ collection.title | slice: 0, 5 }}

{{ collection.all_tags | slice: 1, 2 | join: ', ' }}
```

##### Data

```json
{
  "collection": {
    "all_tags": [
      "Burning",
      "dried",
      "extra-potent",
      "extracts",
      "fresh",
      "healing",
      "ingredients",
      "music",
      "plant",
      "Salty",
      "supplies"
    ],
    "title": "Products"
  }
}
```

##### Output

```html
P
Produ

dried, extra-potent
```

### Negative index

You can supply a negative index which will count from the end of the string.

##### Code

```liquid
{{ collection.title | slice: -3, 3 }}
```

##### Data

```json
{
  "collection": {
    "title": "Products"
  }
}
```

##### Output

```html
cts
```
