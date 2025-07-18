# Gift

## Overview

**Element Name:** `GIFT`  
**Type:** string  
**Architecture:** Attribute based  
**Required:** No  
**Multiple:** Yes  

Gift item with description and ID. Content describes the gift (max 250 characters), ID attribute references the gift product.


## Attribute-Based Field

This field has both text content and XML attributes.

**Text content max length:** 250 characters

### Attributes

#### ID

- **Type:** string
- **Required:** No
- **Description:** Gift product identifier referencing another ITEM_ID.
- **Max Length:** 36
- **Pattern:** `[a-zA-Z0-9_-]{1,36}`
- **Examples:** gift_123


## General Constraints

- **Optional field** - can be omitted
- **Multiple occurrences** allowed

## XML Examples

```xml
<GIFT ID="gift_123">Free wireless headphones</GIFT>
```




