---
title: 'Liquid objects: template'
description: 'Information about the current [template](/docs/themes/architecture/templates).'
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/template'
  md: 'https://shopify.dev/docs/api/liquid/objects/template.md'
api_name: liquid
---

# template

Information about the current [template](https://shopify.dev/docs/themes/architecture/templates).

## Properties

* * **directory**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the template's parent directory.

    Returns `nil` if the template's parent directory is `/templates`.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string) from a set of values

  * The name of the template's [type](https://shopify.dev/docs/themes/architecture/templates#template-types).

    | Possible values |
    | - |
    | 404 |
    | article |
    | blog |
    | cart |
    | collection |
    | list-collections |
    | customers/account |
    | customers/activate\_account |
    | customers/addresses |
    | customers/login |
    | customers/order |
    | customers/register |
    | customers/reset\_password |
    | gift\_card |
    | index |
    | page |
    | password |
    | product |
    | search |

  * **suffix**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The custom name of an [alternate template](https://shopify.dev/themes/architecture/templates#alternate-templates).

    Returns `nil` if the default template is being used.

##### Example

```json
{
  "directory": null,
  "name": "product",
  "suffix": null
}
```
