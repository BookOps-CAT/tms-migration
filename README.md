# tms-migration
Scripts to reconcile and serialize to MARC21 TMS metadata.

## Work notes

### (9/5/2024)
#### Objects count by department:
+ 'Photography Collection' (1) has 275592 objects.
+ 'Print Collection' (2) has 60461 objects.
+ 'Spencer Collection' (3) has 5728 objects.
+ 'Other NYPL' (10) has 84 objects.
+ 'DL' (12) has 2155 objects.
+ 'Art & Architecture' (13) has 193 objects.
+ 'Paintings & Sculpture' (14) has 157 objects.
+ 'Ephemera' (16) has 92509 objects.
+ 'Picture Collection' (18) has 10009 objects.
+ 'DEACCESSIONED' (49) has 39 objects.
+ 'LPA DANCE' (50) has 76 objects.
### Missing tables in Tony's DB copy (8/22/2024)
+ AddressType, ConAddresses, ConEMail, ConPhones, EMailType tbls: consult with Wallach staff; export to a sheet?
+ AltNum tbl: use TableID & ID to figure out the relation to Objects or Constituents tbls
+ AuthorityAltNum tbl: DID NOT SEE IT AMONG EXPORTED TABLES! may include valuable data
+ Associations, AssocParents & Relationships tbls: may be useful in figuring out the relation between different objects
+ AuthorityAltNums tbl: links to authority records for constituents; have not see it!
+ Classification tbl: use to map bibliographic record type and Sierra material type
+ Conditions tbl: use to map item fixed fields and notes regarding poor condition
+ ConTypes tbl: needed for Constituents tbl to properly code in MARC (700 vs 710, for example) if no authority link is available; different than role!
+ DimensionElements & DimItemElemXrefs tbls: easier mapping than from Objects tbl where displayed valued are concatenated
+ Exhibitions, ExhibitionTitles, ExhObjXref tbls: Virginia suggested mapping to 585 MARC field; data needed
+ ObjGeography tbl: columns for different geographical names
+ RoleType vs RolesTypes = duplicate table? Ask Tony
+ FlabLables & StatusFlag tbls: map to item record coding?
+ Terms, TermTypes, TermMasterThes, ThesXrefs (includes relation to Object, Constituents), ThesXrefTypes, ThesaurusBases tbls: 6xx MARC fields
+ TextEntries, TextTypes tbls: needed for bib mapping, captions, etc. 