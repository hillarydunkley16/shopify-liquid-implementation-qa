---
title: 'Liquid objects: remote_shop'
description: Information about a remote store.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/remote_shop'
  md: 'https://shopify.dev/docs/api/liquid/objects/remote_shop.md'
api_name: liquid
---

# remote\_​shop

Information about a remote store.

Remote store information is only present via remote details, if the product comes from a remote source (i.e. a product from another store).

## Properties

* * **brand**

    [brand](https://shopify.dev/docs/api/liquid/objects/brand)

  * The [brand assets](https://help.shopify.com/manual/promoting-marketing/managing-brand-assets) for the remote store.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The name of the remote store.

  * **policies**

    array of [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The shipping and refund policies for the remote store.

    The policies are set in the remote store's [Policies settings](https://www.shopify.com/admin/settings/legal).

  * **refund\_​policy**

    [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The refund policy for the remote store.

  * **shipping\_​policy**

    [policy](https://shopify.dev/docs/api/liquid/objects/policy)

  * The shipping policy for the remote store.

### Returned by

* [remote\_​product.remote\_​details](https://shopify.dev/docs/api/liquid/objects/remote_product#remote_product-remote_details)
* [remote\_​details.shop](https://shopify.dev/docs/api/liquid/objects/remote_details#remote_details-shop)
