---
title: "Reporting Views [Deprecated]"
slug: "reporting-views"
excerpt: ""
hidden: false
createdAt: "Tue Sep 01 2020 11:59:57 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 12:04:24 GMT+0000 (Coordinated Universal Time)"
---
Avni has a generic data model to support the dynamic creation of forms. For new implementers wanting to write custom reports, this can be overwhelming and complex.  
To ease the creation of reports, Avni generates simplified database views with one view corresponding to each form.

## Creating / Refreshing Reporting Views

You can create views for reporting by going to the `Reporting Views` option in the app designer and clicking on `create/refresh view`. For each form, one view is created with all the questions as the columns in the view. 

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f47db05-Screen_Shot_2020-09-04_at_9.28.47_AM.png",
        "Screen Shot 2020-09-04 at 9.28.47 AM.png",
        3356
      ],
      "caption": "App Designer Reporting Views Screen"
    }
  ]
}
[/block]


You can see the view definition by clicking on the expand button, and delete the view by clicking on the delete button.

The views would be accessible in Metabase or any other reporting tool the implementation may be using.

## Naming convention

As PostgreSQL doesn't allow identifiers of length more than 63 bytes, we follow these naming conventions as long as the view name is below 63 characters.

| Form type                      | View name                                                                     |
| :----------------------------- | :---------------------------------------------------------------------------- |
| Registration                   | `{UsernameSuffix}_{SubjectTypeName}`                                          |
| Encounter                      | `{UsernameSuffix}_{SubjectTypeName}_{encounterTypeName}`                      |
| Encounter Cancellation         | `{UsernameSuffix}_{SubjectTypeName}_{encounterTypeName}_cancel`               |
| Program Enrolment              | `{UsernameSuffix}_{SubjectTypeName}_{ProgramName}`                            |
| Program Exit                   | `{UsernameSuffix}_{SubjectTypeName}_{ProgramName}_exit`                       |
| Program Encounter              | `{UsernameSuffix}_{SubjectTypeName}_{ProgramName}_{EncounterTypeName}`        |
| Program Encounter Cancellation | `{UsernameSuffix}_{SubjectTypeName}_{ProgramName}_{EncounterTypeName}_cancel` |

If the view name exceeds 63 characters we trim some parts from different entity type names to keep it below 63 characters. For trimming, we follow the below rule.

_{UsernameSuffix}_{First 6 characters of SubjectTypeName}_{First 6 characters of ProgramName}\_{First 20 characters of EncounterTypeName}_

Some view names exceed the character limit even after the above optimisation. In such a case we take away the last few characters and replace them with the hashcode of the full name. Hashcode is used so that the name remains unique.
