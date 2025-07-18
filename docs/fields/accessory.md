# Accessory

## Overview

**Element Name:** `ACCESSORY`  
**Type:** string  
**Architecture:** Simple  
**Required:** No  
**Multiple:** Yes (max 10)  

Related accessory product ITEM_ID. Maximum 10 accessories can be specified for cross-selling.



## General Constraints

- **Optional field** - can be omitted
- **Multiple occurrences** allowed (maximum 10)
- **Maximum length:** 36 characters
- **Pattern:** `[a-zA-Z0-9_-]{1,36}`

## XML Examples

```xml
<ACCESSORY>CASE_123</ACCESSORY>
```

```xml
<ACCESSORY>CHARGER_456</ACCESSORY>
```




