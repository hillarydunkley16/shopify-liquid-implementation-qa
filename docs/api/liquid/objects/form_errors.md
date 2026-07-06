---
title: 'Liquid objects: form_errors'
description: >-
  The error category strings for errors from a form created by a [`form`
  tag](/docs/api/liquid/tags/form).
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/form_errors'
  md: 'https://shopify.dev/docs/api/liquid/objects/form_errors.md'
api_name: liquid
---

# form\_​errors

The error category strings for errors from a form created by a [`form` tag](https://shopify.dev/docs/api/liquid/tags/form).

The following table outlines the strings that can be returned and the reason that they would be:

| Form property name | Return reason |
| - | - |
| `author` | There were issues with required name fields. |
| `body` | There were issues with required text content fields. |
| `email` | There were issues with required email fields. |
| `form` | There were general issues with the form. |
| `password` | There were issues with required password fields. |

## Properties

* * **messages**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The translated error messages for each value in the `form_errors` array.

    You can access a specific message in the array by using a specific error from the `form_errors` array as a key.

  * **translated\_​fields**

    array of [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The translated names for each value in the `form_errors` array.

    You can access a specific field in the array by using a specific error from the `form_errors` array as a key.

##### Example

```json
{
  "messages": {},
  "translated_fields": {}
}
```

### Output form errors

You can output the name of the field related to the error, and the error message, by using the error as a key to access the `translated_fields` and `messages` properties.

```liquid
<ul>
  {% for error in form.errors %}
    <li>
      {% if error == 'form' %}
        {{ form.errors.messages[error] }}
      {% else %}
        {{ form.errors.translated_fields[error] }} - {{ form.errors.messages[error] }}
      {% endif %}
    </li>
  {% endfor %}
</ul>
```
