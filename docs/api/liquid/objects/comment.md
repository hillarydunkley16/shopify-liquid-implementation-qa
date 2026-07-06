---
title: 'Liquid objects: comment'
description: An article comment.
source_url:
  html: 'https://shopify.dev/docs/api/liquid/objects/comment'
  md: 'https://shopify.dev/docs/api/liquid/objects/comment.md'
api_name: liquid
---

# comment

An article comment.

## Properties

* * **author**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The full name of the author of the comment.

  * **content**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The content of the comment.

  * **created\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the comment was created.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **email**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The email of he author of the comment.

  * **id**

    [number](https://shopify.dev/docs/api/liquid/basics#number)

  * The ID of the comment.

  * **status**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The status of the comment. Always returns `published`.

    Outside of the Liquid context, the status of a comment can vary based on spam detection and whether blog comments are moderated. However, only comments with a status of `published` are included in the [`article.comments` array](https://shopify.dev/docs/api/liquid/objects/article#article-comments).

    **Tip:** To learn more about blog comments, visit the \<a href="https://help.shopify.com/manual/online-store/blogs/managing-comments">Shopify Help Center\</a>.

  * **updated\_​at**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * A timestamp for when the status of the comment was last updated.

    **Tip:** Use the \<a href="/docs/api/liquid/filters/date">\<code>date\</code> filter\</a> to format the timestamp.

  * **url**

    [string](https://shopify.dev/docs/api/liquid/basics#string)

  * The relative URL of the article that the comment is associated with, with [`comment.id`](https://shopify.dev/docs/api/liquid/objects/comment#comment-id) appended.

##### Example

```json
{
  "author": "Cornelius",
  "content": "Wow, this is going to save me a fortune in invisibility potion!",
  "created_at": "2022-06-05 19:33:57 -0400",
  "email": "cornelius.potionmaker@gmail.com",
  "id": 129089273921,
  "status": "published",
  "updated_at": "2022-06-05 19:33:57 -0400",
  "url": "/blogs/potion-notions/how-to-tell-if-you-have-run-out-of-invisibility-potion#129089273921"
}
```
