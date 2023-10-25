# Affinity-answers1
1. Programme for Address Verification:

Problem: BestDelivery Courier Company is dealing with goods with erroneous PIN codes, which causes delivery problems.
Solution: A programme that can cross-reference the PIN code in a given address with actual location data is required. The given API, postalpincode.in/Api-Details, will assist in confirming the PIN code's accuracy against the remainder of the address.
Examples: Addresses like "2nd Phase, 80 Feet Rd, Srinivasa Nagar, Bengaluru, 560050" are OK, however "Colony, Bengaluru, 560050" may be erroneous.
Testing: To assure the program's dependability, various test scenarios, including edge situations, must be examined.

2. Interaction with a database:

The context for these actions is a public SQL database, which is documented at docs.rfam.org/en/latest/database.html.
a. In the taxonomy table, identify the different types of tigers and obtain the "ncbi_id" for the Sumatran Tiger.
b. Determine which columns in this database connect tables.
b. Determine the rice variety having the longest DNA sequence.
d. Create a SQL query to paginate a subset of data pertaining to family names and DNA sequence lengths.

3. Unix Shell Scripting Assignment:

The goal is to extract specified fields from a text file obtained from the URL amfiindia.com/spages/NAVAall.txt.

Execution: The shell script should save the Scheme Name and Asset Value fields to a tsv (tab-separated values) file after filtering them. Consider the advantages and disadvantages of storing the data in JSON format.

# My Apporach -
1. was to provide a structured and modular solution capable of integrating with the API and validating addresses.

Modular Code Structure: The function validate_address was designed to be self-contained and reusable. It can be integrated into other applications or used independently. Because of this modularity, the function can be readily extended or updated in the future.

Efficient String Handling: Python's string handling capabilities are used to extract information from addresses such as PIN codes and post office names. I can efficiently extract patterns (such as the PIN code) from the address text using Python's built-in re-module.

Interactions with APIs: The requests library is a popular Python library for making HTTP requests. It streamlines the process of submitting API requests and receiving responses. It is utilised in this program to retrieve data based on the PIN code and the post office's name.

Validation Process: After extracting the PIN code and prospective post office names, the programme compares each to the API data. It checks that the PIN code and post office name are both correct for the specified address. This two-step validation process ensures more accuracy.

Handling Errors: This function is intended to provide feedback on the validation process. It will return relevant notifications if the address does not have a PIN code or if the information do not match the API's data. This guarantees that users receive detailed feedback on what is wrong with the provided address.

Iterative Checking: Rather of depending solely on one component of the address, the programme compares various portions (district, state, and city) against API data to assure accuracy. This thorough validation ensures that there are fewer false positives.

Testing: The programme is tested with a variety of addresses to ensure its efficacy. To ensure that the function operates as expected in diverse contexts, it is critical to test with both right and wrong addresses.

2. My approach to the SQL queries for the Rfam Database is structured and well-thought-out. Let me break down and discuss your methodology:
a .I used the LIKE operator in conjunction with the phrase 'tiger' to determine how many different varieties of tigers exist. This is a reasonable method, assuming that all tiger species have the term 'tiger' in their name.

successfully utilised the exact biological name 'Panthera tigris sumatrae' to acquire the Sumatran Tiger's ncbi_id.

b. Recognising Relational Columns

I used the ``INFORMATION_SCHEMA.KEY_COLUMN_USAGE table``, which contains information on columns in tables that are used to connect them. This approach clearly maps foreign keys, the referencing table, and the referenced table.

c. Identifying the Rice Variety with the Longest DNA Sequence

On the ``ncbi_id``, the JOIN operation between the rfamseq and taxonomy tables is correctly established. The species names that include the phrase 'rice' are then filtered. I may get the rice kind with the longest DNA sequence by utilising GROUP BY and the aggregate function MAX.


d. Results Pagination for Family Names and DNA Sequence Lengths

I started by joining the family table to the full_region table with the ``rfam_acc column``, which is a proper relationship.
Then enlarged the join to include the rfamseq table using the ``rfamseq_acc`` column to obtain the DNA sequence lengths.
last query in this section effectively employs the GROUP BY clause and the HAVING clause to filter out families with DNA sequence lengths larger than 1,000,000.
I used the LIMIT and OFFSET clauses correctly for pagination. Because the 9th page has 15 results per page, you skip the first 8*15 = 120 results, therefore the OFFSET 120.

3. This question is to test your aptitude for writing small shell scripts on Unix. You are given this URL amfiindia.com/spages/NAVAll.txt. Write a shell script that extracts the Scheme Name and Asset Value fields only and saves them in a tsv file. And ever wondered if this data should not be stored in JSON?

I Used GIT BASH because it more easier to use especially for Windows 
- GIT BASH Run Git commands as if they were on Linux or macOS.
- Git Bash provides a Bash emulation environment for running command-line commands comparable to those used on Unix-based systems. 
  this is really helpful for developers who are used to Unix-like command-line operations but are working on a Windows PC.
- Git Bash allows developers to have a consistent command-line interface across platforms. When working on a project with several contributors, this can streamline collaboration and reduce platform-related concerns.
-  making their workflow more efficient.
-  Git Bash comes with an SSH client, making it easier for users to connect to remote servers and manage Git repositories over SSH.

-  Using the URL 
``url="https://www.amfiindia.com/spages/NAVALL.txt"``
- fetching the data from the URL 
``curl -L -A "Mozilla/5.0" "$url" -o NAVALL.txt ``
- Used Mozilla/5.0 because user-agent to mimic a common browser. Some websites might block or return different content based on the user-agent, so this can be useful to get around such restrictions.
- To see the Data
``cat NAVALL.txt``
- To see first 10 lines of loaded data
``head NAVALL.txt``
- Extract the Scheme name and Asset Value and save it into the TSV file
``if [[ ! -f NAVALL.txt ]]; then
    echo "NAVALL.txt not found!"
    exit 1
fi
awk -F';' '{print $2 "\t" $5}' NAVALL.txt > extracted_data.tsv``
