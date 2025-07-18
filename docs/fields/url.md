# Url

## Overview

**Element Name:** `URL`  
**Type:** string  
**Architecture:** Simple  
**Required:** Yes  

Unique product page URL that displays price and add-to-cart option. Maximum 300 characters. Must be unique for each product variant.



## General Constraints

- **Required field** - must be present in the XML
- **Maximum length:** 300 characters
- **Pattern:** `https?://[^\s]{1,290}`

## XML Examples

```xml
<URL>https://example.com/product/123</URL>
```




