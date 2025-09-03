---
title: "Migrate location of subject"
slug: "migrate-location-of-subject"
excerpt: ""
hidden: false
createdAt: "Mon Nov 06 2023 10:04:52 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Jan 22 2024 07:41:56 GMT+0000 (Coordinated Universal Time)"
---
# Please refer to API Doc

<https://editor.swagger.io/?url=https://raw.githubusercontent.com/avniproject/avni-server/master/avni-server-api/src/main/resources/api/external-api.yaml>

# Documentation Deprecated

Since there are multiple entities that need to be changed, the migration should not be done by making changes directly to the database using SQL commands. In order to migrate a subject use the follow API.

### Endpoint

`{{origin}}/subjectMigration/bulk`

e.g. <https://app.avniproject.org/subjectMigration/bulk>

### Headers

`auth-token`

### Body

- destinationAddresses is a map of source address level id and destination address level id.
- subject type ids is an array of subject types that you want migrated

```Text JSON
{
    "destinationAddresses": {
        "330785": "330856",
        "334657": "335043",
        "331106": "331466"
    },
    "subjectTypeIds": [
        672,
        671
    ]
}
```

### Also know

- if you have a lot of addresses then the request may timeout, but the server will continue to process
- Each source to destination mapping for each subject type, will be done in its own transaction. So for above example there will be 6 transactions (3 address mapping multiplied by 2 subject types).
