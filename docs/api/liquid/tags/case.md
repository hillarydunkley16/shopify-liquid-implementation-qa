---
title: 'Liquid tags: case'
description: Renders a specific expression depending on the value of a specific variable.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/case'
  md: 'https://shopify.dev/docs/api/liquid/tags/case.md'
api_name: liquid
---

# case

Renders a specific expression depending on the value of a specific variable.

## Syntax

```oobleckTag
{% case variable %}
  {% when first_value %}
    first_expression
  {% when second_value %}
    second_expression
  {% else %}
    third_expression
{% endcase %}
```

### variable

The name of the variable you want to base your case statement on.

### first\_value

A specific value to check for.

### second\_value

A specific value to check for.

### first\_expression

An expression to be rendered when the variable's value matches `first_value`.

### second\_expression

An expression to be rendered when the variable's value matches `second_value`.

### third\_expression

An expression to be rendered when the variable's value has no match.

##### Code

```liquid
{% case product.type %}
  {% when 'Health' %}
    This is a health potion.
  {% when 'Love' %}
    This is a love potion.
  {% else %}
    This is a potion.
{% endcase %}
```

##### Data

```json
{
  "product": {
    "type": null
  }
}
```

##### Output

```html
This is a health potion.
```

### Multiple values

## Syntax

```oobleckTag
{% case variable %}
  {% when first_value or second_value or third_value %}
    first_expression
  {% when fourth_value, fifth_value, sixth_value %}
    second_expression
  {% else %}
    third_expression
{% endcase %}
```

A `when` tag can accept multiple values. When multiple values are provided, the expression is returned when the variable matches any of the values inside of the tag. Provide the values as a comma-separated list, or separate them using an `or` operator.

##### Code

```liquid
{% case product.type %}
  {% when 'Love' or 'Luck' %}
    This is a love or luck potion.
  {% when 'Strength','Health' %}
    This is a strength or health potion.
  {% else %}
    This is a potion.
{% endcase %}
```

##### Data

```json
{
  "product": {
    "type": null
  }
}
```

##### Output

```html
This is a strength or health potion.
```
