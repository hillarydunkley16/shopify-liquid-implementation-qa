---
title: 'Liquid tags: cycle'
description: >-
  Loops through a group of strings and outputs them one at a time for each
  iteration of a [`for` loop](/docs/api/liquid/tags/for).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/tags/cycle'
  md: 'https://shopify.dev/docs/api/liquid/tags/cycle.md'
api_name: liquid
---

# cycle

Loops through a group of strings and outputs them one at a time for each iteration of a [`for` loop](https://shopify.dev/docs/api/liquid/tags/for).

The `cycle` tag must be used inside a `for` loop.

***

**Tip:** Use the \<code>cycle\</code> tag to output text in a predictable pattern. For example, to apply odd/even classes to rows in a table.

***

## Syntax

```oobleckTag
{% cycle string, string, ... %}
```

##### Code

```liquid
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}
```

##### Output

```html
one
two
three
one
```

### Create unique cycle groups

## Syntax

```oobleckTag
{% cycle string: string, string, ... %}
```

If you include multiple `cycle` tags with the same parameters, in the same template, then each set of tags is treated as the same group. This means that it's possible for a `cycle` tag to output any of the provided strings, instead of always starting at the first string. To account for this, you can specify a group name for each `cycle` tag.

##### Code

```liquid
<!-- Iteration 1 -->
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 2 -->
{% for i in (1..4) -%}
  {% cycle 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 3 -->
{% for i in (1..4) -%}
  {% cycle 'group_1': 'one', 'two', 'three' %}
{%- endfor %}

<!-- Iteration 4 -->
{% for i in (1..4) -%}
  {% cycle 'group_2': 'one', 'two', 'three' %}
{%- endfor %}
```

##### Output

```html
<!-- Iteration 1 -->
one
two
three
one


<!-- Iteration 2 -->
two
three
one
two


<!-- Iteration 3 -->
one
two
three
one


<!-- Iteration 4 -->
one
two
three
one
```
