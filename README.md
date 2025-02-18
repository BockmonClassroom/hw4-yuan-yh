[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hiWoDjT-)
# HW4
HW 4
(Due 2/17)
Part 1 (50 points): Normalization and Standardization 
Take the iris data set and create two new .csv data sets (25 points each). One that normalizes all columns to have values between 0 and 1 and a second that standardizes all columns to have a mean of 0 and standard deviation of 1.
Push both files to github. 

Part 2 (50 points): ER Diagram 
Create an ER diagram that models a zoo:
Define at least three entities that have several attributes for each entity, their relationship between entities, and their constraints. Argue your decisions. You will graded based on your explanation on why you chose certain constraints. 
What to submit 
Either create a markdown readme file that has a copy of your ER diagram and explanation or .pdf version and push that to github.
Please also submit a link to your github submission to Canvas as well. This helps the TA grade faster. 


## Part 1
After loading the Iris dataset, all numeric columns were separated from the categorical `Species` column.

For the first version of normalizing all columns between 0 and 1, `MinMaxScaler` was used to normalize the features and saves the result as `iris_normalized.csv` under the data folder. 

For another version of standardization to have a mean of 0 and standard deviation of 1, `StandardScaler` was used for standardization and saves the output as `iris_standardized.csv` under the data folder as well.

## Part 2
### Entity & Attributes
1. **Animal**
- `Animal_ID` (Primary Key)
- `Name`
- `Gender`
- `Age`
- `Species`
- `Enclosure_ID` (Foreign Key referencing Enclosure)

2. **Enclosure**
- `Enclosure_ID` (Primary Key)
- `Type` (like aquarium or aviary)
- `Capacity` (Maximum number of animals)
- `Location`

3. **Zookeeper**
- `Zookeeper_ID` (Primary Key)
- `Name`
- `Start_Date` (the first date to start this job)

4. **Zookeeper_Enclosure (Junction Table)**
- Zookeeper_ID (Foreign Key referencing Zookeeper)
- Enclosure_ID (Foreign Key referencing Enclosure)

### Relationship & Constraint
1. **Animal ↔ Enclosure (Many-to-One Relationship)**
- Each animal must belong to an enclosure.
- Each enclosure can hold multiple animals, depending on its capacity.
**Constraint:**
- The number of animals in an enclosure cannot exceed its capacity.
- Each animal can only be assigned to one enclosure.
- The main reason is to ensure that animals have enough space, maintaining zoo regulations and promising animal welfare. Also an animal cannot live in more than one enclosure at a time: it is either assigned to one enclosure or not assigned at all.

2. **Zookeeper ↔ Enclosure (Many-to-Many Relationship)**
- One zookeeper can be responsible for multiple enclosures.
- Each enclosure can have multiple assigned zookeepers.
**Constraint:** 
- A zookeeper cannot manage more than a reasonable number (e.g. 5) of enclosures. For example, one zookeeper cannot be responsible for all enclosures at the same time.
- Each enclosure must have at least one assigned zookeeper to function well (support animal life).
- The main reason is to provide work-life balance for zookeepers as well as ensuring all animals receiving proper management and attention.

3. **Zookeeper ↔ Animal (Many-to-Many Relationship)**
- A zookeeper can take care of multiple animals.
- An animal can be taken cared by multiple zookeepers.
**Constraint:**
- An animal must have at least one assigned zookeeper.
- The main reason is to ensure each animal has received adequate attention by the assigned caretakers for promising animal welfare.

### ER Diagram
![Alt text]([https://github.com/username/repo/assets/image.png](https://github.com/BockmonClassroom/hw4-yuan-yh/blob/main/er.jpeg))
