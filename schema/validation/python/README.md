
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

| Case          | Description                                   | Valid?<br> :heavy_check_mark: = expected valid<br> :heavy_multiplication_x: = expected invalid | Implemented? <br> :white_check_mark: = implemented <br> :red_circle: = not implemented <br> :x: = test fails  |
|:---           |:---                                           |:----                     |:----               |
|**VODML**      |                                               |                          |                    |
|1.1            | - MODEL + GLOBALS + TEMPLATES                 | :heavy_check_mark:       | :white_check_mark: |
|1.2            | - MODEL + GLOBALS; TEMPLATES optional         | :heavy_check_mark:       | :white_check_mark: |
|1.3            | - MODEL + TEMPLATES; GLOBALS optional         | :heavy_check_mark:       | :white_check_mark: |
|1.4            | - MODEL only                                  | :heavy_check_mark:       | :white_check_mark: |
|1.5            | - empty; MODEL required                       | :heavy_multiplication_x: | :white_check_mark: |
|1.6            | - GLOBALS + MODEL + TEMPLATES (order)         | :heavy_multiplication_x: | :white_check_mark: |
|1.7            | - MODEL + TEMPLATES + GLOBALS (order)         | :heavy_multiplication_x: | :white_check_mark: |
|1.8            | - multiple MODEL nodes                        | :heavy_check_mark:       | :white_check_mark: |
|1.9            | - multiple TEMPLATES nodes                    | :heavy_check_mark:       | :white_check_mark: |
|1.10           | - multiple GLOBALS nodes                      | :heavy_multiplication_x: | :white_check_mark: |
|1.11           | - includes other node                         | :heavy_multiplication_x: | :white_check_mark: |
|**MODEL**      |                                               |                          |                    |
|2.1            | - name + url (standard syntax)                | :heavy_check_mark:       | :white_check_mark: |
|2.2            | - name only                                   | :heavy_check_mark:       | :white_check_mark: |
|2.3            | - empty (missing name)                        | :heavy_multiplication_x: | :white_check_mark: |
|2.4            | - name=empty                                  | :heavy_multiplication_x: | :white_check_mark: |
|2.5            | - url=empty                                   | :heavy_multiplication_x: | :white_check_mark: |
|**GLOBALS**    |                                               |                          |                    |
|3.1            | - COLLECTION + INSTANCE                       | :heavy_check_mark:       | :white_check_mark: |
|3.2            | - COLLECTION only                             | :heavy_check_mark:       | :white_check_mark: |
|3.3            | - INSTANCE only                               | :heavy_check_mark:       | :white_check_mark: |
|3.4            | - multiple subnodes (C,I), random order       | :heavy_check_mark:       | :white_check_mark: |
|3.5            | - empty, no subnodes                          | :heavy_check_mark:       | :white_check_mark: |
|3.6            | - includes other node                         | :heavy_multiplication_x: | :white_check_mark: |
|3.7            | - children may have empty or no dmrole        | :heavy_check_mark:       | :white_check_mark: |
|3.8            | - INSTANCE child with non-empty dmrole        | :heavy_multiplication_x: | :white_check_mark: |
|3.11           | - INSTANCE child may have no ID               | :heavy_check_mark:       | :white_check_mark: :x: |
|**TEMPLATES**  |                                               |                          |                    |
|4.1            | - INSTANCE only; WHERE optional               | :heavy_check_mark:       | :white_check_mark: |
|4.2            | - WHERE + INSTANCE                            | :heavy_check_mark:       | :white_check_mark: |
|4.3            | - WHERE only; INSTANCE required               | :heavy_multiplication_x: | :white_check_mark: |
|4.4            | - INSTANCE + WHERE (order)                    | :heavy_multiplication_x: | :white_check_mark: |
|4.5            | - multiple WHERE                              | :heavy_check_mark:       | :white_check_mark: |
|4.6            | - multiple INSTANCE                           | :heavy_check_mark:       | :white_check_mark: |
|4.7            | - includes other node                         | :heavy_multiplication_x: | :white_check_mark: |
|4.8            | - missing tableref (conditionally optional)   | :heavy_check_mark:       | :white_check_mark: |
|4.9            | - empty tableref                              | :heavy_multiplication_x: | :white_check_mark: |
|**INSTANCE**   |                                               |                          |                    |
|-------------- | **Child of GLOBALS**                          |                          |                    |
|5.1            | - ID       + dmrole       + dmtype            : :heavy_multiplication_x: | :white_check_mark: |
|5.2            | - no ID    + dmrole       + dmtype            : :heavy_multiplication_x: | :white_check_mark: |
|5.3            | - ID       + empty dmrole + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.4            | - no ID    + empty dmrole + dmtype            | :heavy_check_mark:       | :white_check_mark: :x: |
|5.5            | - ID       + no dmrole    + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.6            | - no ID    + no dmrole    + dmtype            | :heavy_check_mark:       | :white_check_mark: :x: |
|5.7            | - empty ID + valid dmrole + valid dmtype      | :heavy_multiplication_x: | :white_check_mark: |
|5.8            | - valid ID + valid dmrole + no dmtype         | :heavy_multiplication_x: | :white_check_mark: |
|5.9            | - valid ID + valid dmrole + empty dmtype      | :heavy_multiplication_x: | :white_check_mark: |
|-------------- | **Child of TEMPLATES**                        |                          |                    |
|5.10           | - ID       + dmrole       + dmtype            | :heavy_multiplication_x: | :white_check_mark: :x: |
|5.11           | - no ID    + dmrole       + dmtype            | :heavy_multiplication_x: | :white_check_mark: :x: |
|5.12           | - ID       + empty dmrole + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.13           | - no ID    + empty dmrole + dmtype            | :heavy_check_mark:       | :white_check_mark: :x: |
|5.14           | - ID       + no dmrole    + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.15           | - no ID    + no dmrole    + dmtype            | :heavy_check_mark:       | :white_check_mark: :x: |
|5.16           | - empty ID + valid dmrole + valid dmtype      | :heavy_multiplication_x: | :white_check_mark: :bug: |
|5.17           | - valid ID + valid dmrole + no dmtype         | :heavy_multiplication_x: | :white_check_mark: |
|5.18           | - valid ID + valid dmrole + empty dmtype      | :heavy_multiplication_x: | :white_check_mark: |
|-------------- | **Child of COLLECTION**, for ORM selection    |                          |                    |
|5.20           | - ID       + dmrole       + dmtype            | :heavy_multiplication_x: | :white_check_mark: |
|5.21           | - no ID    + dmrole       + dmtype            | :heavy_multiplication_x: | :white_check_mark: |
|5.22           | - ID       + empty dmrole + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.23           | - no ID    + empty dmrole + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.24           | - ID       + no dmrole    + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.25           | - no ID    + no dmrole    + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.26           | - empty ID + valid dmrole + valid dmtype      | :heavy_multiplication_x: | :white_check_mark: |
|5.27           | - valid ID + valid dmrole + no dmtype         | :heavy_multiplication_x: | :white_check_mark: |
|5.28           | - valid ID + valid dmrole + empty dmtype      | :heavy_multiplication_x: | :white_check_mark: |
|5.29           | - no PRIMARY_KEY                              | :heavy_multiplication_x: | :white_check_mark: :x: |
|-------------- | **Child of COLLECTION**, as array/list        |                          |                    |
|5.30           | - ID       + dmrole       + dmtype            | :heavy_multiplication_x: | :white_check_mark: |
|5.31           | - no ID    + dmrole       + dmtype            | :heavy_multiplication_x: | :white_check_mark: |
|5.32           | - ID       + empty dmrole + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.33           | - no ID    + empty dmrole + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.34           | - ID       + no dmrole    + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.35           | - no ID    + no dmrole    + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.36           | - empty ID + valid dmrole + valid dmtype      | :heavy_multiplication_x: | :white_check_mark: |
|5.37           | - valid ID + valid dmrole + no dmtype         | :heavy_multiplication_x: | :white_check_mark: |
|5.38           | - valid ID + valid dmrole + empty dmtype      | :heavy_multiplication_x: | :white_check_mark: |
|-------------- | **Child of INSTANCE**                         |                          |                    |
|5.40           | - ID       + dmrole       + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.41           | - no ID    + dmrole       + dmtype            | :heavy_check_mark:       | :white_check_mark: |
|5.42           | - ID       + empty dmrole + dmtype            | :heavy_multiplication_x: | :white_check_mark: |
|5.43           | - no ID    + empty dmrole + dmtype            | :heavy_multiplication_x: | :white_check_mark: |
|5.44           | - ID       + no dmrole    + dmtype            | :heavy_multiplication_x: | :white_check_mark: :bug: |
|5.45           | - no ID    + no dmrole    + dmtype            | :heavy_multiplication_x: | :white_check_mark: :bug: |
|5.46           | - empty ID + valid dmrole + valid dmtype      | :heavy_multiplication_x: | :white_check_mark: :bug: |
|5.47           | - valid ID + valid dmrole + no dmtype         | :heavy_multiplication_x: | :white_check_mark: :bug: |
|5.48           | - valid ID + valid dmrole + empty dmtype      | :heavy_multiplication_x: | :white_check_mark: :bug: |
|-------------- | **Content**                                   |                          |                    |
|5.50           | - no children                                 | :heavy_check_mark:       | :white_check_mark: |
|5.51           | - with PRIMARY_KEY as first                   | :heavy_check_mark:       | :white_check_mark: |
|5.53           | - with ATTRIBUTE                              | :heavy_check_mark:       | :white_check_mark: |
|5.54           | - with INSTANCE                               | :heavy_check_mark:       | :white_check_mark: |
|5.55           | - with REFERENCE                              | :heavy_check_mark:       | :white_check_mark: |
|5.56           | - with COLLECTION                             | :heavy_check_mark:       | :white_check_mark: |
|5.57           | - PRIMARY_KEY not first                       | :heavy_multiplication_x: | :white_check_mark: |
|5.58           | - multiple subnodes (A,I,R,C), random order   | :heavy_check_mark:       | :white_check_mark: |
|5.59           | - contains subnode other than (PK,A,I,R,C)    | :heavy_multiplication_x: | :white_check_mark: |
|               |                                               |                          |                    |
|**REFERENCE**  |                                               |                          |                    |
|6.1            | - dmrole + dmref                              | :heavy_check_mark:       | :white_check_mark: |
|6.2            | - dmrole + tableref + FOREIGN_KEY             | :heavy_check_mark:       | :white_check_mark: |
|6.3            | - dmrole only (must have one or other)        | :heavy_multiplication_x: | :white_check_mark: |
|6.4            | - dmrole + dmref + tableref (not both)        | :heavy_multiplication_x: | :white_check_mark: |
|6.5            | - missing dmrole                              | :heavy_multiplication_x: | :white_check_mark: |
|6.6            | - tableref must have FOREIGN_KEY              | :heavy_multiplication_x: | :white_check_mark: |
|6.7            | - dmref must NOT have FOREIGN_KEY             | :heavy_multiplication_x: | :white_check_mark: |
|6.8            | - multiple FOREIGN_KEY nodes                  | :heavy_check_mark:       | :white_check_mark: |
|6.9            | - empty dmrole                                | :heavy_multiplication_x: | :white_check_mark: |
|6.10           | - empty tableref                              | :heavy_multiplication_x: | :white_check_mark: |
|6.11           | - empty dmref                                 | :heavy_multiplication_x: | :white_check_mark: |
|**ATTRIBUTE**  |                                               |                          |                    |
|7.1            | - dmrole + dmtype + value                     | :heavy_check_mark:       | :white_check_mark: |
|7.2            | - dmrole + dmtype + ref                       | :heavy_check_mark:       | :white_check_mark: |
|7.3            | - dmrole + dmtype + ref + value               | :heavy_check_mark:       | :white_check_mark: |
|7.4            | - dmrole + dmtype (must have one, or both)    | :heavy_multiplication_x: | :white_check_mark: |
|7.5            | - dmrole + dmtype + value + unit              | :heavy_check_mark:       | :white_check_mark: |
|7.6            | - dmrole + dmtype + ref + unit                | :heavy_check_mark:       | :white_check_mark: |
|7.7            | - dmrole + dmtype + ref + arrayindex          | :heavy_check_mark:       | :white_check_mark: |
|7.8            | - dmrole + dmtype + value + arrayindex        | :heavy_multiplication_x: | :white_check_mark: |
|7.9            | - missing dmrole                              | :heavy_multiplication_x: | :white_check_mark: |
|7.10           | - missing dmtype                              | :heavy_multiplication_x: | :white_check_mark: |
|7.11           | - empty dmrole                                | :heavy_multiplication_x: | :white_check_mark: |
|7.12           | - empty dmtype                                | :heavy_multiplication_x: | :white_check_mark: |
|7.13           | - empty ref                                   | :heavy_multiplication_x: | :white_check_mark: |
|7.14           | - empty value                                 | :heavy_check_mark:       | :white_check_mark: |
|7.15           | - arrayindex value < 0                        | :heavy_multiplication_x: | :white_check_mark: |
|**COLLECTION** |                                               |                          |                    |
|-------------- | **Child of GLOBALS**                          |                          |                    |
|8.1            | - ID, no dmrole                               | :heavy_check_mark:       | :white_check_mark: |
|8.2            | - no ID, no dmrole                            | :heavy_multiplication_x: | :white_check_mark: |
|8.3            | - empty ID, no dmrole                         | :heavy_multiplication_x: | :white_check_mark: |
|8.4            | - ID, empty dmrole                            | :heavy_check_mark:       | :white_check_mark: |
|8.5            | - ID, dmrole                                  | :heavy_multiplication_x: | :white_check_mark: |
|8.6            | - no children (empty collection)              | :heavy_check_mark:       | :white_check_mark: |
|8.7            | - with INSTANCE children                      | :heavy_check_mark:       | :white_check_mark: |
|8.8            | - with non-INSTANCE children (A,R,J)          | :heavy_multiplication_x: | :white_check_mark: :x: |
|8.9            | - with other child node                       | :heavy_multiplication_x: | :white_check_mark: |
|-------------- | **Child of INSTANCE**                         |                          |                    |
|8.10           | - ID + dmrole                                 | :heavy_multiplication_x: | :white_check_mark: :x: |
|8.11           | - empty ID, dmrole                            | :heavy_multiplication_x: | :white_check_mark: |
|8.12           | - no ID, no dmrole                            | :heavy_multiplication_x: | :white_check_mark: |
|8.13           | - no ID, empty dmrole                         | :heavy_multiplication_x: | :white_check_mark: |
|8.14           | - no ID, dmrole                               | :heavy_check_mark:       | :white_check_mark: |
|8.15           | - no children (empty collection)              | :heavy_check_mark:       | :white_check_mark: |
|8.16           | - dmrole + ATTRIBUTE                          | :heavy_check_mark:       | :white_check_mark: |
|8.17           | - dmrole + REFERENCE                          | :heavy_check_mark:       | :white_check_mark: |
|8.18           | - dmrole + INSTANCE                           | :heavy_check_mark:       | :white_check_mark: |
|8.19           | - dmrole + JOIN                               | :heavy_check_mark:       | :white_check_mark: |
|8.20           | - dmrole + INSTANCE  + JOIN                   | :heavy_check_mark:       | :white_check_mark: |
|8.21           | - dmrole + ATTRIBUTE + (R,I,J)                | :heavy_multiplication_x: | :white_check_mark: |
|8.22           | - dmrole + REFERENCE + (A,I,J)                | :heavy_multiplication_x: | :white_check_mark: :x: |
|8.23           | - dmrole + INSTANCE + (A,R)                   | :heavy_multiplication_x: | :white_check_mark: |
|8.24           | - dmrole + other (not A,R,I,J)                | :heavy_multiplication_x: | :white_check_mark: |
|**JOIN**       |                                               |                          |                    |
|9.1            | - dmref                                       | :heavy_check_mark:       | :white_check_mark: |
|9.2            | - tableref                                    | :heavy_check_mark:       | :white_check_mark: |
|9.3            | - empty (must have one or other)              | :heavy_multiplication_x: | :white_check_mark: |
|9.4            | - dmref + tableref (not both)                 | :heavy_multiplication_x: | :white_check_mark: |
|9.5            | - dmref + WHERE                               | :heavy_check_mark:       | :white_check_mark: |
|9.6            | - tableref + WHERE                            | :heavy_check_mark:       | :white_check_mark: |
|9.7            | - empty dmref                                 | :heavy_multiplication_x: | :white_check_mark: |
|9.8            | - empty tableref                              | :heavy_multiplication_x: | :white_check_mark: |
|**WHERE**      |                                               |                          |                    |
|10.1           | - primarykey only                             | :heavy_multiplication_x: | :white_check_mark: |
|10.2           | - primarykey + foreignkey                     | :heavy_check_mark:       | :white_check_mark: |
|10.3           | - primarykey + value                          | :heavy_check_mark:       | :white_check_mark: |
|10.4           | - foreignkey + value                          | :heavy_check_mark:       | :white_check_mark: |
|10.5           | - foreignkey only                             | :heavy_multiplication_x: | :white_check_mark: |
|10.6           | - value only (must have pk,fk with value)     | :heavy_multiplication_x: | :white_check_mark: |
|10.7           | - primarykey + foreignkey + value  (not all)  | :heavy_multiplication_x: | :white_check_mark: |
|10.8           | - empty (must have valid combo)               | :heavy_multiplication_x: | :white_check_mark: |
|10.9           | - empty primarykey                            | :heavy_multiplication_x: | :white_check_mark: |
|10.10          | - empty foreignkey                            | :heavy_multiplication_x: | :white_check_mark: |
|10.11          | - empty value                                 | :heavy_check_mark:       | :white_check_mark: |
|**PRIMARY_KEY**|                                               |                          |                    |
|11.1           | - dmtype + ref                                | :heavy_check_mark:       | :white_check_mark: |
|11.2           | - dmtype + value                              | :heavy_check_mark:       | :white_check_mark: |
|11.3           | - dmtype only  (must have one or other)       | :heavy_multiplication_x: | :white_check_mark: |
|11.4           | - dmtype + ref + value (not both)             | :heavy_multiplication_x: | :white_check_mark: |
|11.5           | - missing dmtype                              | :heavy_multiplication_x: | :white_check_mark: |
|11.6           | - empty dmtype                                | :heavy_multiplication_x: | :white_check_mark: |
|11.7           | - empty ref                                   | :heavy_multiplication_x: | :white_check_mark: |
|11.8           | - empty value                                 | :heavy_check_mark:       | :white_check_mark: |
|**FOREIGN_KEY**|                                               |                          |                    |
|12.1           | - ref                                         | :heavy_check_mark:       | :white_check_mark: |
|12.2           | - missing ref                                 | :heavy_multiplication_x: | :white_check_mark: |
|12.3           | - empty ref                                   | :heavy_multiplication_x: | :white_check_mark: |
