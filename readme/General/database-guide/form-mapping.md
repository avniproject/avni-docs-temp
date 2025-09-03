---
title: "Form Mapping"
slug: "form-mapping"
excerpt: ""
hidden: false
createdAt: "Fri Jan 05 2018 14:55:28 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 12:04:24 GMT+0000 (Coordinated Universal Time)"
---
**What does form mapping do?**  
Forms are an important part of Avni. Before trying to understand forms it is required to understand what are key entities which hold the transaction data in Avni.

- Individual (or Subject)
- Encounter
- Program Enrolment
- Program Encounter
- Program Exit

Each of these entities has some core data and configurable data. Configurable or dynamic data is modelled using forms.

- **Individual** has one form (for Registration) for each subject type.
- **Encounter** can be of multiple encounter types and for each encounter type, there is one form.
- An individual can be enrolled in multiple programs hence for each **Program Enrolment** there will be a form. Corresponding to each enrolment there is usually exit data which is captured via forms.
- An individual can be registered in different programs, and within each program, there can be multiple types of **Program Encounters** (hence forms).

Form Mapping tries to model this relationship between Programs, ProgramEncounters or NonProgram Encounters and their Forms. Form Mapping has the following key fields. In the column header for Program and Encounter Type, we have the current name for the database columns and domain class fields in the brackets which will be renamed to more understandable names, soon.

This is depicted in tabular form below (with an added Form Type dimension). 

| Form Type         | entity_id  | observations_type_entity_id | subject_type_id |
| :---------------- | :--------- | :-------------------------- | :-------------- |
| Individual        | null       | null                        | subject_type.id |
| Encounter         | null       | encounter_type.id           | subject_type.id |
| Program Enrolment | program.id | null                        | subject_type.id |
| Program Encounter | program.id | encounter_type.id           | subject_type.id |
| Program Exit      | program.id | null                        | subject_type.id |
