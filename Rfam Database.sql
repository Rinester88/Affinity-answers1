Rfam Database


public SQL DB: docs.rfam.org/en/latest/database.html

a. How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)

USE Rfam;

1. Count of Distinct Tiger Types
To determine the number of distinct tiger species/types present in the taxonomy table.

Query:

SELECT COUNT(DISTINCT species) AS NumberOfTigerTypes
FROM taxonomy
WHERE species LIKE '%tiger%';

2. Retrieving ncbi_id for Sumatran Tiger
To retrieve the ncbi_id associated with the Sumatran Tiger.

Query:

SELECT ncbi_id
FROM taxonomy
WHERE species = 'Panthera tigris sumatrae';





b. Find all the columns that can be used to connect the tables in the given database.

3. Columns Connecting Database Tables
To identify columns that link tables within the Rfam database schema.

Query:

SELECT 
    TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
FROM 
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE 
    REFERENCED_TABLE_NAME IS NOT NULL	
AND TABLE_SCHEMA = 'Rfam';



c. Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)


4. Type of Rice with Longest DNA Sequence
To determine which type of rice has the maximum DNA sequence length.

SELECT 
    t.species AS RiceType, 
    MAX(r.length) AS LongestDNASequence
FROM 
    rfamseq r
JOIN 
    taxonomy t ON r.ncbi_id = t.ncbi_id
WHERE 
    t.species LIKE '%rice%'
GROUP BY 
    t.species
ORDER BY 
    LongestDNASequence DESC
LIMIT 1;


d. We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

5.Joining family and full_region Tables
To display records by joining the family table with the full_region table using the rfam_acc column.

Query:

SELECT 
    f.*, fr.*
FROM 
    family f
JOIN 
    full_region fr ON f.rfam_acc = fr.rfam_acc;

6. Retrieving Family Names and DNA Sequence Length

To obtain family names and the corresponding sequence lengths.

Query:

SELECT 
    f.rfam_acc,
    f.rfam_id AS FamilyName,
    rs.length AS SequenceLength
FROM 
    family f
JOIN 
    full_region fr ON f.rfam_acc = fr.rfam_acc
JOIN 
    rfamseq rs ON fr.rfamseq_acc = rs.rfamseq_acc;

7. Paginated List of Family Names with DNA Sequence Length > 1,000,000

To retrieve a paginated list of family names and their longest DNA sequence lengths in descending order where the sequence length is greater than 1,000,000. The results show the 9th page with 15 results per page.

Query:

SELECT 
    f.rfam_acc AS FamilyAccessionID,
    f.rfam_id AS FamilyName,
    MAX(rs.length) AS LongestDNASequence
FROM 
    family f
JOIN 
    full_region fr ON f.rfam_acc = fr.rfam_acc
JOIN 
    rfamseq rs ON fr.rfamseq_acc = rs.rfamseq_acc
GROUP BY 
    f.rfam_acc, f.rfam_id
HAVING 
    MAX(rs.length) > 1000000
ORDER BY 
    LongestDNASequence DESC
LIMIT 15 OFFSET 120;
