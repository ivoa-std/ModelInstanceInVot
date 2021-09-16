
# Validation Code #

### tests ###

* Set of focused python unit tests; one for each syntax element.
    * executes the Test plan cases for that element
* Rich Instance Tests
    * examples of more complex cases
* VOTable Test
    * ??

### utils ###

* utility methods used in testing.

# Annotation Syntax Test Plan #

| Case          | Description                                   | Valid?                   | Implemented?       |
|:---           |:---                                           |:----                     |:----               | 
|**VODML**      |                                               |                          |                    |
|1.1            | - MODEL + GLOBALS + TEMPLATES                 | :heavy_check_mark:       | :red_circle:       |
|1.2            | - MODEL + GLOBALS                             | :heavy_check_mark:       | :red_circle:       |
|1.3            | - MODEL + TEMPLATES                           | :heavy_check_mark:       | :red_circle:       |
|1.4            | - MODEL only                                  | :heavy_check_mark:       | :red_circle:       |
|1.5            | - empty (missing MODEL)                       | :heavy_multiplication_x: | :red_circle:       |
|1.6            | - GLOBALS + MODEL + TEMPLATES (order)         | :heavy_multiplication_x: | :red_circle:       |
|1.7            | - MODEL + TEMPLATES + GLOBALS (order)         | :heavy_multiplication_x: | :red_circle:       |
|1.8            | - multiple MODEL nodes                        | :heavy_check_mark:       | :red_circle:       |
|1.9            | - multiple TEMPLATES nodes                    | :heavy_check_mark:       | :red_circle:       |
|1.10           | - multiple GLOBALS nodes                      | :heavy_multiplication_x: | :red_circle:       |
|1.11           | - includes other node                         | :heavy_multiplication_x: | :red_circle:       |
|**MODEL**      |                                               |                          |                    |
|2.1            | - name + url (standard syntax)                | :heavy_check_mark:       | :red_circle:       |
|2.2            | - name only                                   | :heavy_check_mark:       | :red_circle:       |
|2.3            | - empty (missing name)                        | :heavy_multiplication_x: | :red_circle:       |
|2.4            | - name=empty                                  | :heavy_multiplication_x: | :red_circle:       |
|2.5            | - url=empty                                   | :heavy_multiplication_x: | :red_circle:       |
|**GLOBALS**    |                                               |                          |                    |
|3.1            | - COLLECTION + INSTANCE                       | :heavy_check_mark:       | :red_circle:       |
|3.2            | - COLLECTION only                             | :heavy_check_mark:       | :red_circle:       |
|3.3            | - INSTANCE only                               | :heavy_check_mark:       | :red_circle:       |
|3.4            | - multiple subnodes (C,I), random order       | :heavy_check_mark:       | :red_circle:       |
|3.5            | - empty, no subnodes                          | :heavy_check_mark:       | :red_circle:       |
|3.6            | - includes other node                         | :heavy_multiplication_x: | :red_circle:       |
|**TEMPLATES**  |                                               |                          |                    |
|4.1            | - WHERE + INSTANCE                            | :heavy_check_mark:       | :red_circle:       |
|4.2            | - INSTANCE only                               | :heavy_check_mark:       | :red_circle:       |
|4.3            | - WHERE only                                  | :heavy_multiplication_x: | :red_circle:       |
|4.4            | - INSTANCE + WHERE (order)                    | :heavy_multiplication_x: | :red_circle:       |
|4.5            | - multiple WHERE                              | :heavy_check_mark:       | :red_circle:       |
|4.6            | - multiple INSTANCE                           | :heavy_check_mark:       | :red_circle:       |
|4.7            | - includes other node                         | :heavy_multiplication_x: | :red_circle:       |
|4.8            | - missing tableref                            | :heavy_multiplication_x: | :red_circle:       |
|4.9            | - empty tableref                              | :heavy_multiplication_x: | :red_circle:       |
|**INSTANCE**   |                                               |                          |                    |
|5.1            | - ID + dmrole + dmtype + PK + A + I + R + C   | :heavy_check_mark:       | :red_circle:       |
|5.2            | - missing ID                                  | :heavy_check_mark:       | :red_circle:       |
|5.3            | - missing dmrole                              | :heavy_multiplication_x: | :red_circle:       |
|5.4            | - missing dmtype                              | :heavy_multiplication_x: | :red_circle:       |
|5.5            | - empty ID                                    | :heavy_multiplication_x: | :red_circle:       |
|5.6            | - empty dmrole                                | :heavy_check_mark:       | :red_circle:       |
|5.7            | - empty dmtype                                | :heavy_multiplication_x: | :red_circle:       |
|5.8            | - missing PRIMARY_KEY node                    | :heavy_check_mark:       | :red_circle:       |
|5.9            | - missing ATTRIBUTE                           | :heavy_check_mark:       | :red_circle:       |
|5.10           | - missing INSTANCE                            | :heavy_check_mark:       | :red_circle:       |
|5.11           | - missing REFERENCE                           | :heavy_check_mark:       | :red_circle:       |
|5.12           | - missing COLLECTION                          | :heavy_check_mark:       | :red_circle:       |
|5.13           | - PRIMARY_KEY not first                       | :heavy_multiplication_x: | :red_circle:       |
|5.14           | - multiple PRIMARY_KEY nodes                  | :heavy_check_mark:       | :red_circle:       |
|5.15           | - multiple subnodes (A,I,R,C), random order   | :heavy_check_mark:       | :red_circle:       |
|5.16           | - includes other node                         | :heavy_multiplication_x: | :red_circle:       |
|**REFERENCE**  |                                               |                          |                    |
|6.1            | - dmrole + dmref                              | :heavy_check_mark:       | :red_circle:       |
|6.2            | - dmrole + tableref + FOREIGN_KEY             | :heavy_check_mark:       | :red_circle:       |
|6.3            | - dmrole only (must have one or other)      | :heavy_multiplication_x: | :red_circle:       |
|6.4            | - dmrole + dmref + tableref (not both)        | :heavy_multiplication_x: | :red_circle:       |
|6.5            | - missing dmrole                              | :heavy_multiplication_x: | :red_circle:       |
|6.6            | - tableref must have FOREIGN_KEY              | :heavy_multiplication_x: | :red_circle:       |
|6.7            | - dmref must NOT have FOREIGN_KEY             | :heavy_multiplication_x: | :red_circle:       |
|6.8            | - multiple FOREIGN_KEY nodes                  | :heavy_check_mark:       | :red_circle:       |
|6.9            | - empty dmrole                                | :heavy_multiplication_x: | :red_circle:       |
|6.10           | - empty tableref                              | :heavy_multiplication_x: | :red_circle:       |
|6.11           | - empty dmref                                 | :heavy_multiplication_x: | :red_circle:       |
|**ATTRIBUTE**  |                                               |                          |                    |
|7.1            | - dmrole + dmtype + ref                       | :heavy_check_mark:       | :red_circle:       |
|7.2            | - dmrole + dmtype + value                     | :heavy_check_mark:       | :red_circle:       |
|7.3            | - dmrole + dmtype + ref + value               | :heavy_check_mark:       | :red_circle:       |
|7.4            | - dmrole + dmtype (must have one, or both)    | :heavy_multiplication_x: | :red_circle:       |
|7.5            | - dmrole + dmtype + value + unit              | :heavy_check_mark:       | :red_circle:       |
|7.6            | - dmrole + dmtype + ref + unit                | :heavy_check_mark:       | :red_circle:       |
|7.7            | - missing dmrole                              | :heavy_multiplication_x: | :red_circle:       |
|7.8            | - missing dmtype                              | :heavy_multiplication_x: | :red_circle:       |
|7.9            | - empty dmrole                                | :heavy_multiplication_x: | :red_circle:       |
|7.10           | - empty dmtype                                | :heavy_multiplication_x: | :red_circle:       |
|7.11           | - empty ref                                   | :heavy_multiplication_x: | :red_circle:       |
|7.12           | - empty value                                 | :heavy_check_mark:       | :red_circle:       |
|7.13           | - include arrayindex                          | :heavy_check_mark:       | :red_circle:       |
|7.14           | - arrayindex value < 0                        | :heavy_multiplication_x: | :red_circle:       |
|**COLLECTION** |                                               |                          |                    |
|8.1            | - ID + dmrole only (empty collection)         | :heavy_check_mark:       | :red_circle:       |
|8.2            | - missing ID                                  | :heavy_check_mark:       | :red_circle:       |
|8.3            | - missing dmrole                              | :heavy_multiplication_x: | :red_circle:       |
|8.4            | - empty ID                                    | :heavy_multiplication_x: | :red_circle:       |
|8.5            | - empty dmrole                                | :heavy_check_mark:       | :red_circle:       |
|8.6            | - dmrole + ATTRIBUTE                          | :heavy_check_mark:       | :red_circle:       |
|8.7            | - dmrole + REFERENCE                          | :heavy_check_mark:       | :red_circle:       |
|8.8            | - dmrole + INSTANCE                           | :heavy_check_mark:       | :red_circle:       |
|8.9            | - dmrole + JOIN                               | :heavy_check_mark:       | :red_circle:       |
|8.10           | - dmrole + COLLECTION                         | :heavy_check_mark:       | :red_circle:       |
|8.11           | - dmrole + multiple (A,R), random order       | :heavy_check_mark:       | :red_circle:       |
|8.12           | - dmrole + multiple (I,J,C), random order     | :heavy_check_mark:       | :red_circle:       |
|8.13           | - dmrole + ATTRIBUTE + INSTANCE (mixed set)   | :heavy_multiplication_x: | :red_circle:       |
|**JOIN**       |                                               |                          |                    |
|9.1            | - dmref                                       | :heavy_check_mark:       | :red_circle:       |
|9.2            | - tableref                                    | :heavy_check_mark:       | :red_circle:       |
|9.3            | - empty (must have one or other)              | :heavy_multiplication_x: | :red_circle:       |
|9.4            | - dmref + tableref (not both)                 | :heavy_multiplication_x: | :red_circle:       |
|9.5            | - dmref + WHERE                               | :heavy_check_mark:       | :red_circle:       |
|9.6            | - tableref + WHERE                            | :heavy_check_mark:       | :red_circle:       |
|9.7            | - empty dmref                                 | :heavy_multiplication_x: | :red_circle:       |
|9.8            | - empty tableref                              | :heavy_multiplication_x: | :red_circle:       |
|**WHERE**      |                                               |                          |                    |
|10.1           | - primarykey only                             | :heavy_check_mark:       | :red_circle:       |
|10.2           | - primarykey + foreignkey                     | :heavy_check_mark:       | :red_circle:       |
|10.3           | - primarykey + value                          | :heavy_check_mark:       | :red_circle:       |
|10.4           | - foreignkey + value                          | :heavy_check_mark:       | :red_circle:       |
|10.5           | - foreignkey only                             | :heavy_multiplication_x: | :red_circle:       |
|10.6           | - value only (must have pk,fk with value)     | :heavy_multiplication_x: | :red_circle:       |
|10.7           | - primarykey + foreignkey + value  (not all)  | :heavy_multiplication_x: | :red_circle:       |
|10.8           | - empty (must have valid combo)               | :heavy_multiplication_x: | :red_circle:       |
|10.9           | - empty primarykey                            | :heavy_multiplication_x: | :red_circle:       |
|10.10          | - empty foreignkey                            | :heavy_multiplication_x: | :red_circle:       |
|10.11          | - empty value                                 | :heavy_check_mark:       | :red_circle:       |
|**PRIMARY_KEY**|                                               |                          |                    |
|11.1           | - dmtype + ref                                | :heavy_check_mark:       | :red_circle:       |
|11.2           | - dmtype + value                              | :heavy_check_mark:       | :red_circle:       |
|11.3           | - dmtype only  (must have one or other)       | :heavy_multiplication_x: | :red_circle:       |
|11.4           | - dmtype + ref + value (not both)             | :heavy_multiplication_x: | :red_circle:       |
|11.5           | - missing dmtype                              | :heavy_multiplication_x: | :red_circle:       |
|11.6           | - empty dmtype                                | :heavy_multiplication_x: | :red_circle:       |
|11.7           | - empty ref                                   | :heavy_multiplication_x: | :red_circle:       |
|11.8           | - empty value                                 | :heavy_check_mark:       | :red_circle:       |
|**FOREIGN_KEY**|                                               |                          |                    |
|12.1           | - ref                                         | :heavy_check_mark:       | :red_circle:       |
|12.2           | - missing ref                                 | :heavy_multiplication_x: | :red_circle:       |
|12.3           | - empty ref                                   | :heavy_multiplication_x: | :red_circle:       |
