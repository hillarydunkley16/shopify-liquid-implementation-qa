---
title: 'Liquid objects: user'
description: The author of a blog article.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/user'
  md: 'https://shopify.dev/docs/api/liquid/objects/user.md'
api_name: liquid
---

# user

The author of a blog article.

***

**Tip:** The information returned by the \<code>user\</code> object can be edited on the \<a href="https://www\.shopify.com/admin/settings/account">\<strong>Account\</strong> page\</a> of the Shopify admin.

***

## Properties

* * **account\_​owner**

    [boolean](https://shopify.dev/docs/api/liquid/basics#boolean)

  * Returns `true` if the author is the account owner of the store. Returns `false` if not.

  * **bio**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The bio associated with the author's account.

    If no bio is specified, then `nil` is returned.

  * **email**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The email associated with the author's account.

  * **first\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The first name associated with the author's account.

  * **homepage**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The URL for the personal website associated with the author's account.

    If no personal website is specified, then `nil` is returned.

  * **image**

    [image](https://shopify.dev/docs/api/liquid/objects/image)

  * The image associated with the author's account.

    If no image is specified, then `nil` is returned.

  * **last\_​name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The last name associated with the author's account.

  * **name**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The first and last name associated with the author's account.

##### Example

```json
{
  "account_owner": false,
  "bio": "Polina got her first cauldron at the tender age of six, and she has been passionate about potions ever since!!",
  "email": "polinas.potent.potions@gmail.com",
  "first_name": "Polina",
  "homepage": null,
  "image": {},
  "last_name": "Waters",
  "name": "Polina Waters"
}
```
