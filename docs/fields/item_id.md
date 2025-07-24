# Item Id

## Overview

**Element Name:** `ITEM_ID`<br>
**Type:** string<br>
**Architecture:** Simple<br>
**Required:** Yes<br>

Unique product identifier within the e-shop. Maximum 36 characters.
Allowed characters: a-z, A-Z, 0-9, underscore, hyphen.


## General Constraints

- **Required field** - must be present in the XML
- **Maximum length:** 36 characters
- **Pattern:** `[a-zA-Z0-9_-]{1,36}`

## XML Examples

```xml
<ITEM_ID>product_123</ITEM_ID>
```




