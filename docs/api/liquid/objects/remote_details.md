---
title: 'Liquid objects: remote_details'
description: Information about the remote source from which the object came from.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/remote_details'
  md: 'https://shopify.dev/docs/api/liquid/objects/remote_details.md'
api_name: liquid
---

# remote\_​details

Information about the remote source from which the object came from.

Remote details can only be accessed on an object that comes from a remote source, such as a product from another store.

## Properties

* * **shop**

    [remote\_shop](https://shopify.dev/docs/api/liquid/objects/remote_shop)

  * Information about the store that the remote object came from.

  * **type**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * Provides context on how the remote object was surfaced. Currently the only supported value is "seller", but this may be expanded in the future.

### Returned by

* [remote\_​product](https://shopify.dev/docs/api/liquid/objects/remote_product)
* [remote\_​product.remote\_​details](https://shopify.dev/docs/api/liquid/objects/remote_product#remote_product-remote_details)
