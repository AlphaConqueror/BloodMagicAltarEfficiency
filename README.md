# BloodMagicAltarEfficiency

A Python project to calculate the optimal rune layout for Blood Magic altar.
It enables you to calculate the **most efficient** rune layout for any given **transmutation** or **Well of Suffering**
setup.

## Transmutation

Here are the results for the **most efficient transmutation** of all **Blood Magic slates** using a **tier 6 altar**
with a **rune space of 184**.

### STONE -> BLANK SLATE

|                             |                                                      |
|-----------------------------|------------------------------------------------------|
| RUNE SPACE                  | 184                                                  |
| RUNES OF DISLOCATION        | 12                                                   |
| RUNES OF ACCELERATION       | 19                                                   |
| RUNES OF AUGMENTED CAPACITY | 0                                                    |
| SPEED RUNES                 | 153                                                  |
| TICK FACTOR                 | 1                                                    |
| TRANSFER RATE               | 178.32200896511992 LP/1t ( 178.32200896511992 LP/t ) |
| CONSUMPTION RATE            | 158.0 LP/1t ( 158.0 LP/t )                           |
| BUFFER                      | 1000.0 LP/1t ( 1000.0 LP/t )                         |
| CAPACITY                    | 10000 LP                                             |

### BLANK SLATE -> REINFORCED SLATE

|                             |                                                      |
|-----------------------------|------------------------------------------------------|
| RUNE SPACE                  | 184                                                  |
| RUNES OF DISLOCATION        | 12                                                   |
| RUNES OF ACCELERATION       | 19                                                   |
| RUNES OF AUGMENTED CAPACITY | 0                                                    |
| SPEED RUNES                 | 153                                                  |
| TICK FACTOR                 | 1                                                    |
| TRANSFER RATE               | 178.32200896511992 LP/1t ( 178.32200896511992 LP/t ) |
| CONSUMPTION RATE            | 158.0 LP/1t ( 158.0 LP/t )                           |
| BUFFER                      | 1000.0 LP/1t ( 1000.0 LP/t )                         |
| CAPACITY                    | 10000 LP                                             |

### REINFORCED SLATE -> IMBUED SLATE

|                             |                                                      |
|-----------------------------|------------------------------------------------------|
| RUNE SPACE                  | 184                                                  |
| RUNES OF DISLOCATION        | 18                                                   |
| RUNES OF ACCELERATION       | 19                                                   |
| RUNES OF AUGMENTED CAPACITY | 0                                                    |
| SPEED RUNES                 | 147                                                  |
| TICK FACTOR                 | 1                                                    |
| TRANSFER RATE               | 532.4666656177045 LP/1t ( 532.4666656177045 LP/t )   |
| CONSUMPTION RATE            | 456.00000000000006 LP/1t ( 456.00000000000006 LP/t ) |
| BUFFER                      | 1000.0 LP/1t ( 1000.0 LP/t )                         |
| CAPACITY                    | 10000 LP                                             |

### IMBUED SLATE -> DEMONIC SLATE

|                             |                                                    |
|-----------------------------|----------------------------------------------------|
| RUNE SPACE                  | 184                                                |
| RUNES OF DISLOCATION        | 19                                                 |
| RUNES OF ACCELERATION       | 19                                                 |
| RUNES OF AUGMENTED CAPACITY | 0                                                  |
| SPEED RUNES                 | 146                                                |
| TICK FACTOR                 | 1                                                  |
| TRANSFER RATE               | 638.9599987412454 LP/1t ( 638.9599987412454 LP/t ) |
| CONSUMPTION RATE            | 604.0 LP/1t ( 604.0 LP/t )                         |
| BUFFER                      | 1000.0 LP/1t ( 1000.0 LP/t )                       |
| CAPACITY                    | 10000 LP                                           |

### DEMONIC SLATE -> ETHEREAL SLATE

|                             |                                                    |
|-----------------------------|----------------------------------------------------|
| RUNE SPACE                  | 184                                                |
| RUNES OF DISLOCATION        | 23                                                 |
| RUNES OF ACCELERATION       | 19                                                 |
| RUNES OF AUGMENTED CAPACITY | 1                                                  |
| SPEED RUNES                 | 141                                                |
| TICK FACTOR                 | 1                                                  |
| TRANSFER RATE               | 1324.947453389846 LP/1t ( 1324.947453389846 LP/t ) |
| CONSUMPTION RATE            | 1168.0 LP/1t ( 1168.0 LP/t )                       |
| BUFFER                      | 1200.0 LP/1t ( 1200.0 LP/t )                       |
| CAPACITY                    | 12000 LP                                           |

## Generation

Here is an example of a **Well of Suffering** setup using a **tier 6 altar** with a **rune space of 184** with an
average mob count of 20.

|                             |                                                      |
|-----------------------------|------------------------------------------------------|
| AVERAGE MOB COUNT           | 20                                                   |
| RUNE SPACE                  | 184                                                  |
| RUNES OF DISLOCATION        | 11                                                   |
| RUNES OF ACCELERATION       | 19                                                   |
| RUNES OF AUGMENTED CAPACITY | 0                                                    |
| RUNES OF SACRIFICE          | 154                                                  |
| TICK FACTOR                 | 1                                                    |
| TRANSFER RATE               | 148.60167413759993 LP/1t ( 148.60167413759993 LP/t ) |
| -> WITHIN 25 TICKS          | 3715.0418534399982 LP                                |
| GENERATION RATE             | 3279.9999999999995 LP/25t                            |
| BUFFER                      | 1000.0 LP/1t ( 1000.0 LP/t )                         |
| CAPACITY                    | 10000 LP                                             |
