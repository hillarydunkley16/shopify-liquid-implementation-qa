---
title: 'Liquid filters: join'
description: >-
  Combines all of the items in an array into a single string, separated by a
  space.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/filters/join'
  md: 'https://shopify.dev/docs/api/liquid/filters/join.md'
api_name: liquid
---

# join

```oobleck
array | join
```

returns [string](https://shopify.dev/docs/api/liquid/basics#string)

Combines all of the items in an array into a single string, separated by a space.

##### Code

```liquid
{{ collection.all_tags | join }}
```

##### Data

```json
{
  "collection": {
    "all_tags": [
      "extra-potent",
      "fresh",
      "healing",
      "ingredients"
    ]
  }
}
```

##### Output

```html
extra-potent fresh healing ingredients
```

### Custom separator

```oobleck
array | join: string
```

You can specify a custom separator for the joined items.

##### Code

```liquid
{{ collection.all_tags | join: ', ' }}
```

##### Data

```json
{
  "collection": {
    "all_tags": [
      "extra-potent",
      "fresh",
      "healing",
      "ingredients"
    ]
  }
}
```

##### Output

```html
extra-potent, fresh, healing, ingredients
```
